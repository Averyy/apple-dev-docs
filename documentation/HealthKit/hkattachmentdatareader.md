# HKAttachmentDataReader

**Framework**: HealthKit  
**Kind**: class

A reader that provides access to an attachment’s data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
class HKAttachmentDataReader
```

#### Overview

To access the attachment’s data, get a data reader from the attachment store.

```swift
let attachmentStore = HKAttachmentStore(healthStore: store)

// Get a data reader for the attachment.
let dataReader = attachmentStore.dataReader(for: myAttachment)
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

## Topics

### Reading attachment data
- [var data: Data](hkattachmentdatareader/data.md)
  The abstract’s data.
- [var bytes: HKAttachment.AsyncBytes](hkattachmentdatareader/bytes.md)
  An asynchronous sequence that provides the attachment’s data.
- [var progress: Progress](hkattachmentdatareader/progress.md)
  An object you can use to track the progress while reading an attachment’s data.
### Accessing the attachment object
- [var attachment: HKAttachment](hkattachmentdatareader/attachment.md)
  An attachment object that represents the file from which the reader is reading.

## See Also

- [class HKAttachment](hkattachment.md)
  A file that is attached to a sample in the HealthKit store.
- [class HKAttachmentStore](hkattachmentstore.md)
  The access point for attachments associated with samples in the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachmentdatareader)*