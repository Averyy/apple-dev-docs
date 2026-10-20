# P256.KeyAgreement.PublicKey

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

A P-256 public key used for key agreement.

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
- [init<D>(rawRepresentation: D) throws](./publickey/init%28rawrepresentation%29.md)
  Creates a P-256 public key for key agreement from a collection of bytes.
- [init<Bytes>(compactRepresentation: Bytes) throws](./publickey/init%28compactrepresentation%29.md)
  Creates a P-256 public key for key agreement from a compact representation of the key.
- [init<Bytes>(derRepresentation: Bytes) throws](./publickey/init%28derrepresentation%29.md)
  Creates a P-256 public key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](./publickey/init%28pemrepresentation%29.md)
  Creates a P-256 public key for key agreement from a Privacy-Enhanced Mail (PEM) representation.
- [init<Bytes>(x963Representation: Bytes) throws](./publickey/init%28x963representation%29.md)
  Creates a P-256 public key for key agreement from an ANSI x9.63 representation.
- [init<Bytes>(compressedRepresentation: Bytes) throws](./publickey/init%28compressedrepresentation%29.md)
  Creates a P-256 public key for key agreement from a compressed representation of the key.
### Representing the key
- [var rawRepresentation: Data](./publickey/rawrepresentation.md)
  A full representation of the public key.
- [var compactRepresentation: Data?](./publickey/compactrepresentation.md)
  A compact representation of the public key.
- [var derRepresentation: Data](./publickey/derrepresentation.md)
  A Distinguished Encoding Rules (DER) encoded representation of the public key.
- [var pemRepresentation: String](./publickey/pemrepresentation.md)
  A Privacy-Enhanced Mail (PEM) representation of the public key.
- [var x963Representation: Data](./publickey/x963representation.md)
  An ANSI x9.63 representation of the public key.
- [var compressedRepresentation: Data](./publickey/compressedrepresentation.md)
  A compressed representation of the public key.
### Type Aliases
- [P256.KeyAgreement.PublicKey.HPKEEphemeralPrivateKey](./publickey/hpkeephemeralprivatekey.md)
  The type of the ephemeral private key associated with this public key.
### Default Implementations
- [HPKEDiffieHellmanPublicKey Implementations](./publickey/hpkediffiehellmanpublickey-implementations.md)
- [HPKEPublicKeySerialization Implementations](./publickey/hpkepublickeyserialization-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [Escapable](../../../Swift/escapable.md)
- [HPKEDiffieHellmanPublicKey](../../hpkediffiehellmanpublickey.md)
- [HPKEPublicKeySerialization](../../hpkepublickeyserialization.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Using keys
- [P256.KeyAgreement.PrivateKey](./privatekey.md)
  A P-256 private key used for key agreement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p256/keyagreement/publickey)*