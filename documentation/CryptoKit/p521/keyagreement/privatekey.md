# P521.KeyAgreement.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct

A P-521 private key used for key agreement.

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
- [init(compactRepresentable: Bool)](p521/keyagreement/privatekey/init(compactrepresentable:).md)
  Creates a random P-521 private key for key agreement.
- [init<Bytes>(rawRepresentation: Bytes) throws](p521/keyagreement/privatekey/init(rawrepresentation:).md)
  Creates a P-521 private key for key agreement from a collection of bytes.
- [init<Bytes>(derRepresentation: Bytes) throws](p521/keyagreement/privatekey/init(derrepresentation:).md)
  Creates a P-521 private key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](p521/keyagreement/privatekey/init(pemrepresentation:).md)
  Creates a P-521 private key for key agreement from a Privacy-Enhanced Mail PEM) representation.
- [init<Bytes>(x963Representation: Bytes) throws](p521/keyagreement/privatekey/init(x963representation:).md)
  Creates a P-521 private key for key agreement from an ANSI x9.63 representation.
### Representing the key
- [var rawRepresentation: Data](p521/keyagreement/privatekey/rawrepresentation.md)
  A data representation of the private key.
- [var derRepresentation: Data](p521/keyagreement/privatekey/derrepresentation.md)
  A Distinguished Encoding Rules (DER) encoded representation of the private key.
- [var pemRepresentation: String](p521/keyagreement/privatekey/pemrepresentation.md)
  A Privacy-Enhanced Mail (PEM) representation of the private key.
- [var x963Representation: Data](p521/keyagreement/privatekey/x963representation.md)
  An ANSI x9.63 representation of the private key.
### Finding the public key
- [var publicKey: P521.KeyAgreement.PublicKey](p521/keyagreement/privatekey/publickey.md)
  The corresponding public key.
### Creating a shared secret
- [func sharedSecretFromKeyAgreement(with: P521.KeyAgreement.PublicKey) throws -> SharedSecret](p521/keyagreement/privatekey/sharedsecretfromkeyagreement(with:).md)
  Computes a shared secret with the provided public key from another party.
- [struct SharedSecret](sharedsecret.md)
  A key agreement result from which you can derive a symmetric cryptographic key.
### Default Implementations
- [DiffieHellmanKeyAgreement Implementations](p521/keyagreement/privatekey/diffiehellmankeyagreement-implementations.md)
- [HPKEDiffieHellmanPrivateKeyGeneration Implementations](p521/keyagreement/privatekey/hpkediffiehellmanprivatekeygeneration-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [DiffieHellmanKeyAgreement](diffiehellmankeyagreement.md)
- [HPKEDiffieHellmanPrivateKey](hpkediffiehellmanprivatekey.md)
- [HPKEDiffieHellmanPrivateKeyGeneration](hpkediffiehellmanprivatekeygeneration.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [P521.KeyAgreement.PublicKey](p521/keyagreement/publickey.md)
  A P-521 public key used for key agreement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/keyagreement/privatekey)*