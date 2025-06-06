# init(rawRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a P-384 private key for key agreement from a collection of bytes.

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
init<Bytes>(rawRepresentation: Bytes) throws where Bytes : ContiguousBytes
```

## Parameters

- `rawRepresentation`: A raw representation of the key as a collection of   contiguous bytes.

## See Also

- [init(compactRepresentable: Bool)](p384/keyagreement/privatekey/init(compactrepresentable:).md)
  Creates a random P-384 private key for key agreement.
- [init<Bytes>(derRepresentation: Bytes) throws](p384/keyagreement/privatekey/init(derrepresentation:).md)
  Creates a P-384 private key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](p384/keyagreement/privatekey/init(pemrepresentation:).md)
  Creates a P-384 private key for key agreement from a Privacy-Enhanced Mail PEM) representation.
- [init<Bytes>(x963Representation: Bytes) throws](p384/keyagreement/privatekey/init(x963representation:).md)
  Creates a P-384 private key for key agreement from an ANSI x9.63 representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p384/keyagreement/privatekey/init(rawrepresentation:))*