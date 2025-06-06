# SecKeychainCopyAccess(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the application access of a keychain.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainCopyAccess(_ keychain: SecKeychain?, _ access: UnsafeMutablePointer<SecAccess?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `keychain`: A reference to the keychain from which to copy the access object. Pass   to specify the default keychain.
- `access`: A pointer to an access object. On return, this points to the access object of the specified keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaincopyaccess(_:_:))*