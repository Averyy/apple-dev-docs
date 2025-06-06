# init(derRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a P-521 digital signature from a Distinguished Encoding Rules (DER) encoded representation.

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

- `derRepresentation`: The DER-encoded representation of the   signature.

## See Also

- [init<D>(rawRepresentation: D) throws](p521/signing/ecdsasignature/init(rawrepresentation:).md)
  Creates a P-521 digital signature from a raw representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/signing/ecdsasignature/init(derrepresentation:))*