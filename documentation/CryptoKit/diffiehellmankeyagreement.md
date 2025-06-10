# DiffieHellmanKeyAgreement

**Framework**: Apple CryptoKit  
**Kind**: protocol

A Diffie-Hellman Key Agreement Key

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
protocol DiffieHellmanKeyAgreement : Sendable
```

## Topics

### Associated Types
- [associatedtype PublicKey : Sendable](diffiehellmankeyagreement/publickey-swift.associatedtype.md)
  The public key share type to perform the DH Key Agreement
### Instance Properties
- [var publicKey: Self.PublicKey](diffiehellmankeyagreement/publickey-swift.property.md)
### Instance Methods
- [func sharedSecretFromKeyAgreement(with: Self.PublicKey) throws -> SharedSecret](diffiehellmankeyagreement/sharedsecretfromkeyagreement(with:).md)
  Performs a Diffie-Hellman Key Agreement.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [HPKEDiffieHellmanPrivateKey](hpkediffiehellmanprivatekey.md)
- [HPKEDiffieHellmanPrivateKeyGeneration](hpkediffiehellmanprivatekeygeneration.md)
### Conforming Types
- [Curve25519.KeyAgreement.PrivateKey](curve25519/keyagreement/privatekey.md)
- [P256.KeyAgreement.PrivateKey](p256/keyagreement/privatekey.md)
- [P384.KeyAgreement.PrivateKey](p384/keyagreement/privatekey.md)
- [P521.KeyAgreement.PrivateKey](p521/keyagreement/privatekey.md)
- [SecureEnclave.P256.KeyAgreement.PrivateKey](secureenclave/p256/keyagreement/privatekey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/diffiehellmankeyagreement)*