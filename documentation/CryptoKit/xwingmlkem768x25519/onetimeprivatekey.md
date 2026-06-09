# XWingMLKEM768X25519.OneTimePrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519/onetimeprivatekey)*