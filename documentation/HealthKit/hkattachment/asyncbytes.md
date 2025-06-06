# HKAttachment.AsyncBytes

**Framework**: HealthKit  
**Kind**: struct

An asynchronous sequence that returns the attached file as a series of bytes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct AsyncBytes
```

#### Overview

To access the attachment file as an asynchronous sequence of bytes, get a data reader from the attachment store, and then access its [`bytes`](hkattachmentdatareader/bytes.md) using a `for-await-in` loop.

```swift
// Get a data reader for the attachment.
let dataReader = attachmentStore.dataReader(for: myAttachment)

// Asynchronously access the attachment's bytes.
var data = Data()
do {
    for try await byte in dataReader.bytes {
        data.append(byte)
    }
} catch {
    // Handle the error here.
    fatalError("*** An error occurred while reading the attachment's data: \(error.localizedDescription) ***")
}

// Use the data here.
```

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [var name: String](hkattachment/name.md)
  The name of the attached file.
- [var identifier: UUID](hkattachment/identifier.md)
  The universally unique identifier for the attached file.
- [var contentType: UTType](hkattachment/contenttype.md)
  The type of data stored in the attached file.
- [var size: Int](hkattachment/size.md)
  The attachment’s size (in bytes).
- [var creationDate: Date](hkattachment/creationdate.md)
  The attachment’s creation date.
- [var metadata: [String : Any]?](hkattachment/metadata.md)
  Additional data associated with the attachment in the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachment/asyncbytes)*