# HKAttachmentStore

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HKAttachmentStore : NSObject
```

#### Overview

Use an [`HKAttachmentStore`](./hkattachmentstore.md) object to manage attachments for samples that your app has saved to the HealthKit store.

## Topics

### Creating an attachment store
- [init(healthStore: HKHealthStore)](./hkattachmentstore/init%28healthstore%29.md)
  Creates an attachment store for the provided HealthKit store.
### Adding attachments
- [func addAttachment(to: HKObject, name: String, contentType: UTType, url: URL, metadata: [String : Any]) async throws -> HKAttachment](./hkattachmentstore/addattachment%28to,name,contenttype,url,metadata%29.md)
  Asynchronously adds an attachment to the specified object.
- [func addAttachment(to: HKObject, name: String, contentType: UTType, url: URL, metadata: [String : Any], completion: (HKAttachment?, (any Error)?) -> Void)](./hkattachmentstore/addattachment%28to,name,contenttype,url,metadata,completion%29.md)
  Adds an attachment to the specified object.
- [- addAttachmentToObject:name:contentType:URL:metadata:completion:](./hkattachmentstore/addattachmenttoobject_name_contenttype_url_metadata_completion_.md)
  Adds an attachment to the specified object.
### Accessing attachments
- [func getAttachments(for: HKObject, completion: ([HKAttachment]?, (any Error)?) -> Void)](./hkattachmentstore/getattachments%28for,completion%29.md)
  Returns all the attachments for the specified object.
- [func dataReader(for: HKAttachment) -> HKAttachmentDataReader](./hkattachmentstore/datareader%28for%29.md)
  Returns a data reader for the attachment.
- [func getData(for: HKAttachment, completion: (Data?, (any Error)?) -> Void) -> Progress](./hkattachmentstore/getdata%28for,completion%29.md)
  Returns an attachment’s data.
- [func streamData(for: HKAttachment, dataHandler: (Data?, (any Error)?, Bool) -> Void) -> Progress](./hkattachmentstore/streamdata%28for,datahandler%29.md)
  Asynchronously returns the attachment’s data.
### Removing attachments
- [func removeAttachment(HKAttachment, from: HKObject, completion: (Bool, (any Error)?) -> Void)](./hkattachmentstore/removeattachment%28_,from,completion%29.md)
  Removes the specified attachment.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Attachments
- [class HKAttachment](./hkattachment.md)
  A file that is attached to a sample in the HealthKit store.
- [class HKAttachmentDataReader](./hkattachmentdatareader.md)
  A reader that provides access to an attachment’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachmentstore)*