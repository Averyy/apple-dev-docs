# HKAttachmentStore

**Framework**: HealthKit  
**Kind**: class

The access point for attachments associated with samples in the HealthKit store.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class HKAttachmentStore
```

#### Overview

Use an [`HKAttachmentStore`](hkattachmentstore.md) object to manage attachments for samples that your app has saved to the HealthKit store.

## Topics

### Creating an attachment store
- [init(healthStore: HKHealthStore)](hkattachmentstore/init(healthstore:).md)
  Creates an attachment store for the provided HealthKit store.
### Adding attachments
- [func addAttachment(to: HKObject, name: String, contentType: UTType, url: URL, metadata: [String : Any]) async throws -> HKAttachment](hkattachmentstore/addattachment(to:name:contenttype:url:metadata:).md)
  Asynchronously adds an attachment to the specified object.
- [func addAttachment(to: HKObject, name: String, contentType: UTType, url: URL, metadata: [String : Any], completion: (HKAttachment?, (any Error)?) -> Void)](hkattachmentstore/addattachment(to:name:contenttype:url:metadata:completion:).md)
  Adds an attachment to the specified object.
### Accessing attachments
- [func getAttachments(for: HKObject, completion: ([HKAttachment]?, (any Error)?) -> Void)](hkattachmentstore/getattachments(for:completion:).md)
  Returns all the attachments for the specified object.
- [func dataReader(for: HKAttachment) -> HKAttachmentDataReader](hkattachmentstore/datareader(for:).md)
  Returns a data reader for the attachment.
- [func getData(for: HKAttachment, completion: (Data?, (any Error)?) -> Void) -> Progress](hkattachmentstore/getdata(for:completion:).md)
  Returns an attachment’s data.
- [func streamData(for: HKAttachment, dataHandler: (Data?, (any Error)?, Bool) -> Void) -> Progress](hkattachmentstore/streamdata(for:datahandler:).md)
  Asynchronously returns the attachment’s data.
### Removing attachments
- [func removeAttachment(HKAttachment, from: HKObject, completion: (Bool, (any Error)?) -> Void)](hkattachmentstore/removeattachment(_:from:completion:).md)
  Removes the specified attachment.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class HKAttachment](hkattachment.md)
  A file that is attached to a sample in the HealthKit store.
- [class HKAttachmentDataReader](hkattachmentdatareader.md)
  A reader that provides access to an attachment’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachmentstore)*