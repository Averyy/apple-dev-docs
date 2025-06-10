# HPKEPublicKeySerialization

**Framework**: Apple CryptoKit  
**Kind**: protocol

A type that [`HPKE`](hpke.md) uses to encode the public key.

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
protocol HPKEPublicKeySerialization : Sendable
```

## Topics

### Initializers
- [init<D>(D, kem: HPKE.KEM) throws](hpkepublickeyserialization/init(_:kem:).md)
  Creates a public key from an encoded representation.
### Instance Methods
- [func hpkeRepresentation(kem: HPKE.KEM) throws -> Data](hpkepublickeyserialization/hpkerepresentation(kem:).md)
  Creates an encoded representation of the public key.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [HPKEDiffieHellmanPublicKey](hpkediffiehellmanpublickey.md)
- [HPKEKEMPublicKey](hpkekempublickey.md)
### Conforming Types
- [Curve25519.KeyAgreement.PublicKey](curve25519/keyagreement/publickey.md)
- [P256.KeyAgreement.PublicKey](p256/keyagreement/publickey.md)
- [P384.KeyAgreement.PublicKey](p384/keyagreement/publickey.md)
- [P521.KeyAgreement.PublicKey](p521/keyagreement/publickey.md)
- [XWingMLKEM768X25519.PublicKey](xwingmlkem768x25519/publickey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpkepublickeyserialization)*