# init(rawRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init  
**Role**: Initializer

Creates a P-521 public key for key agreement from a collection of bytes.

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
init<D>(rawRepresentation: D) throws where D : ContiguousBytes
```

## Parameters

- `rawRepresentation`: A raw representation of the key as a collection of contiguous bytes.

## See Also

### Creating a public key
- [init<Bytes>(compactRepresentation: Bytes) throws](./init%28compactrepresentation%29.md)
  Creates a P-521 public key for key agreement from a compact representation of the key.
- [init<Bytes>(derRepresentation: Bytes) throws](./init%28derrepresentation%29.md)
  Creates a P-521 public key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](./init%28pemrepresentation%29.md)
  Creates a P-521 public key for key agreement from a Privacy-Enhanced Mail (PEM) representation.
- [init<Bytes>(x963Representation: Bytes) throws](./init%28x963representation%29.md)
  Creates a P-521 public key for key agreement from an ANSI x9.63 representation.
- [init<Bytes>(compressedRepresentation: Bytes) throws](./init%28compressedrepresentation%29.md)
  Creates a P-521 public key for key agreement from a compressed representation of the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/keyagreement/publickey/init(rawrepresentation:))*