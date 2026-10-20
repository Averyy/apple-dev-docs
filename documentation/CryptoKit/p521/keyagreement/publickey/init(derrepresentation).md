# init(derRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init  
**Role**: Initializer

Creates a P-521 public key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.

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

### Creating a public key
- [init<D>(rawRepresentation: D) throws](./init%28rawrepresentation%29.md)
  Creates a P-521 public key for key agreement from a collection of bytes.
- [init<Bytes>(compactRepresentation: Bytes) throws](./init%28compactrepresentation%29.md)
  Creates a P-521 public key for key agreement from a compact representation of the key.
- [init(pemRepresentation: String) throws](./init%28pemrepresentation%29.md)
  Creates a P-521 public key for key agreement from a Privacy-Enhanced Mail (PEM) representation.
- [init<Bytes>(x963Representation: Bytes) throws](./init%28x963representation%29.md)
  Creates a P-521 public key for key agreement from an ANSI x9.63 representation.
- [init<Bytes>(compressedRepresentation: Bytes) throws](./init%28compressedrepresentation%29.md)
  Creates a P-521 public key for key agreement from a compressed representation of the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/keyagreement/publickey/init(derrepresentation:))*