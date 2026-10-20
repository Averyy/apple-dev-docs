# init(derRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init  
**Role**: Initializer

Creates a P-384 digital signature from a Distinguished Encoding Rules (DER) encoded representation.

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
init<D>(derRepresentation: D) throws where D : DataProtocol
```

## Parameters

- `derRepresentation`: The DER-encoded representation of the signature.

## See Also

### Creating a signature
- [init<D>(rawRepresentation: D) throws](./init%28rawrepresentation%29.md)
  Creates a P-384 digital signature from a raw representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p384/signing/ecdsasignature/init(derrepresentation:))*