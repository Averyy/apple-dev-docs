# getData(for:completion:)

**Framework**: HealthKit  
**Kind**: method

Returns an attachment’s data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func getData(for attachment: HKAttachment, completion: @escaping (Data?, (any Error)?) -> Void) -> Progress
```

#### Discussion

Call this method to read the attachment’s contents directly from the attachment store.

```swift
let progress = attachmentStore.getData(for: myAttachment) { data, error in
    if let error {
        // Handle the error here.
        fatalError("*** An error occurred while accessing the attachment's data. \(error.localizedDescription) ***")
    }
    
    // Use the data here.
}

// Monitor the progress here.
```

## Parameters

- `attachment`: An attachment associated with an object in the HealthKit store.
- `completion`: A completion handler that the system calls to return the data. This handler takes the following parameters:

## See Also

- [func getAttachments(for: HKObject, completion: ([HKAttachment]?, (any Error)?) -> Void)](hkattachmentstore/getattachments(for:completion:).md)
  Returns all the attachments for the specified object.
- [func dataReader(for: HKAttachment) -> HKAttachmentDataReader](hkattachmentstore/datareader(for:).md)
  Returns a data reader for the attachment.
- [func streamData(for: HKAttachment, dataHandler: (Data?, (any Error)?, Bool) -> Void) -> Progress](hkattachmentstore/streamdata(for:datahandler:).md)
  Asynchronously returns the attachment’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachmentstore/getdata(for:completion:))*