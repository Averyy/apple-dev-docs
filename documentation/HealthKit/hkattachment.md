# HKAttachment

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

A file that is attached to a sample in the HealthKit store.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class HKAttachment
```

```objc
@interface HKAttachment : NSObject
```

## Overview

To access the attachment’s data, get a data reader from the attachment store for each attachment.

```swift
let attachmentStore = HKAttachmentStore(healthStore: store)

let attachments: [HKAttachment]
do {
    attachments = try await attachmentStore.attachments(for: prescription)
} catch {
    // Handle the error here.
    fatalError("*** An error occurred while accessing the attachments for a prescription: \(error.localizedDescription) ***")
}

// Use the attachments here.
print("*** \(attachments.count) attachments found ***")

for attachment in attachments {

    // Get a data reader for the attachment.
    let dataReader = attachmentStore.dataReader(for:   attachment)

    // Read the data here.
}
```

You can then asynchronously access the whole data object.

```swift
let data: Data
do {
    data = try await dataReader.data
} catch {
    // Handle the error here.
    fatalError("*** An error occurred while accessing the attachment's data. \(error.localizedDescription) ***")
}
```

Alternatively, you can access the file’s contents as an asynchronous sequence of bytes.

```swift
// Asynchronously access the attachment's bytes.
var data = Data()
do {
    for try await byte in dataReader.bytes {
        // Use the bytes here.
        data.append(byte)
    }
} catch {
    // Handle the error here.
    fatalError("*** An error occurred while reading the attachment's data: \(error.localizedDescription) ***")
}
```

> **Note**:  You can only add attachments to [`HKVisionPrescription`](./hkvisionprescription.md), [`HKGlassesPrescription`](./hkglassesprescription.md), and [`HKContactsPrescription`](./hkcontactsprescription.md) samples. You can also read attachments from [`clinicalNoteRecord`](./hkclinicaltypeidentifier/clinicalnoterecord.md) samples.

## Topics

### Accessing attachment data
- [var name: String](./hkattachment/name.md)
  The name of the attached file.
- [var identifier: UUID](./hkattachment/identifier.md)
  The universally unique identifier for the attached file.
- [var contentType: UTType](./hkattachment/contenttype.md)
  The type of data stored in the attached file.
- [var size: Int](./hkattachment/size.md)
  The attachment’s size (in bytes).
- [var creationDate: Date](./hkattachment/creationdate.md)
  The attachment’s creation date.
- [var metadata: [String : Any]?](./hkattachment/metadata.md)
  Additional data associated with the attachment in the HealthKit store.
- [HKAttachment.AsyncBytes](./hkattachment/asyncbytes.md)
  An asynchronous sequence that returns the attached file as a series of bytes.
### Initializers
- [init?(coder: NSCoder)](./hkattachment/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Related Documentation
- [class HKVisionPrescription](./hkvisionprescription.md)
  A sample that stores a vision prescription.
- [class HKGlassesPrescription](./hkglassesprescription.md)
  A sample that stores a prescription for glasses.
- [class HKContactsPrescription](./hkcontactsprescription.md)
  A sample that store a prescription for contacts.
### Attachments
- [class HKAttachmentStore](./hkattachmentstore.md)
  The access point for attachments associated with samples in the HealthKit store.
- [class HKAttachmentDataReader](./hkattachmentdatareader.md)
  A reader that provides access to an attachment’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachment)*