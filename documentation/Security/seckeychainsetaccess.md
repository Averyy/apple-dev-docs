# SecKeychainSetAccess(_:_:)

**Framework**: Security  
**Kind**: func

Sets the application access for a keychain.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainSetAccess(_ keychain: SecKeychain?, _ access: SecAccess) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `keychain`: A reference to the keychain for which to set the access. Pass   to specify the default keychain.
- `access`: An access object of type   containing access control lists for the keychain. See   for more information about creating an access object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainsetaccess(_:_:))*