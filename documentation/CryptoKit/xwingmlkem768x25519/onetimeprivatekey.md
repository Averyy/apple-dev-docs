# XWingMLKEM768X25519.OneTimePrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

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
- [var publicKey: XWingMLKEM768X25519.PublicKey](./onetimeprivatekey/publickey.md)
  The corresponding public key.
### Instance Methods
- [func decapsulate(Data) throws -> SymmetricKey](./onetimeprivatekey/decapsulate%28_%29.md)
  Decapsulate a shared secret.
### Type Methods
- [static func generate() throws -> XWingMLKEM768X25519.OneTimePrivateKey](./onetimeprivatekey/generate%28%29.md)
  Generates a new, random one-time-use private key.

## Relationships

### Conforms To
- [KEMOneTimePrivateKey](../kemonetimeprivatekey.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519/onetimeprivatekey)*