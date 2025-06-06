# SecKeychainCopyDefault(_:)

**Framework**: Security  
**Kind**: func

Retrieves a pointer to the default keychain.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainCopyDefault(_ keychain: UnsafeMutablePointer<SecKeychain?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md). The result code [`errSecNoDefaultKeychain`](errsecnodefaultkeychain.md) indicates that there is no default keychain.

## Parameters

- `keychain`: On return, a pointer to the default keychain object. In Objective-C, call the   function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaincopydefault(_:))*