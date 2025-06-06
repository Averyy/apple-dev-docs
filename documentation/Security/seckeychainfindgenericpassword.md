# SecKeychainFindGenericPassword(_:_:_:_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Finds the first generic password based on the attributes passed.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainFindGenericPassword(_ keychainOrArray: CFTypeRef?, _ serviceNameLength: UInt32, _ serviceName: UnsafePointer<CChar>?, _ accountNameLength: UInt32, _ accountName: UnsafePointer<CChar>?, _ passwordLength: UnsafeMutablePointer<UInt32>?, _ passwordData: UnsafeMutablePointer<UnsafeMutableRawPointer?>?, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This function finds the first generic password item that matches the attributes you provide. Most attributes are optional; you should pass only as many as you need to narrow the search sufficiently for your application’s intended use. This function optionally returns a reference to the found item.

This function decrypts the password before returning it to you. If the calling application is not in the list of trusted applications, the user is prompted before access is allowed. If the access controls for this item do not allow decryption, the function returns the `errSecAuthFailed` result code.

This function automatically calls the function [`SecKeychainUnlock(_:_:_:_:)`](seckeychainunlock(_:_:_:_:).md) to display the Unlock Keychain dialog box if the keychain is currently locked.

## Parameters

- `keychainOrArray`: A reference to an array of keychains to search, a single keychain, or   to search the user’s default keychain search list.
- `serviceNameLength`: The length of the   character string.
- `serviceName`: A UTF-8 encoded character string representing the service name.
- `accountNameLength`: The length of the   character string.
- `accountName`: A UTF-8 encoded character string representing the account name.
- `passwordLength`: On return, the length of the buffer pointed to by  .
- `passwordData`: On return, a pointer to a buffer that holds the password data. Pass   if you want to obtain the item object but not the password data. In this case, you must also pass   in the   parameter. You should use the   function to free the memory pointed to by this parameter.
- `itemRef`: On return, a pointer to the item object of the generic password. You are responsible for releasing your reference to this object. Pass   if you don’t want to obtain this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainfindgenericpassword(_:_:_:_:_:_:_:_:))*