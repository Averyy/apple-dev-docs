# P384.Signing.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

A P-384 private key used to create cryptographic signatures.

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
- [init<Bytes>(rawRepresentation: Bytes) throws](./privatekey/init%28rawrepresentation%29.md)
  Creates a P-384 private key for signing from a collection of bytes.
- [init(compactRepresentable: Bool)](./privatekey/init%28compactrepresentable%29.md)
  Creates a random P-384 private key for signing.
- [init<Bytes>(derRepresentation: Bytes) throws](./privatekey/init%28derrepresentation%29.md)
  Creates a P-384 private key for signing from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](./privatekey/init%28pemrepresentation%29.md)
  Creates a P-384 private key for signing from a Privacy-Enhanced Mail PEM) representation.
- [init<Bytes>(x963Representation: Bytes) throws](./privatekey/init%28x963representation%29.md)
  Creates a P-384 private key for signing from an ANSI x9.63 representation.
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
- [var publicKey: P384.Signing.PublicKey](./privatekey/publickey.md)
  The corresponding public key.
### Creating a signature
- [func signature<D>(for: D) throws -> P384.Signing.ECDSASignature](./privatekey/signature%28for%29-8nncg.md)
  Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the data you provide over the P-384 elliptic curve, using SHA-384 as the hash function.
- [func signature<D>(for: D) throws -> P384.Signing.ECDSASignature](./privatekey/signature%28for%29-wrsj.md)
  Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the digest you provide over the P-384 elliptic curve.
- [P384.Signing.ECDSASignature](./ecdsasignature.md)
  A P-384 elliptic curve digital signature algorithm (ECDSA) signature.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Using keys
- [P384.Signing.PublicKey](./publickey.md)
  A P-384 public key used to verify cryptographic signatures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p384/signing/privatekey)*