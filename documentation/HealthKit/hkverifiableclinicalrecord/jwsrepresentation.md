# jwsRepresentation

**Framework**: HealthKit  
**Kind**: property

A raw representation of the SMART Health Card’s contents.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var jwsRepresentation: Data { get }
```

#### Discussion

This property contains a JSON Web Signature (JWS) Compact Serialization of the card. The data is cryptographically signed by the issuer, and compressed.

> ❗ **Important**:  To ensure that the data is authentic and that no one has tampered with it, decompress the data and then use a public key from the issuer to verify their signature.

 To ensure that the data is authentic and that no one has tampered with it, decompress the data and then use a public key from the issuer to verify their signature.

## See Also

- [var dataRepresentation: Data](hkverifiableclinicalrecord/datarepresentation.md)
  A raw representation of the record’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecord/jwsrepresentation)*