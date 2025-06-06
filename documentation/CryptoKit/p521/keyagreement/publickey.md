# P521.KeyAgreement.PublicKey

**Framework**: Apple CryptoKit  
**Kind**: struct

A P-521 public key used for key agreement.

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
- [init<D>(rawRepresentation: D) throws](p521/keyagreement/publickey/init(rawrepresentation:).md)
  Creates a P-521 public key for key agreement from a collection of bytes.
- [init<Bytes>(compactRepresentation: Bytes) throws](p521/keyagreement/publickey/init(compactrepresentation:).md)
  Creates a P-521 public key for key agreement from a compact representation of the key.
- [init<Bytes>(derRepresentation: Bytes) throws](p521/keyagreement/publickey/init(derrepresentation:).md)
  Creates a P-521 public key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](p521/keyagreement/publickey/init(pemrepresentation:).md)
  Creates a P-521 public key for key agreement from a Privacy-Enhanced Mail (PEM) representation.
- [init<Bytes>(x963Representation: Bytes) throws](p521/keyagreement/publickey/init(x963representation:).md)
  Creates a P-521 public key for key agreement from an ANSI x9.63 representation.
- [init<Bytes>(compressedRepresentation: Bytes) throws](p521/keyagreement/publickey/init(compressedrepresentation:).md)
  Creates a P-521 public key for key agreement from a compressed representation of the key.
### Representing the key
- [var rawRepresentation: Data](p521/keyagreement/publickey/rawrepresentation.md)
  A full representation of the public key.
- [var compactRepresentation: Data?](p521/keyagreement/publickey/compactrepresentation.md)
  A compact representation of the public key.
- [var derRepresentation: Data](p521/keyagreement/publickey/derrepresentation.md)
  A Distinguished Encoding Rules (DER) encoded representation of the public key.
- [var pemRepresentation: String](p521/keyagreement/publickey/pemrepresentation.md)
  A Privacy-Enhanced Mail (PEM) representation of the public key.
- [var x963Representation: Data](p521/keyagreement/publickey/x963representation.md)
  An ANSI x9.63 representation of the public key.
- [var compressedRepresentation: Data](p521/keyagreement/publickey/compressedrepresentation.md)
  A compressed representation of the public key.
### Type Aliases
- [P521.KeyAgreement.PublicKey.HPKEEphemeralPrivateKey](p521/keyagreement/publickey/hpkeephemeralprivatekey.md)
  The type of the ephemeral private key associated with this public key.
### Default Implementations
- [HPKEDiffieHellmanPublicKey Implementations](p521/keyagreement/publickey/hpkediffiehellmanpublickey-implementations.md)
- [HPKEPublicKeySerialization Implementations](p521/keyagreement/publickey/hpkepublickeyserialization-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [HPKEDiffieHellmanPublicKey](hpkediffiehellmanpublickey.md)
- [HPKEPublicKeySerialization](hpkepublickeyserialization.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [P521.KeyAgreement.PrivateKey](p521/keyagreement/privatekey.md)
  A P-521 private key used for key agreement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/keyagreement/publickey)*