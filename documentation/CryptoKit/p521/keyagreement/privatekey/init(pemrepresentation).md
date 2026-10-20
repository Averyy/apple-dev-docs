# init(pemRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init  
**Role**: Initializer

Creates a P-521 private key for key agreement from a Privacy-Enhanced Mail PEM) representation.

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

### Creating a private key
- [init(compactRepresentable: Bool)](./init%28compactrepresentable%29.md)
  Creates a random P-521 private key for key agreement.
- [init<Bytes>(rawRepresentation: Bytes) throws](./init%28rawrepresentation%29.md)
  Creates a P-521 private key for key agreement from a collection of bytes.
- [init<Bytes>(derRepresentation: Bytes) throws](./init%28derrepresentation%29.md)
  Creates a P-521 private key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init<Bytes>(x963Representation: Bytes) throws](./init%28x963representation%29.md)
  Creates a P-521 private key for key agreement from an ANSI x9.63 representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/keyagreement/privatekey/init(pemrepresentation:))*