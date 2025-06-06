# init(compressedRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a P-256 public key for key agreement from a compressed representation of the key.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init<Bytes>(compressedRepresentation: Bytes) throws where Bytes : ContiguousBytes
```

## Parameters

- `compressedRepresentation`: A compressed representation of the key as a collection   of contiguous bytes.

## See Also

- [init<D>(rawRepresentation: D) throws](p256/keyagreement/publickey/init(rawrepresentation:).md)
  Creates a P-256 public key for key agreement from a collection of bytes.
- [init<Bytes>(compactRepresentation: Bytes) throws](p256/keyagreement/publickey/init(compactrepresentation:).md)
  Creates a P-256 public key for key agreement from a compact representation of the key.
- [init<Bytes>(derRepresentation: Bytes) throws](p256/keyagreement/publickey/init(derrepresentation:).md)
  Creates a P-256 public key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](p256/keyagreement/publickey/init(pemrepresentation:).md)
  Creates a P-256 public key for key agreement from a Privacy-Enhanced Mail (PEM) representation.
- [init<Bytes>(x963Representation: Bytes) throws](p256/keyagreement/publickey/init(x963representation:).md)
  Creates a P-256 public key for key agreement from an ANSI x9.63 representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p256/keyagreement/publickey/init(compressedrepresentation:))*