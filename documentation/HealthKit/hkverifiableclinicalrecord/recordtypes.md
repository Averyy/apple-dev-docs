# recordTypes

**Framework**: HealthKit  
**Kind**: property

An array of strings representing the types of records contained in the card.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var recordTypes: [String] { get }
```

## See Also

- [var issuedDate: Date](hkverifiableclinicalrecord/issueddate.md)
  The date when the issuer created the card.
- [var relevantDate: Date](hkverifiableclinicalrecord/relevantdate.md)
  A date relevant to this record, such as when the issuer administered a vaccine or performed a test.
- [var expirationDate: Date?](hkverifiableclinicalrecord/expirationdate.md)
  The date when the card expires.
- [var sourceType: HKVerifiableClinicalRecordSourceType?](hkverifiableclinicalrecord/sourcetype.md)
  The source for the verifiable clinical record
- [struct HKVerifiableClinicalRecordSourceType](hkverifiableclinicalrecordsourcetype.md)
  The source type for the verifiable clinical record.
- [var itemNames: [String]](hkverifiableclinicalrecord/itemnames.md)
  A human-readable description of the card’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecord/recordtypes)*