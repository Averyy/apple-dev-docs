# key(for:)

**Framework**: CryptoTokenKit  
**Kind**: method

Returns a key from the keychain with the object identifier you specify.

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
func key(for objectID: TKToken.ObjectID) throws -> TKTokenKeychainKey
```

#### Return Value

The key that the keychain stores.

#### Discussion

If the key the `objectID` specifies isn’t found, the system fills the `error` with [`TKError.Code.objectNotFound`](tkerror/code/objectnotfound.md).

## Parameters

- `objectID`: The identifier for the key within the keychain.

## See Also

- [var keychainItems: [TKTokenKeychainItem]](tktoken/configuration-swift.class/keychainitems.md)
  The keychain items associated with this token.
- [func certificate(for: TKToken.ObjectID) throws -> TKTokenKeychainCertificate](tktoken/configuration-swift.class/certificate(for:).md)
  Returns a certificate from the keychain with the object identifier you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktoken/configuration-swift.class/key(for:))*