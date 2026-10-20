# P521.Signing.ECDSASignature

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

A P-521 elliptic curve digital signature algorithm (ECDSA) signature.

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
struct ECDSASignature
```

## Topics

### Creating a signature
- [init<D>(derRepresentation: D) throws](./ecdsasignature/init%28derrepresentation%29.md)
  Creates a P-521 digital signature from a Distinguished Encoding Rules (DER) encoded representation.
- [init<D>(rawRepresentation: D) throws](./ecdsasignature/init%28rawrepresentation%29.md)
  Creates a P-521 digital signature from a raw representation.
### Representing the signature
- [var derRepresentation: Data](./ecdsasignature/derrepresentation.md)
  A Distinguished Encoding Rules (DER) encoded representation of a P-521 digital signature.
- [var rawRepresentation: Data](./ecdsasignature/rawrepresentation.md)
  A raw data representation of a P-521 digital signature.

## Relationships

### Conforms To
- [ContiguousBytes](../../../Foundation/contiguousbytes.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Creating a signature
- [func signature<D>(for: D) throws -> P521.Signing.ECDSASignature](./privatekey/signature%28for%29-34g01.md)
  Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the data you provide over the P-521 elliptic curve, using SHA-512 as the hash function.
- [func signature<D>(for: D) throws -> P521.Signing.ECDSASignature](./privatekey/signature%28for%29-7rxva.md)
  Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the digest you provide over the P-521 elliptic curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/signing/ecdsasignature)*