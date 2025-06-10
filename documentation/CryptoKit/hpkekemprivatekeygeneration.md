# HPKEKEMPrivateKeyGeneration

**Framework**: Apple CryptoKit  
**Kind**: protocol

A type that represents the generation of private keys in HPKE

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.0+
- watchOS 26.0+ (Beta)

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