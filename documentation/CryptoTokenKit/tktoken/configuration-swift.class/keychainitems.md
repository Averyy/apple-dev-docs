# keychainItems

**Framework**: CryptoTokenKit  
**Kind**: property

The keychain items associated with this token.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var keychainItems: [TKTokenKeychainItem] { get set }
```

## See Also

- [func certificate(for: TKToken.ObjectID) throws -> TKTokenKeychainCertificate](tktoken/configuration-swift.class/certificate(for:).md)
  Returns a certificate from the keychain with the object identifier you specify.
- [func key(for: TKToken.ObjectID) throws -> TKTokenKeychainKey](tktoken/configuration-swift.class/key(for:).md)
  Returns a key from the keychain with the object identifier you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktoken/configuration-swift.class/keychainitems)*