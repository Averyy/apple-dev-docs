# SecKeychainFindInternetPassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Finds the first Internet password based on the attributes passed.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainFindInternetPassword(_ keychainOrArray: CFTypeRef?, _ serverNameLength: UInt32, _ serverName: UnsafePointer<CChar>?, _ securityDomainLength: UInt32, _ securityDomain: UnsafePointer<CChar>?, _ accountNameLength: UInt32, _ accountName: UnsafePointer<CChar>?, _ pathLength: UInt32, _ path: UnsafePointer<CChar>?, _ port: UInt16, _ protocol: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UnsafeMutablePointer<UInt32>?, _ passwordData: UnsafeMutablePointer<UnsafeMutableRawPointer?>?, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This function finds the first Internet password item that matches the attributes you provide. This function optionally returns a reference to the found item.

This function decrypts the password before returning it to you. If the calling application is not in the list of trusted applications, the user is prompted before access is allowed. If the access controls for this item do not allow decryption, the function returns the `errSecAuthFailed` result code.

This function automatically calls the function [`SecKeychainUnlock(_:_:_:_:)`](seckeychainunlock(_:_:_:_:).md) to display the Unlock Keychain dialog box if the keychain is currently locked.

## Parameters

- `keychainOrArray`: A reference to an array of keychains to search, a single keychain or `NULL` to search the user’s default keychain search list.
- `serverNameLength`: The length of the `serverName` character string.
- `serverName`: A UTF-8 encoded character string representing the server name.
- `securityDomainLength`: The length of the `securityDomain` character string.
- `securityDomain`: A UTF-8 encoded character string representing the security domain. This parameter is optional, as not all protocols require it. Pass `NULL` if it is not required.
- `accountNameLength`: The length of the `accountName` character string.
- `accountName`: A UTF-8 encoded character string representing the account name.
- `pathLength`: The length of the `path` character string.
- `path`: A UTF-8 encoded character string representing the path.
- `port`: The TCP/IP port number. Pass `0` to ignore the port number.
- `protocol`: The protocol associated with this password. See [`SecProtocolType`](secprotocoltype.md) for a description of possible values.
- `authenticationType`: The authentication scheme used. See [`SecAuthenticationType`](secauthenticationtype.md) for a description of possible values. Pass the constant `kSecAuthenticationTypeDefault`, to specify the default authentication scheme.
- `passwordLength`: On return, the length of the buffer pointed to by `passwordData`.
- `passwordData`: On return, a pointer to a buffer containing the password data. Pass `NULL` if you want to obtain the item object but not the password data. In this case, you must also pass `NULL` in the `passwordLength` parameter. You should use the [`SecKeychainItemFreeContent(_:_:)`](seckeychainitemfreecontent(_:_:).md) function to free the memory pointed to by this parameter.
- `itemRef`: On return, a pointer to the item object of the Internet password. You are responsible for releasing your reference to this object. Pass `NULL` if you don’t want to obtain this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainfindinternetpassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*