# visionPrescriptionType()

**Framework**: HealthKit  
**Kind**: method

Returns a shared vision prescription type object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class func visionPrescriptionType() -> HKPrescriptionType
```

#### Discussion

This method returns an instance of the [`HKPrescriptionType`](hkprescriptiontype.md) concrete subclass. Use a prescription type to request permission to read or write prescriptions from the HealthKit store., and to create samples that store prescription information. In HealthKit, all prescriptions use the same [`HKPrescriptionType`](hkprescriptiontype.md) instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobjecttype/visionprescriptiontype())*