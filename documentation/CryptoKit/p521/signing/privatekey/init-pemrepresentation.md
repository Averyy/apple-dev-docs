# init(pemRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a P-521 private key for signing from a Privacy-Enhanced Mail PEM) representation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(pemRepresentation: String) throws
```

## Parameters

- `pemRepresentation`: A PEM representation of the key.

## See Also

- [init<Bytes>(rawRepresentation: Bytes) throws](p521/signing/privatekey/init(rawrepresentation:).md)
  Creates a P-521 private key for signing from a collection of bytes.
- [init(compactRepresentable: Bool)](p521/signing/privatekey/init(compactrepresentable:).md)
  Creates a random P-521 private key for signing.
- [init<Bytes>(derRepresentation: Bytes) throws](p521/signing/privatekey/init(derrepresentation:).md)
  Creates a P-521 private key for signing from a Distinguished Encoding Rules (DER) encoded representation.
- [init<Bytes>(x963Representation: Bytes) throws](p521/signing/privatekey/init(x963representation:).md)
  Creates a P-521 private key for signing from an ANSI x9.63 representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/signing/privatekey/init(pemrepresentation:))*