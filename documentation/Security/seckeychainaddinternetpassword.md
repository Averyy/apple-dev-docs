# SecKeychainAddInternetPassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Adds a new Internet password to a keychain.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainAddInternetPassword(_ keychain: SecKeychain?, _ serverNameLength: UInt32, _ serverName: UnsafePointer<CChar>?, _ securityDomainLength: UInt32, _ securityDomain: UnsafePointer<CChar>?, _ accountNameLength: UInt32, _ accountName: UnsafePointer<CChar>?, _ pathLength: UInt32, _ path: UnsafePointer<CChar>?, _ port: UInt16, _ protocol: SecProtocolType, _ authenticationType: SecAuthenticationType, _ passwordLength: UInt32, _ passwordData: UnsafeRawPointer, _ itemRef: UnsafeMutablePointer<SecKeychainItem?>?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md). The result code [`errSecNoDefaultKeychain`](errsecnodefaultkeychain.md) indicates that no default keychain could be found. The result code [`errSecDuplicateItem`](errsecduplicateitem.md) indicates that you tried to add a password that already exists in the keychain. The result code [`errSecDataTooLarge`](errsecdatatoolarge.md) indicates that you tried to add more data than is allowed for a structure of this type.

#### Discussion

This function adds a new Internet server password to the specified keychain. Required parameters to identify the password are `serverName` and `accountName` (you cannot pass `NULL` for both parameters). In addition, some protocols may require an optional `securityDomain` when authentication is requested. This function optionally returns a reference to the newly added item.

This function sets the initial access rights for the new keychain item so that the application creating the item is given trusted access.

This function automatically calls the function [`SecKeychainUnlock(_:_:_:_:)`](seckeychainunlock(_:_:_:_:).md) to display the Unlock Keychain dialog box if the keychain is currently locked.

## Parameters

- `keychain`: A reference to the keychain in which to store an Internet password. Pass   to specify the user’s default keychain.
- `serverNameLength`: The length of the   character string.
- `serverName`: A UTF-8 encoded character string representing the server name.
- `securityDomainLength`: The length of the   character string.
- `securityDomain`: A UTF-8 encoded character string representing the security domain. This parameter is optional. Pass NULL if the protocol does not require it.
- `accountNameLength`: The length of the   character string.
- `accountName`: A UTF-8 encoded character string representing the account name.
- `pathLength`: The length of the   character string.
- `path`: A UTF-8 encoded character string representing the path.
- `port`: The TCP/IP port number. If no specific port number is associated with this password, pass  .
- `protocol`: The protocol associated with this password. See   for a description of possible values.
- `authenticationType`: The authentication scheme used. See   for a description of possible values. Pass the constant  , to specify the default authentication scheme.
- `passwordLength`: The length of the   buffer.
- `passwordData`: A pointer to a buffer containing the password data to be stored in the keychain.
- `itemRef`: On return, a pointer to a reference to the new keychain item. Pass   if you don’t want to obtain this object. You must allocate the memory for this pointer. You must call the   function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainaddinternetpassword(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*