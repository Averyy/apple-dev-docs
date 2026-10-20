# init(compactRepresentable:)

**Framework**: Apple CryptoKit  
**Kind**: init  
**Role**: Initializer

Creates a random P-384 private key for key agreement.

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
init(compactRepresentable: Bool = true)
```

#### Discussion

Keys that use a compact point encoding enable shorter public keys, but aren’t compliant with FIPS certification. If your app requires FIPS certification, create a key with [`init(rawRepresentation:)`](./init%28rawrepresentation%29.md).

## Parameters

- `compactRepresentable`: A Boolean value that indicates whether CryptoKit creates the key with the structure to enable compact point encoding.

## See Also

### Creating a private key
- [init<Bytes>(rawRepresentation: Bytes) throws](./init%28rawrepresentation%29.md)
  Creates a P-384 private key for key agreement from a collection of bytes.
- [init<Bytes>(derRepresentation: Bytes) throws](./init%28derrepresentation%29.md)
  Creates a P-384 private key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](./init%28pemrepresentation%29.md)
  Creates a P-384 private key for key agreement from a Privacy-Enhanced Mail PEM) representation.
- [init<Bytes>(x963Representation: Bytes) throws](./init%28x963representation%29.md)
  Creates a P-384 private key for key agreement from an ANSI x9.63 representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p384/keyagreement/privatekey/init(compactrepresentable:))*