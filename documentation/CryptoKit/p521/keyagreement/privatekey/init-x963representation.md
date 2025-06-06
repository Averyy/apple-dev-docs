# init(x963Representation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a P-521 private key for key agreement from an ANSI x9.63 representation.

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

- [init(compactRepresentable: Bool)](p521/keyagreement/privatekey/init(compactrepresentable:).md)
  Creates a random P-521 private key for key agreement.
- [init<Bytes>(rawRepresentation: Bytes) throws](p521/keyagreement/privatekey/init(rawrepresentation:).md)
  Creates a P-521 private key for key agreement from a collection of bytes.
- [init<Bytes>(derRepresentation: Bytes) throws](p521/keyagreement/privatekey/init(derrepresentation:).md)
  Creates a P-521 private key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](p521/keyagreement/privatekey/init(pemrepresentation:).md)
  Creates a P-521 private key for key agreement from a Privacy-Enhanced Mail PEM) representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/keyagreement/privatekey/init(x963representation:))*