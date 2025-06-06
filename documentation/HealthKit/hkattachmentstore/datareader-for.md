# dataReader(for:)

**Framework**: HealthKit  
**Kind**: method

Returns a data reader for the attachment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func dataReader(for attachment: HKAttachment) -> HKAttachmentDataReader
```

#### Discussion

Call this method to access a data reader for the attachment’s contents.

```swift
// Get a data reader for the attachment.
let dataReader = attachmentStore.dataReader(for: myAttachment)
```

You can then read the attachment’s contents from the data reader.

```swift
let data: Data
do {
    data = try await dataReader.data
} catch {
    // Handle the error here.
    fatalError("*** An error occurred while accessing the attachment's data. \(error.localizedDescription) ***")
}

// Use the data here.
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

## Parameters

- `attachment`: An attachment associated with an object in the HealthKit store.

## See Also

- [func getAttachments(for: HKObject, completion: ([HKAttachment]?, (any Error)?) -> Void)](hkattachmentstore/getattachments(for:completion:).md)
  Returns all the attachments for the specified object.
- [func getData(for: HKAttachment, completion: (Data?, (any Error)?) -> Void) -> Progress](hkattachmentstore/getdata(for:completion:).md)
  Returns an attachment’s data.
- [func streamData(for: HKAttachment, dataHandler: (Data?, (any Error)?, Bool) -> Void) -> Progress](hkattachmentstore/streamdata(for:datahandler:).md)
  Asynchronously returns the attachment’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachmentstore/datareader(for:))*