# init(compactRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a P-384 public key for signing from a compact representation of the key.

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
init<Bytes>(compactRepresentation: Bytes) throws where Bytes : ContiguousBytes
```

## Parameters

- `compactRepresentation`: A compact representation of the key   as a collection of contiguous bytes.

## See Also

- [init<D>(rawRepresentation: D) throws](p384/signing/publickey/init(rawrepresentation:).md)
  Creates a P-384 public key for signing from a collection of bytes.
- [init<Bytes>(compressedRepresentation: Bytes) throws](p384/signing/publickey/init(compressedrepresentation:).md)
  Creates a P-384 public key for signing from a compressed representation of the key.
- [init<Bytes>(derRepresentation: Bytes) throws](p384/signing/publickey/init(derrepresentation:).md)
  Creates a P-384 public key for signing from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](p384/signing/publickey/init(pemrepresentation:).md)
  Creates a P-384 public key for signing from a Privacy-Enhanced Mail (PEM) representation.
- [init<Bytes>(x963Representation: Bytes) throws](p384/signing/publickey/init(x963representation:).md)
  Creates a P-384 public key for signing from an ANSI x9.63 representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p384/signing/publickey/init(compactrepresentation:))*