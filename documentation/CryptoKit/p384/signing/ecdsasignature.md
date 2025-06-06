# P384.Signing.ECDSASignature

**Framework**: Apple CryptoKit  
**Kind**: struct

A P-384 elliptic curve digital signature algorithm (ECDSA) signature.

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
- [init<D>(derRepresentation: D) throws](p384/signing/ecdsasignature/init(derrepresentation:).md)
  Creates a P-384 digital signature from a Distinguished Encoding Rules (DER) encoded representation.
- [init<D>(rawRepresentation: D) throws](p384/signing/ecdsasignature/init(rawrepresentation:).md)
  Creates a P-384 digital signature from a raw representation.
### Representing the signature
- [var derRepresentation: Data](p384/signing/ecdsasignature/derrepresentation.md)
  A Distinguished Encoding Rules (DER) encoded representation of a P-384 digital signature.
- [var rawRepresentation: Data](p384/signing/ecdsasignature/rawrepresentation.md)
  A raw data representation of a P-384 digital signature.

## Relationships

### Conforms To
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func signature<D>(for: D) throws -> P384.Signing.ECDSASignature](p384/signing/privatekey/signature(for:)-8nncg.md)
  Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the data you provide over the P-384 elliptic curve, using SHA-384 as the hash function.
- [func signature<D>(for: D) throws -> P384.Signing.ECDSASignature](p384/signing/privatekey/signature(for:)-wrsj.md)
  Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the digest you provide over the P-384 elliptic curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p384/signing/ecdsasignature)*