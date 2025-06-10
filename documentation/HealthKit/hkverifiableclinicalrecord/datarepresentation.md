# dataRepresentation

**Framework**: HealthKit  
**Kind**: property

A raw representation of the record’s data.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var dataRepresentation: Data { get }
```

#### Discussion

The data’s format varies based on its [`sourceType`](hkverifiableclinicalrecord/sourcetype.md):

> ❗ **Important**:  To ensure that the data is authentic and that no one has tampered with it, decompress the data and then use a public key from the issuer to verify their signature.

## See Also

- [var jwsRepresentation: Data](hkverifiableclinicalrecord/jwsrepresentation.md)
  A raw representation of the SMART Health Card’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecord/datarepresentation)*