# P256.Signing.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct

A P-256 private key used to create cryptographic signatures.

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
- [init<Bytes>(rawRepresentation: Bytes) throws](p256/signing/privatekey/init(rawrepresentation:).md)
  Creates a P-256 private key for signing from a collection of bytes.
- [init(compactRepresentable: Bool)](p256/signing/privatekey/init(compactrepresentable:).md)
  Creates a random P-256 private key for signing.
- [init<Bytes>(derRepresentation: Bytes) throws](p256/signing/privatekey/init(derrepresentation:).md)
  Creates a P-256 private key for signing from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](p256/signing/privatekey/init(pemrepresentation:).md)
  Creates a P-256 private key for signing from a Privacy-Enhanced Mail PEM) representation.
- [init<Bytes>(x963Representation: Bytes) throws](p256/signing/privatekey/init(x963representation:).md)
  Creates a P-256 private key for signing from an ANSI x9.63 representation.
### Representing the key
- [var rawRepresentation: Data](p256/signing/privatekey/rawrepresentation.md)
  A data representation of the private key.
- [var derRepresentation: Data](p256/signing/privatekey/derrepresentation.md)
  A Distinguished Encoding Rules (DER) encoded representation of the private key.
- [var pemRepresentation: String](p256/signing/privatekey/pemrepresentation.md)
  A Privacy-Enhanced Mail (PEM) representation of the private key.
- [var x963Representation: Data](p256/signing/privatekey/x963representation.md)
  An ANSI x9.63 representation of the private key.
### Finding the public key
- [var publicKey: P256.Signing.PublicKey](p256/signing/privatekey/publickey.md)
  The corresponding public key.
### Creating a signature
- [func signature<D>(for: D) throws -> P256.Signing.ECDSASignature](p256/signing/privatekey/signature(for:)-5h94p.md)
  Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the data you provide over the P-256 elliptic curve, using SHA-256 as the hash function.
- [func signature<D>(for: D) throws -> P256.Signing.ECDSASignature](p256/signing/privatekey/signature(for:)-1iyzc.md)
  Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the digest you provide over the P-256 elliptic curve.
- [P256.Signing.ECDSASignature](p256/signing/ecdsasignature.md)
  A P-256 elliptic curve digital signature algorithm (ECDSA) signature.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [P256.Signing.PublicKey](p256/signing/publickey.md)
  A P-256 public key used to verify cryptographic signatures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p256/signing/privatekey)*