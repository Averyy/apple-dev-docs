# key(forObjectID:)

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (TKTokenKeychainKey *) keyForObjectID:(TKTokenObjectID) objectID error:(NSError **) error;
```

## Return Value

The key, or `nil` if no key exists.

## Parameters

- `objectID`: The object identifier for the keychain item.

## See Also

### Accessing Keychain Items
- [var items: [TKTokenKeychainItem]](./items.md)
  Returns all items for token in the keychain.
- [func certificate(forObjectID: TKToken.ObjectID) throws -> TKTokenKeychainCertificate](./certificate%28forobjectid%29.md)
  Returns the key for a specified object identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincontents/key(forobjectid:))*