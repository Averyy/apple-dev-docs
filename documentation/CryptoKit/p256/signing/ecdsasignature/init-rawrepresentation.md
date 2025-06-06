# init(rawRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a P-256 digital signature from a raw representation.

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
init<D>(rawRepresentation: D) throws where D : DataProtocol
```

## Parameters

- `rawRepresentation`: A raw representation of the signature as a   collection of contiguous bytes.

## See Also

- [init<D>(derRepresentation: D) throws](p256/signing/ecdsasignature/init(derrepresentation:).md)
  Creates a P-256 digital signature from a Distinguished Encoding Rules (DER) encoded representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p256/signing/ecdsasignature/init(rawrepresentation:))*