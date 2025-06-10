# P256.Signing.PublicKey

**Framework**: Apple CryptoKit  
**Kind**: struct

A P-256 public key used to verify cryptographic signatures.

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

### Creating a key
- [init<D>(rawRepresentation: D) throws](p256/signing/publickey/init(rawrepresentation:).md)
  Creates a P-256 public key for signing from a collection of bytes.
- [init<Bytes>(compactRepresentation: Bytes) throws](p256/signing/publickey/init(compactrepresentation:).md)
  Creates a P-256 public key for signing from a compact representation of the key.
- [init<Bytes>(compressedRepresentation: Bytes) throws](p256/signing/publickey/init(compressedrepresentation:).md)
  Creates a P-256 public key for signing from a compressed representation of the key.
- [init<Bytes>(derRepresentation: Bytes) throws](p256/signing/publickey/init(derrepresentation:).md)
  Creates a P-256 public key for signing from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](p256/signing/publickey/init(pemrepresentation:).md)
  Creates a P-256 public key for signing from a Privacy-Enhanced Mail (PEM) representation.
- [init<Bytes>(x963Representation: Bytes) throws](p256/signing/publickey/init(x963representation:).md)
  Creates a P-256 public key for signing from an ANSI x9.63 representation.
### Representing the key
- [var rawRepresentation: Data](p256/signing/publickey/rawrepresentation.md)
  A full representation of the public key.
- [var compactRepresentation: Data?](p256/signing/publickey/compactrepresentation.md)
  A compact representation of the public key.
- [var compressedRepresentation: Data](p256/signing/publickey/compressedrepresentation.md)
  A compressed representation of the public key.
- [var derRepresentation: Data](p256/signing/publickey/derrepresentation.md)
  A Distinguished Encoding Rules (DER) encoded representation of the public key.
- [var pemRepresentation: String](p256/signing/publickey/pemrepresentation.md)
  A Privacy-Enhanced Mail (PEM) representation of the public key.
- [var x963Representation: Data](p256/signing/publickey/x963representation.md)
  An ANSI x9.63 representation of the public key.
### Verifying a signature
- [func isValidSignature<D>(P256.Signing.ECDSASignature, for: D) -> Bool](p256/signing/publickey/isvalidsignature(_:for:)-3da2m.md)
  Verifies an elliptic curve digital signature algorithm (ECDSA) signature on a block of data over the P-256 elliptic curve.
- [func isValidSignature<D>(P256.Signing.ECDSASignature, for: D) -> Bool](p256/signing/publickey/isvalidsignature(_:for:)-2rsb5.md)
  Verifies an elliptic curve digital signature algorithm (ECDSA) signature on a digest over the P-256 elliptic curve.
- [P256.Signing.ECDSASignature](p256/signing/ecdsasignature.md)
  A P-256 elliptic curve digital signature algorithm (ECDSA) signature.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [P256.Signing.PrivateKey](p256/signing/privatekey.md)
  A P-256 private key used to create cryptographic signatures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p256/signing/publickey)*