# init(compactRepresentable:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a random P-521 private key for signing.

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

Keys that use a compact point encoding enable shorter public keys, but aren’t compliant with FIPS certification. If your app requires FIPS certification, create a key with [`init(rawRepresentation:)`](p521/signing/privatekey/init(rawrepresentation:).md).

## Parameters

- `compactRepresentable`: A Boolean value that indicates whether CryptoKit   creates the key with the structure to enable compact point encoding.

## See Also

- [init<Bytes>(rawRepresentation: Bytes) throws](p521/signing/privatekey/init(rawrepresentation:).md)
  Creates a P-521 private key for signing from a collection of bytes.
- [init<Bytes>(derRepresentation: Bytes) throws](p521/signing/privatekey/init(derrepresentation:).md)
  Creates a P-521 private key for signing from a Distinguished Encoding Rules (DER) encoded representation.
- [init(pemRepresentation: String) throws](p521/signing/privatekey/init(pemrepresentation:).md)
  Creates a P-521 private key for signing from a Privacy-Enhanced Mail PEM) representation.
- [init<Bytes>(x963Representation: Bytes) throws](p521/signing/privatekey/init(x963representation:).md)
  Creates a P-521 private key for signing from an ANSI x9.63 representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/signing/privatekey/init(compactrepresentable:))*