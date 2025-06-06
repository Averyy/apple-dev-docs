# SecKeychainCreate(_:_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Creates an empty keychain.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainCreate(_ pathName: UnsafePointer<CChar>, _ passwordLength: UInt32, _ password: UnsafeRawPointer?, _ promptUser: Bool, _ initialAccess: SecAccess?, _ keychain: UnsafeMutablePointer<SecKeychain?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This function creates an empty keychain. The `keychain`, `password`, and `initialAccess` parameters are optional. If user interaction to create a keychain is posted, the newly-created keychain is automatically unlocked after creation.

The system ensures that a default keychain is created for the user at login, thus, in most cases, you do not need to call this function yourself. Users can create additional keychains, or change the default, by using the Keychain Access application. However, a missing default keychain is not recreated automatically, and you may receive an `errSecNoDefaultKeychain` error from other functions if a default keychain does not exist. In that case, you can use this function followed by [`SecKeychainSetDefault(_:)`](seckeychainsetdefault(_:).md), to create a new default keychain. You can also call this function to create a private temporary keychain for your application’s use, in cases where no user interaction can occur.

## Parameters

- `pathName`: A constant character string representing the POSIX path indicating where to store the keychain.
- `passwordLength`: An unsigned 32-bit integer representing the length of the buffer pointed to by  . Pass   if the value of   is   and the value of   is  .
- `password`: A pointer to the buffer containing the password which is used to protect the new keychain. The password must be in canonical UTF-8 encoding. Pass   if the value of   is   and the value of   is  .
- `promptUser`: A Boolean value representing whether to display a password dialog to the user. Set this value to   to display a password dialog or   otherwise. If you pass  , any values passed for   and   are ignored, and a dialog for the user to enter a password is presented.
- `initialAccess`: Ignored. Pass   for this parameter.
- `keychain`: On return, a pointer to a keychain object. You must call the   function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaincreate(_:_:_:_:_:_:))*