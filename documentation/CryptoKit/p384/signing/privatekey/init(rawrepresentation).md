# init(rawRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init  
**Role**: Initializer

Creates a P-384 private key for signing from a collection of bytes.

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

- `rawRepresentation`: A raw representation of the key as a collection of contiguous bytes.

## See Also

### Creating a private key
- [init(compactRepresentable: Bool)](./init%28compactrepresentable%29.md)
  Creates a random P-384 private key for signing.
- [init<Bytes>(derRepresentation: Bytes) throws](./init%28derrepresentation%29.md)
  Creates a P-384 private key for signing from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](./init%28pemrepresentation%29.md)
  Creates a P-384 private key for signing from a Privacy-Enhanced Mail PEM) representation.
- [init<Bytes>(x963Representation: Bytes) throws](./init%28x963representation%29.md)
  Creates a P-384 private key for signing from an ANSI x9.63 representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p384/signing/privatekey/init(rawrepresentation:))*