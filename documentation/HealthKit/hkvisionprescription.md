# HKVisionPrescription

**Framework**: HealthKit  
**Kind**: class

A sample that stores a vision prescription.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class HKVisionPrescription
```

#### Overview

Use this class to create an image-only prescription. Here, you attach the prescription as an image or PDF to a simple sample. The sample contains only basic information about the prescription, such as the issue and expiration dates. To see the prescription data, people must view the attached image or PDF.

> ❗ **Important**:  Some regions may require an image of the original prescription to validate the prescription record.

To create an image-only prescription, start by creating an [`HKVisionPrescription`](hkvisionprescription.md) sample object.

```swift
// Create a minimal prescription sample that just holds an image attachment.
let prescription = HKVisionPrescription(type: .glasses,
                                        dateIssued: Date(),
                                        expirationDate: nil,
                                        device: HKDevice.local(),
                                        metadata: nil)
```

Next, save the sample to the HealthKit store.

```swift
// Save the sample to the HealthKit store.
do {
    try await store.save(prescription)
} catch {
    // Handle the error here.
    fatalError("*** An error occurred while saving the prescription sample to the HealthKit store \(error.localizedDescription) ***")
}
```

Then, you can attach the image or PDF to the sample.

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

For more information about adding images or pdfs as attachments, see [`HKAttachmentStore`](hkattachmentstore.md). To create a vision prescription sample that contains the full data for the prescription, use [`HKGlassesPrescription`](hkglassesprescription.md) or [`HKContactsPrescription`](hkcontactsprescription.md) instead.

## Topics

### Creating vision prescription samples
- [convenience init(type: HKVisionPrescriptionType, dateIssued: Date, expirationDate: Date?, device: HKDevice?, metadata: [String : Any]?)](hkvisionprescription/init(type:dateissued:expirationdate:device:metadata:).md)
  Creates a new vision prescription sample.
### Accessing the prescription data
- [var prescriptionType: HKVisionPrescriptionType](hkvisionprescription/prescriptiontype.md)
  The type of vision prescription.
- [enum HKVisionPrescriptionType](hkvisionprescriptiontype.md)
  The type of vision prescription, for example a prescription for glasses or for contacts.
- [var dateIssued: Date](hkvisionprescription/dateissued.md)
  The date when the doctor issued the prescription.
- [var expirationDate: Date?](hkvisionprescription/expirationdate.md)
  The date when the prescription expires.

## Relationships

### Inherits From
- [HKSample](hksample.md)
### Inherited By
- [HKContactsPrescription](hkcontactsprescription.md)
- [HKGlassesPrescription](hkglassesprescription.md)
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
- [class HKPrescriptionType](hkprescriptiontype.md)
  A type that identifies samples that store a prescription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkvisionprescription)*