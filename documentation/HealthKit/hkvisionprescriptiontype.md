# HKVisionPrescriptionType

**Framework**: HealthKit  
**Kind**: enum

The type of vision prescription, for example a prescription for glasses or for contacts.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum HKVisionPrescriptionType
```

## Topics

### Prescription types
- [HKVisionPrescriptionType.glasses](hkvisionprescriptiontype/glasses.md)
  A prescription for glasses.
- [HKVisionPrescriptionType.contacts](hkvisionprescriptiontype/contacts.md)
  A prescription for contacts.
### Initializers
- [init?(rawValue: UInt)](hkvisionprescriptiontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var prescriptionType: HKVisionPrescriptionType](hkvisionprescription/prescriptiontype.md)
  The type of vision prescription.
- [var dateIssued: Date](hkvisionprescription/dateissued.md)
  The date when the doctor issued the prescription.
- [var expirationDate: Date?](hkvisionprescription/expirationdate.md)
  The date when the prescription expires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkvisionprescriptiontype)*