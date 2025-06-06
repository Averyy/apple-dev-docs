# streamData(for:dataHandler:)

**Framework**: HealthKit  
**Kind**: method

Asynchronously returns the attachment’s data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func streamData(for attachment: HKAttachment, dataHandler: @escaping (Data?, (any Error)?, Bool) -> Void) -> Progress
```

#### Discussion

Call this method to incrementally read the attachment’s contents directly from the attachment store.

```swift
var data = Data()
attachmentStore.streamData(for: myAttachment) { dataChunk, error, done in
    
    if let error {
        // Handle the error here.
        fatalError("*** An error occurred while streaming the attachment's data. \(error.localizedDescription) ***")
    }
    
    guard let dataChunk else { return }
    
    data.append(dataChunk)
    
    if done {
        // Use the attachment's data here.
        print(data)
    }
}
```

## Parameters

- `attachment`: An attachment associated with an object in the HealthKit store.
- `dataHandler`: A closure that the system calls repeatedly to return the attachment’s contents. This closure takes the following parameters:

## See Also

- [func getAttachments(for: HKObject, completion: ([HKAttachment]?, (any Error)?) -> Void)](hkattachmentstore/getattachments(for:completion:).md)
  Returns all the attachments for the specified object.
- [func dataReader(for: HKAttachment) -> HKAttachmentDataReader](hkattachmentstore/datareader(for:).md)
  Returns a data reader for the attachment.
- [func getData(for: HKAttachment, completion: (Data?, (any Error)?) -> Void) -> Progress](hkattachmentstore/getdata(for:completion:).md)
  Returns an attachment’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachmentstore/streamdata(for:datahandler:))*