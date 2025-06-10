# HKVisionPrism

**Framework**: HealthKit  
**Kind**: class

Prescription data for eye alignment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class HKVisionPrism
```

#### Overview

To include prism information in a glasses prescription, start by creating an [`HKVisionPrism`](hkvisionprism.md) object.

```swift
// The correction for eye alignment.
let prismQuantity = HKQuantity(unit: .prismDiopter(), doubleValue: +0.25)
let angle = HKQuantity(unit: .degreeAngle(), doubleValue: 15.0)
let prism = HKVisionPrism(amount: prismQuantity,
                          angle: angle,
                          eye: .right)
```

Then, pass this value to the [`HKGlassesLensSpecification`](hkglasseslensspecification.md)’s initializer.

```swift
// The prescription for the right eye.
let glassesRightEye = HKGlassesLensSpecification(sphere: sphere,
                                                 cylinder: cylinder,
                                                 axis: axis,
                                                 addPower: addPower,
                                                 vertexDistance: vertexDistance,
                                                 prism: prism,
                                                 farPupillaryDistance: farDistance,
                                                 nearPupillaryDistance: nearDistance)
```

Finally, create the glasses prescription and save it to the HealthKit store.

```swift
// The glasses prescription.
let prescription = HKGlassesPrescription(rightEyeSpecification: glassesRightEye,
                                               leftEyeSpecification: glassesLeftEye,
                                               dateIssued: dateIssued,
                                               expirationDate: expirationDate,
                                               device: HKDevice.local(),
                                               metadata: nil)
// Save the sample to the HealthKit store.
do {
    try await store.save(prescription)
} catch {
    // Handle the error here.
    fatalError("*** An error occurred while saving the prescription sample to the HealthKit store \(error.localizedDescription) ***")
}
```

## Topics

### Creating vision prism objects
- [init(amount: HKQuantity, angle: HKQuantity, eye: HKVisionEye)](hkvisionprism/init(amount:angle:eye:).md)
  Creates a new vision prism object, using a single quantity and an alignment angle.
- [init(verticalAmount: HKQuantity, verticalBase: HKPrismBase, horizontalAmount: HKQuantity, horizontalBase: HKPrismBase, eye: HKVisionEye)](hkvisionprism/init(verticalamount:verticalbase:horizontalamount:horizontalbase:eye:).md)
  Creates a new vision prism object that separates the correction strength into horizontal and vertical components.
### Accessing lens specification data
- [var eye: HKVisionEye](hkvisionprism/eye.md)
  A value indicating which eye the correction applies to.
- [enum HKVisionEye](hkvisioneye.md)
  A value that specifies the eye for a vision prescription.
- [var amount: HKQuantity](hkvisionprism/amount.md)
  The strength of the correction.
- [var angle: HKQuantity](hkvisionprism/angle.md)
  The orientation of the adjustment.
- [var horizontalAmount: HKQuantity](hkvisionprism/horizontalamount.md)
  The strength of the horizontal correction.
- [var horizontalBase: HKPrismBase](hkvisionprism/horizontalbase.md)
  The orientation of the horizontal portion of the correction.
- [var verticalAmount: HKQuantity](hkvisionprism/verticalamount.md)
  The strength of the vertical correction.
- [var verticalBase: HKPrismBase](hkvisionprism/verticalbase.md)
  The orientation of the vertical portion of the correction.
- [enum HKPrismBase](hkprismbase.md)
  The orientation of the prism correction, represented by the location of the prism’s base (the thickest part of the prism).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [class HKPrescriptionType](hkprescriptiontype.md)
  A type that identifies samples that store a prescription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkvisionprism)*