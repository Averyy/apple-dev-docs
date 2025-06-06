# init(x963Representation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a P-384 public key for key agreement from an ANSI x9.63 representation.

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
init<Bytes>(x963Representation: Bytes) throws where Bytes : ContiguousBytes
```

## Parameters

- `x963Representation`: An ANSI x9.63 representation of the key.

## See Also

- [init<D>(rawRepresentation: D) throws](p384/keyagreement/publickey/init(rawrepresentation:).md)
  Creates a P-384 public key for key agreement from a collection of bytes.
- [init<Bytes>(compactRepresentation: Bytes) throws](p384/keyagreement/publickey/init(compactrepresentation:).md)
  Creates a P-384 public key for key agreement from a compact representation of the key.
- [init<Bytes>(derRepresentation: Bytes) throws](p384/keyagreement/publickey/init(derrepresentation:).md)
  Creates a P-384 public key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](p384/keyagreement/publickey/init(pemrepresentation:).md)
  Creates a P-384 public key for key agreement from a Privacy-Enhanced Mail (PEM) representation.
- [init<Bytes>(compressedRepresentation: Bytes) throws](p384/keyagreement/publickey/init(compressedrepresentation:).md)
  Creates a P-384 public key for key agreement from a compressed representation of the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p384/keyagreement/publickey/init(x963representation:))*