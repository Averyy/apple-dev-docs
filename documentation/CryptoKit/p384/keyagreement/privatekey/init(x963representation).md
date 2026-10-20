# init(x963Representation:)

**Framework**: Apple CryptoKit  
**Kind**: init  
**Role**: Initializer

Creates a P-384 private key for key agreement from an ANSI x9.63 representation.

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

### Creating a private key
- [init<Bytes>(rawRepresentation: Bytes) throws](./init%28rawrepresentation%29.md)
  Creates a P-384 private key for key agreement from a collection of bytes.
- [init(compactRepresentable: Bool)](./init%28compactrepresentable%29.md)
  Creates a random P-384 private key for key agreement.
- [init<Bytes>(derRepresentation: Bytes) throws](./init%28derrepresentation%29.md)
  Creates a P-384 private key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](./init%28pemrepresentation%29.md)
  Creates a P-384 private key for key agreement from a Privacy-Enhanced Mail PEM) representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p384/keyagreement/privatekey/init(x963representation:))*