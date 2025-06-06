# items

**Framework**: CryptoTokenKit  
**Kind**: property

Returns all items for token in the keychain.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var items: [TKTokenKeychainItem] { get }
```

## See Also

- [func key(forObjectID: TKToken.ObjectID) throws -> TKTokenKeychainKey](tktokenkeychaincontents/key(forobjectid:).md)
  Returns the key for a specified object identifier.
- [func certificate(forObjectID: TKToken.ObjectID) throws -> TKTokenKeychainCertificate](tktokenkeychaincontents/certificate(forobjectid:).md)
  Returns the key for a specified object identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincontents/items)*