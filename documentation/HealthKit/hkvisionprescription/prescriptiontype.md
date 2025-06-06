# prescriptionType

**Framework**: HealthKit  
**Kind**: property

The type of vision prescription.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var prescriptionType: HKVisionPrescriptionType { get }
```

#### Discussion

This property contains a value that indicates the type of prescription. For a list of possible values, see [`HKVisionPrescriptionType`](hkvisionprescriptiontype.md).

## See Also

- [class HKGlassesPrescription](hkglassesprescription.md)
  A sample that stores a prescription for glasses.
- [class HKContactsPrescription](hkcontactsprescription.md)
  A sample that store a prescription for contacts.
- [enum HKVisionPrescriptionType](hkvisionprescriptiontype.md)
  The type of vision prescription, for example a prescription for glasses or for contacts.
- [var dateIssued: Date](hkvisionprescription/dateissued.md)
  The date when the doctor issued the prescription.
- [var expirationDate: Date?](hkvisionprescription/expirationdate.md)
  The date when the prescription expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkvisionprescription/prescriptiontype)*