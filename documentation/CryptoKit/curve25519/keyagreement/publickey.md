# Curve25519.KeyAgreement.PublicKey

**Framework**: Apple CryptoKit  
**Kind**: struct

A Curve25519 public key used for key agreement.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct PublicKey
```

## Topics

### Creating a public key
- [init<D>(rawRepresentation: D) throws](curve25519/keyagreement/publickey/init(rawrepresentation:).md)
  Creates a Curve25519 public key for key agreement from a collection of bytes.
### Representing the key
- [var rawRepresentation: Data](curve25519/keyagreement/publickey/rawrepresentation.md)
  A representation of the Curve25519 public key as a collection of bytes.
### Type Aliases
- [Curve25519.KeyAgreement.PublicKey.HPKEEphemeralPrivateKey](curve25519/keyagreement/publickey/hpkeephemeralprivatekey.md)
  The type of the ephemeral private key associated with this public key.
### Default Implementations
- [HPKEDiffieHellmanPublicKey Implementations](curve25519/keyagreement/publickey/hpkediffiehellmanpublickey-implementations.md)
- [HPKEPublicKeySerialization Implementations](curve25519/keyagreement/publickey/hpkepublickeyserialization-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [HPKEDiffieHellmanPublicKey](hpkediffiehellmanpublickey.md)
- [HPKEPublicKeySerialization](hpkepublickeyserialization.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Curve25519.KeyAgreement.PrivateKey](curve25519/keyagreement/privatekey.md)
  A Curve25519 private key used for key agreement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/curve25519/keyagreement/publickey)*