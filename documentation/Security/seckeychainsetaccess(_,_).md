# SecKeychainSetAccess(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Sets the application access for a keychain.

**Availability**:
- macOS 10.2+ - Deprecated in 10.10

> **Deprecated**: In addition to the ACLs for individual keychain items, the keychain itself has ACLs. However, they are currently unused and this function isn’t implemented.

## Declaration

```swift
func SecKeychainSetAccess(_ keychain: SecKeychain?, _ access: SecAccess) -> OSStatus
```

```c
OSStatus SecKeychainSetAccess(SecKeychainRef keychain, SecAccessRef access);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Parameters

- `keychain`: A reference to the keychain for which to set the access. Pass `NULL` to specify the default keychain.
- `access`: An access object of type [`SecAccess`](./secaccess.md) containing access control lists for the keychain. See [Access Control Lists](./access-control-lists.md) for more information about creating an access object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainsetaccess(_:_:))*