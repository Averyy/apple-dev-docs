# HPKEDiffieHellmanPublicKey

**Framework**: Apple CryptoKit  
**Kind**: protocol

A type that represents the public key in a Diffie-Hellman key exchange.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@preconcurrency
protocol HPKEDiffieHellmanPublicKey : HPKEPublicKeySerialization
```

## Topics

### Associated Types
- [associatedtype EphemeralPrivateKey : HPKEDiffieHellmanPrivateKeyGeneration](hpkediffiehellmanpublickey/ephemeralprivatekey.md)
  The type of the ephemeral private key.

## Relationships

### Inherits From
- [HPKEPublicKeySerialization](hpkepublickeyserialization.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [Curve25519.KeyAgreement.PublicKey](curve25519/keyagreement/publickey.md)
- [P256.KeyAgreement.PublicKey](p256/keyagreement/publickey.md)
- [P384.KeyAgreement.PublicKey](p384/keyagreement/publickey.md)
- [P521.KeyAgreement.PublicKey](p521/keyagreement/publickey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpkediffiehellmanpublickey)*