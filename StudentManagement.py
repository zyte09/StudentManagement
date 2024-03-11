def main():
    print('')
    studentname = input('ENTER STUDENT NAME: ')
    name.append(studentname)
    srcode = input('ENTER STUDENT SR-Code: ')
    sr.append(srcode)
    studentage =  input('ENTER STUDENT AGE: ')
    age.append(studentage)
    studentmajor =  input('ENTER STUDENT MAJOR: ')
    major.append(studentmajor)
    studentemail =  input('ENTER STUDENT E-MAIL ID: ')
    email.append(studentemail)
    studentaddress =  input('ENTER STUDENT ADDRESS: ')
    address.append(studentaddress)

name = []
sr = []
age = []
major = []
email = []
address = []

while True:
    print('PRESS FROM THE FOLLOWING OPTION : ')
    print('\nPRESS 1: TO ADD STUDENT INFORMATION. ')
    print('PRESS 2: TO DELETE STUDENT INFORMATION. ')
    print('PRESS 3: TO UPDATE STUDENT INFORMATION. ')
    print('PRESS 4: TO DISPLAY STUDENT INFORMATION. ')
    print('PRESS 5: TO EXIT SYSTEM. ')

    option = input('ENTER YOU OPTION: ')

    if option == '1':
        main()
        print('SUCCESSFUL')
        continue
    elif option == '2':
        studentname = input('NAME OF THE STUDENT: ')
        if studentname not in name:
            print('INVALID NAME')
        else:
            i = name.index(studentname)
            del name[i]
            del sr[i]
            del age[i]
            del major[i]
            del email[i]
            del address[i]
            print('SUCCESSFUL')
        continue


    elif option == '3':
        studentname = input('NAME OF THE STUDENT: ')
        if studentname not in name:
            print('INVALID NAME')
        else:
            i = name.index(studentname)
            del name[i]
            del sr[i]
            del age[i]
            del major[i]
            del email[i]
            del address[i]
            main()
            print('SUCCESSFUL')
        continue

    elif option == '4':
        studentname = input('NAME OF THE STUDENT: ')
        i = name.index(studentname)
        print('NAME :' + name[i])
        print('SR-CODE : ' + sr[i])
        print('AGE : ' + age[i])
        print('MAJOR : ' + major[i])
        print('EMAIL : ' + email[i] )
        print('ADDRESS : ' + address[i])
        print('SUCCESSFUL')
        continue
    elif option == '5':
        print('\nTHANK YOU. HAVE A GREAT DAY!')
        break