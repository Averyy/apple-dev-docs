# HKLensSpecification

**Framework**: HealthKit  
**Kind**: class

An abstract superclass for lens specifications.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class HKLensSpecification
```

#### Overview

Don’t instantiate this class directly. Instead, use one of its concrete subclasses: [`HKGlassesLensSpecification`](hkglasseslensspecification.md) or [`HKContactsLensSpecification`](hkcontactslensspecification.md).

## Topics

### Accessing lens specification data
- [var sphere: HKQuantity](hklensspecification/sphere.md)
  The correction for farsightedness.
- [var cylinder: HKQuantity?](hklensspecification/cylinder.md)
  Part of the correction for astigmatism that measures the strength of the correction.
- [var axis: HKQuantity?](hklensspecification/axis.md)
  Part of the correction for astigmatism that measures the orientation fo the correction.
- [var addPower: HKQuantity?](hklensspecification/addpower.md)
  The correction for nearsightedness.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [HKContactsLensSpecification](hkcontactslensspecification.md)
- [HKGlassesLensSpecification](hkglasseslensspecification.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class HKVisionPrescription](hkvisionprescription.md)
  A sample that stores a vision prescription.
- [class HKGlassesPrescription](hkglassesprescription.md)
  A sample that stores a prescription for glasses.
- [class HKContactsPrescription](hkcontactsprescription.md)
  A sample that store a prescription for contacts.
- [class HKGlassesLensSpecification](hkglasseslensspecification.md)
  An object that contains the glasses prescription data for one eye.
- [class HKContactsLensSpecification](hkcontactslensspecification.md)
  An object that contains the contacts prescription data for one eye.
- [class HKVisionPrism](hkvisionprism.md)
  Prescription data for eye alignment.
- [class HKPrescriptionType](hkprescriptiontype.md)
  A type that identifies samples that store a prescription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hklensspecification)*