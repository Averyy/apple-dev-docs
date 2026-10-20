# recordTypes

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSArray<NSString *> * recordTypes;
```

## See Also

### Reading Metadata
- [var issuedDate: Date](./issueddate.md)
  The date when the issuer created the card.
- [var relevantDate: Date](./relevantdate.md)
  A date relevant to this record, such as when the issuer administered a vaccine or performed a test.
- [var expirationDate: Date?](./expirationdate.md)
  The date when the card expires.
- [var sourceType: HKVerifiableClinicalRecordSourceType?](./sourcetype.md)
  The source for the verifiable clinical record
- [struct HKVerifiableClinicalRecordSourceType](../hkverifiableclinicalrecordsourcetype.md)
  The source type for the verifiable clinical record.
- [var itemNames: [String]](./itemnames.md)
  A human-readable description of the card’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecord/recordtypes)*