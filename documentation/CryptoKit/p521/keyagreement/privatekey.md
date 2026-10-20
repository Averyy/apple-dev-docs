# P521.KeyAgreement.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

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
- [init(compactRepresentable: Bool)](./privatekey/init%28compactrepresentable%29.md)
  Creates a random P-521 private key for key agreement.
- [init<Bytes>(rawRepresentation: Bytes) throws](./privatekey/init%28rawrepresentation%29.md)
  Creates a P-521 private key for key agreement from a collection of bytes.
- [init<Bytes>(derRepresentation: Bytes) throws](./privatekey/init%28derrepresentation%29.md)
  Creates a P-521 private key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](./privatekey/init%28pemrepresentation%29.md)
  Creates a P-521 private key for key agreement from a Privacy-Enhanced Mail PEM) representation.
- [init<Bytes>(x963Representation: Bytes) throws](./privatekey/init%28x963representation%29.md)
  Creates a P-521 private key for key agreement from an ANSI x9.63 representation.
### Representing the key
- [var rawRepresentation: Data](./privatekey/rawrepresentation.md)
  A data representation of the private key.
- [var derRepresentation: Data](./privatekey/derrepresentation.md)
  A Distinguished Encoding Rules (DER) encoded representation of the private key.
- [var pemRepresentation: String](./privatekey/pemrepresentation.md)
  A Privacy-Enhanced Mail (PEM) representation of the private key.
- [var x963Representation: Data](./privatekey/x963representation.md)
  An ANSI x9.63 representation of the private key.
### Finding the public key
- [var publicKey: P521.KeyAgreement.PublicKey](./privatekey/publickey.md)
  The corresponding public key.
### Creating a shared secret
- [func sharedSecretFromKeyAgreement(with: P521.KeyAgreement.PublicKey) throws -> SharedSecret](./privatekey/sharedsecretfromkeyagreement%28with%29.md)
  Computes a shared secret with the provided public key from another party.
- [struct SharedSecret](../../sharedsecret.md)
  A key agreement result from which you can derive a symmetric cryptographic key.
### Default Implementations
- [DiffieHellmanKeyAgreement Implementations](./privatekey/diffiehellmankeyagreement-implementations.md)
- [HPKEDiffieHellmanPrivateKeyGeneration Implementations](./privatekey/hpkediffiehellmanprivatekeygeneration-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [DiffieHellmanKeyAgreement](../../diffiehellmankeyagreement.md)
- [Escapable](../../../Swift/escapable.md)
- [HPKEDiffieHellmanPrivateKey](../../hpkediffiehellmanprivatekey.md)
- [HPKEDiffieHellmanPrivateKeyGeneration](../../hpkediffiehellmanprivatekeygeneration.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Using keys
- [P521.KeyAgreement.PublicKey](./publickey.md)
  A P-521 public key used for key agreement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/keyagreement/privatekey)*