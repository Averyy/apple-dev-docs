# key(forObjectID:)

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
func key(forObjectID objectID: TKToken.ObjectID) throws -> TKTokenKeychainKey
```

#### Return Value

The key, or `nil` if no key exists.

## Parameters

- `objectID`: The object identifier for the keychain item.

## See Also

- [var items: [TKTokenKeychainItem]](tktokenkeychaincontents/items.md)
  Returns all items for token in the keychain.
- [func certificate(forObjectID: TKToken.ObjectID) throws -> TKTokenKeychainCertificate](tktokenkeychaincontents/certificate(forobjectid:).md)
  Returns the key for a specified object identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincontents/key(forobjectid:))*