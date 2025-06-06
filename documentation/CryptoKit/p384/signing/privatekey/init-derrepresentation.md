# init(derRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a P-384 private key for signing from a Distinguished Encoding Rules (DER) encoded representation.

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
init<Bytes>(derRepresentation: Bytes) throws where Bytes : RandomAccessCollection, Bytes.Element == UInt8
```

## Parameters

- `derRepresentation`: A DER-encoded representation of the key.

## See Also

- [init<Bytes>(rawRepresentation: Bytes) throws](p384/signing/privatekey/init(rawrepresentation:).md)
  Creates a P-384 private key for signing from a collection of bytes.
- [init(compactRepresentable: Bool)](p384/signing/privatekey/init(compactrepresentable:).md)
  Creates a random P-384 private key for signing.
- [init(pemRepresentation: String) throws](p384/signing/privatekey/init(pemrepresentation:).md)
  Creates a P-384 private key for signing from a Privacy-Enhanced Mail PEM) representation.
- [init<Bytes>(x963Representation: Bytes) throws](p384/signing/privatekey/init(x963representation:).md)
  Creates a P-384 private key for signing from an ANSI x9.63 representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p384/signing/privatekey/init(derrepresentation:))*