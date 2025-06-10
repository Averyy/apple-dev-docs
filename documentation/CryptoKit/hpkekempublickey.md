# HPKEKEMPublicKey

**Framework**: Apple CryptoKit  
**Kind**: protocol

A type that represents the public key in HPKE

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
protocol HPKEKEMPublicKey : HPKEPublicKeySerialization, KEMPublicKey
```

## Topics

### Associated Types
- [associatedtype EphemeralPrivateKey : HPKEKEMPrivateKeyGeneration](hpkekempublickey/ephemeralprivatekey.md)
  The type of the ephemeral private key.

## Relationships

### Inherits From
- [HPKEPublicKeySerialization](hpkepublickeyserialization.md)
- [KEMPublicKey](kempublickey.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [XWingMLKEM768X25519.PublicKey](xwingmlkem768x25519/publickey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpkekempublickey)*