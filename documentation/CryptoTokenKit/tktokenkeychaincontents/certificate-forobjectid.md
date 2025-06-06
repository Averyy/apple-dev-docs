# certificate(forObjectID:)

**Framework**: CryptoTokenKit  
**Kind**: method

Returns the key for a specified object identifier.

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
func certificate(forObjectID objectID: TKToken.ObjectID) throws -> TKTokenKeychainCertificate
```

#### Return Value

The certificate, or `nil` if no certificate exists.

## Parameters

- `objectID`: The object identifier for the keychain item.

## See Also

- [var items: [TKTokenKeychainItem]](tktokenkeychaincontents/items.md)
  Returns all items for token in the keychain.
- [func key(forObjectID: TKToken.ObjectID) throws -> TKTokenKeychainKey](tktokenkeychaincontents/key(forobjectid:).md)
  Returns the key for a specified object identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincontents/certificate(forobjectid:))*