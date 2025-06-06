# init(pemRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a P-256 private key for key agreement from a Privacy-Enhanced Mail PEM) representation.

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

- [init<Bytes>(rawRepresentation: Bytes) throws](p256/keyagreement/privatekey/init(rawrepresentation:).md)
  Creates a P-256 private key for key agreement from a collection of bytes.
- [init(compactRepresentable: Bool)](p256/keyagreement/privatekey/init(compactrepresentable:).md)
  Creates a random P-256 private key for key agreement.
- [init<Bytes>(derRepresentation: Bytes) throws](p256/keyagreement/privatekey/init(derrepresentation:).md)
  Creates a P-256 private key for key agreement from a Distinguished Encoding Rules (DER) encoded representation.
- [init<Bytes>(x963Representation: Bytes) throws](p256/keyagreement/privatekey/init(x963representation:).md)
  Creates a P-256 private key for key agreement from an ANSI x9.63 representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p256/keyagreement/privatekey/init(pemrepresentation:))*