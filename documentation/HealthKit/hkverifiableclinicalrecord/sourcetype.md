# sourceType

**Framework**: HealthKit  
**Kind**: property

The source for the verifiable clinical record

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var sourceType: HKVerifiableClinicalRecordSourceType? { get }
```

#### Discussion

For a list of valid sources, see [`HKVerifiableClinicalRecordSourceType`](hkverifiableclinicalrecordsourcetype.md).

## See Also

- [var issuedDate: Date](hkverifiableclinicalrecord/issueddate.md)
  The date when the issuer created the card.
- [var relevantDate: Date](hkverifiableclinicalrecord/relevantdate.md)
  A date relevant to this record, such as when the issuer administered a vaccine or performed a test.
- [var expirationDate: Date?](hkverifiableclinicalrecord/expirationdate.md)
  The date when the card expires.
- [var recordTypes: [String]](hkverifiableclinicalrecord/recordtypes.md)
  An array of strings representing the types of records contained in the card.
- [struct HKVerifiableClinicalRecordSourceType](hkverifiableclinicalrecordsourcetype.md)
  The source type for the verifiable clinical record.
- [var itemNames: [String]](hkverifiableclinicalrecord/itemnames.md)
  A human-readable description of the card’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecord/sourcetype)*