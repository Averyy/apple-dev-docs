# HPKEDiffieHellmanPrivateKeyGeneration

**Framework**: Apple CryptoKit  
**Kind**: protocol

A type that represents the generation of private keys in a Diffie-Hellman key exchange.

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
protocol HPKEDiffieHellmanPrivateKeyGeneration : HPKEDiffieHellmanPrivateKey
```

## Topics

### Initializers
- [init()](hpkediffiehellmanprivatekeygeneration/init.md)
  Creates a private key generator.

## Relationships

### Inherits From
- [DiffieHellmanKeyAgreement](diffiehellmankeyagreement.md)
- [HPKEDiffieHellmanPrivateKey](hpkediffiehellmanprivatekey.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [Curve25519.KeyAgreement.PrivateKey](curve25519/keyagreement/privatekey.md)
- [P256.KeyAgreement.PrivateKey](p256/keyagreement/privatekey.md)
- [P384.KeyAgreement.PrivateKey](p384/keyagreement/privatekey.md)
- [P521.KeyAgreement.PrivateKey](p521/keyagreement/privatekey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpkediffiehellmanprivatekeygeneration)*