# dateIssued

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The date when the doctor issued the prescription.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var dateIssued: Date { get }
```

```objc
@property (nonatomic, copy, readonly) NSDate * dateIssued;
```

## See Also

### Accessing the prescription data
- [var prescriptionType: HKVisionPrescriptionType](./prescriptiontype.md)
  The type of vision prescription.
- [enum HKVisionPrescriptionType](../hkvisionprescriptiontype.md)
  The type of vision prescription, for example a prescription for glasses or for contacts.
- [var expirationDate: Date?](./expirationdate.md)
  The date when the prescription expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkvisionprescription/dateissued)*