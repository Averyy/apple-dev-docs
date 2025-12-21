# HPKEKEMPrivateKeyGeneration

**Framework**: Apple CryptoKit  
**Kind**: protocol

A type that represents the generation of private keys in HPKE

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 1.0+
- watchOS 26.0+

## Declaration

```swift
@preconcurrency
protocol HPKEKEMPrivateKeyGeneration : HPKEKEMPrivateKey
```

## Topics

### Initializers
- [init() throws](hpkekemprivatekeygeneration/init.md)
  Creates a private key generator.

## Relationships

### Inherits From
- [HPKEKEMPrivateKey](hpkekemprivatekey.md)
- [KEMPrivateKey](kemprivatekey.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [XWingMLKEM768X25519.PrivateKey](xwingmlkem768x25519/privatekey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpkekemprivatekeygeneration)*