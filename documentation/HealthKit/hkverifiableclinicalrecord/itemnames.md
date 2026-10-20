# itemNames

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A human-readable description of the card’s contents.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var itemNames: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * itemNames;
```

## See Also

### Reading Metadata
- [var issuedDate: Date](./issueddate.md)
  The date when the issuer created the card.
- [var relevantDate: Date](./relevantdate.md)
  A date relevant to this record, such as when the issuer administered a vaccine or performed a test.
- [var expirationDate: Date?](./expirationdate.md)
  The date when the card expires.
- [var recordTypes: [String]](./recordtypes.md)
  An array of strings representing the types of records contained in the card.
- [var sourceType: HKVerifiableClinicalRecordSourceType?](./sourcetype.md)
  The source for the verifiable clinical record
- [struct HKVerifiableClinicalRecordSourceType](../hkverifiableclinicalrecordsourcetype.md)
  The source type for the verifiable clinical record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecord/itemnames)*