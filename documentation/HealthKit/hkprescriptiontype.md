# HKPrescriptionType

**Framework**: Healthkit  
**Kind**: class

A type that identifies samples that store a prescription.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class HKPrescriptionType
```

#### Overview

The [`HKPrescriptionType`](hkprescriptiontype.md) class is a concrete subclass of the [`HKSampleType`](hksampletype.md) class. To create a vision prescription type instances, use the [`visionPrescriptionType()`](hkobjecttype/visionprescriptiontype().md) convenience method.

Use this data type to request permission to save vision prescriptions to the HealthKit store.

```swift
// Create the prescription data type.
let visionPrescriptionType = HKObjectType.visionPrescriptionType()


// Request authorization to save vision prescription samples.
store.requestAuthorization(toShare: [visionPrescriptionType],
                           read: []) { success, error in
    if let error {
        // Handle errors here.
        fatalError("*** An error occurred while requesting permission: \(error.localizedDescription) ***")
    }
}
```

> **Note**: Important Vision prescription samples require per-object authorization. Requesting authorization to read these samples using [`requestAuthorization(toShare:read:)`](hkhealthstore/requestauthorization(toshare:read:).md) fails with an error. Instead, use [`requestPerObjectReadAuthorization(for:predicate:completion:)`](hkhealthstore/requestperobjectreadauthorization(for:predicate:completion:).md) to request authorization before querying for samples.

## Relationships

### Inherits From
- [HKSampleType](hksampletype.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
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
- [class HKLensSpecification](hklensspecification.md)
  An abstract superclass for lens specifications.
- [class HKVisionPrism](hkvisionprism.md)
  Prescription data for eye alignment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/HealthKit/hkprescriptiontype)*