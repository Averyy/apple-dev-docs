# certificate(for:)

**Framework**: CryptoTokenKit  
**Kind**: method

Returns a certificate from the keychain with the object identifier you specify.

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
func certificate(for objectID: TKToken.ObjectID) throws -> TKTokenKeychainCertificate
```

#### Return Value

The certificate that the keychain stores.

#### Discussion

If the certificate the `objectID` specifies isn’t found, the system fills `error` with [`TKError.Code.objectNotFound`](tkerror/code/objectnotfound.md).

## Parameters

- `objectID`: The identifier for the certificate within the keychain.

## See Also

- [var keychainItems: [TKTokenKeychainItem]](tktoken/configuration-swift.class/keychainitems.md)
  The keychain items associated with this token.
- [func key(for: TKToken.ObjectID) throws -> TKTokenKeychainKey](tktoken/configuration-swift.class/key(for:).md)
  Returns a key from the keychain with the object identifier you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktoken/configuration-swift.class/certificate(for:))*