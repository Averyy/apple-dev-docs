# useEnDecryptKey

**Framework**: Security  
**Kind**: property

The key can be used to encrypt or decrypt (wrap or unwrap) a key.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var useEnDecryptKey: SecTrustSettingsKeyUsage { get }
```

#### Discussion

Private keys must be wrapped before they can be exported from a keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustsettingskeyusage/useendecryptkey)*