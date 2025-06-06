# SecKeychainCopySettings(_:_:)

**Framework**: Security  
**Kind**: func

Obtains a keychain’s settings.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainCopySettings(_ keychain: SecKeychain?, _ outSettings: UnsafeMutablePointer<SecKeychainSettings>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `keychain`: A reference to the keychain from which to copy its settings.
- `outSettings`: On return, a pointer to a keychain settings structure. Since this structure is versioned, you must allocate the memory for it and fill in the version of the structure before passing it to the function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaincopysettings(_:_:))*