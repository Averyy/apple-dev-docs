# XWingMLKEM768X25519.OneTimePrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct OneTimePrivateKey
```

## Topics

### Instance Properties
- [var publicKey: XWingMLKEM768X25519.PublicKey](xwingmlkem768x25519/onetimeprivatekey/publickey.md)
  The corresponding public key.
### Instance Methods
- [func decapsulate(Data) throws -> SymmetricKey](xwingmlkem768x25519/onetimeprivatekey/decapsulate(_:).md)
  Decapsulate a shared secret.
### Type Methods
- [static func generate() throws -> XWingMLKEM768X25519.OneTimePrivateKey](xwingmlkem768x25519/onetimeprivatekey/generate.md)
  Generates a new, random one-time-use private key.

## Relationships

### Conforms To
- [KEMOneTimePrivateKey](kemonetimeprivatekey.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519/onetimeprivatekey)*