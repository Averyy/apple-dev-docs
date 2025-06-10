# HKContactsLensSpecification

**Framework**: HealthKit  
**Kind**: class

An object that contains the contacts prescription data for one eye.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class HKContactsLensSpecification
```

#### Overview

To create a sample that stores a contacts prescription, start by defining a specification for each eye. Each lens specification object requires a `sphere` parameter. This measures the lens’s strength for correcting either nearsightedness or farsightedness (measured in [`diopter()`](hkunit/diopter().md) units).

```swift
// The correction for farsightedness.
let sphere = HKQuantity(unit: .diopter(), doubleValue: -0.75)
```

Next, create values for any of the prescription’s optional parameters. For example, if the prescription corrects for astigmatism, create the `cylinder` and `axis` values. The `cylinder` value uses [`diopter()`](hkunit/diopter().md) units, while the `axis` uses [`degreeAngle()`](hkunit/degreeangle().md).

```swift
// The corrections for astigmatism.
let cylinder = HKQuantity(unit: .diopter(), doubleValue: -0.5)
let axis = HKQuantity(unit: .degreeAngle(), doubleValue: 155.0)
```

To add a multifocal correction for reading, create an `addPower` value using [`diopter()`](hkunit/diopter().md) units.

```swift
// Multifocal correction for reading.
let addPower = HKQuantity(unit: .diopter(), doubleValue: +2.00)
```

To add fitting information for the contact lens, create `baseCurve` and `diameter` values. Both of these values use millimeters.

```swift
// The fitting information.
let baseCurve = HKQuantity(unit: HKUnit.meterUnit(with: .milli),
                           doubleValue: 9.0)

let diameter = HKQuantity(unit: HKUnit.meterUnit(with: .milli),
                          doubleValue: 12.0)
```

Then you can create the [`HKContactsLensSpecification`](hkcontactslensspecification.md) lens specification.

```swift
// The prescription for the right eye.
let contactsRightEye = HKContactsLensSpecification(sphere: sphere,
                                                   cylinder: cylinder,
                                                   axis: axis,
                                                   addPower: addPower,
                                                   baseCurve: baseCurve,
                                                   diameter: diameter)
```

After you create your lens specifications, you can create an [`HKContactsPrescription`](hkcontactsprescription.md) sample.

```swift
// The date the doctor issued the prescription.
let dateIssued = Date()

// The date when the prescription expires.
let expirationDate = dateIssued.addingTimeInterval(60 * 24 * 365)

// The contacts prescription.
let prescription = HKContactsPrescription(rightEyeSpecification: contactsRightEye,
                                          leftEyeSpecification: contactsLeftEye,
                                          brand: "MyBrand Name",
                                          dateIssued: dateIssued,
                                          expirationDate: expirationDate,
                                          device: HKDevice.local(),
                                          metadata: nil)
```

Then save the sample to the HealthKit store.

```swift
// Save the sample to the HealthKit store.
do {
    try await store.save(prescription)
} catch {
    // Handle the error here.
    fatalError("*** An error occurred while saving the prescription sample to the HealthKit store \(error.localizedDescription) ***")
}
```

Finally, add an image or PDF of the prescription to the sample as an attachment.

```swift
// Get the attachment store.
let attachmentStore = HKAttachmentStore(healthStore: store)

// Attach the image to the sample.
do {
    _ = try await attachmentStore.addAttachment(to: prescription,
                                                name: "Glasses Prescription",
                                                contentType: type,
                                                url: url)
} catch {
    // Handle the error.
    fatalError("*** An error occurred while attaching the image: \(error.localizedDescription) ***")
}
```

> ❗ **Important**:  Many regions require an image of the prescription to manufacture glasses or contacts. Add an image or pdf of the prescription as an attachment. For more information, see [`HKAttachmentStore`](hkattachmentstore.md).

## Topics

### Creating contacts lens specifications
- [init(sphere: HKQuantity, cylinder: HKQuantity?, axis: HKQuantity?, addPower: HKQuantity?, baseCurve: HKQuantity?, diameter: HKQuantity?)](hkcontactslensspecification/init(sphere:cylinder:axis:addpower:basecurve:diameter:).md)
  Creates a new contact lens specification, containing the prescription data for one eye.
### Accessing the specification’s data
- [var baseCurve: HKQuantity?](hkcontactslensspecification/basecurve.md)
  Part of the contact’s fit, it measures the curve of the back side of the contact, measured in mm.
- [var diameter: HKQuantity?](hkcontactslensspecification/diameter.md)
  Part of the contact’s fit, it measures the diameter of the lens, measured in mm.

## Relationships

### Inherits From
- [HKLensSpecification](hklensspecification.md)
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
- [class HKLensSpecification](hklensspecification.md)
  An abstract superclass for lens specifications.
- [class HKVisionPrism](hkvisionprism.md)
  Prescription data for eye alignment.
- [class HKPrescriptionType](hkprescriptiontype.md)
  A type that identifies samples that store a prescription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcontactslensspecification)*