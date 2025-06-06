# Curve25519.KeyAgreement.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct

A Curve25519 private key used for key agreement.

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
struct PrivateKey
```

## Topics

### Creating a private key
- [init()](curve25519/keyagreement/privatekey/init.md)
  Creates a random Curve25519 private key for key agreement.
- [init<D>(rawRepresentation: D) throws](curve25519/keyagreement/privatekey/init(rawrepresentation:).md)
  Creates a Curve25519 private key for key agreement from a collection of bytes.
### Reporting the private key
- [var rawRepresentation: Data](curve25519/keyagreement/privatekey/rawrepresentation.md)
  The raw representation of the key as a collection of contiguous bytes.
### Finding the public key
- [var publicKey: Curve25519.KeyAgreement.PublicKey](curve25519/keyagreement/privatekey/publickey.md)
  The corresponding public key.
### Creating a shared secret
- [func sharedSecretFromKeyAgreement(with: Curve25519.KeyAgreement.PublicKey) throws -> SharedSecret](curve25519/keyagreement/privatekey/sharedsecretfromkeyagreement(with:).md)
  Computes a shared secret with the provided public key from another party.
- [struct SharedSecret](sharedsecret.md)
  A key agreement result from which you can derive a symmetric cryptographic key.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [DiffieHellmanKeyAgreement](diffiehellmankeyagreement.md)
- [HPKEDiffieHellmanPrivateKey](hpkediffiehellmanprivatekey.md)
- [HPKEDiffieHellmanPrivateKeyGeneration](hpkediffiehellmanprivatekeygeneration.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Curve25519.KeyAgreement.PublicKey](curve25519/keyagreement/publickey.md)
  A Curve25519 public key used for key agreement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/curve25519/keyagreement/privatekey)*