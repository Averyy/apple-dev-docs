# getAttachments(for:completion:)

**Framework**: HealthKit  
**Kind**: method

Returns all the attachments for the specified object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func attachments(for object: HKObject) async throws -> [HKAttachment]
```

#### Discussion

Call this method to get all the attachments for the specified object.

```swift
let attachments: [HKAttachment]
do {
    attachments = try await attachmentStore.attachments(for: prescription)
} catch {
    // Handle the error here.
    fatalError("*** An error occurred while accessing the attachments for a prescription: \(error.localizedDescription) ***")
}

// Use the attachments here.
```

## Parameters

- `object`: An object from the HealthKit store.
- `completion`: A completion handler that the system calls to return the attachment. This handler takes the following parameters:

## See Also

- [func dataReader(for: HKAttachment) -> HKAttachmentDataReader](hkattachmentstore/datareader(for:).md)
  Returns a data reader for the attachment.
- [func getData(for: HKAttachment, completion: (Data?, (any Error)?) -> Void) -> Progress](hkattachmentstore/getdata(for:completion:).md)
  Returns an attachment’s data.
- [func streamData(for: HKAttachment, dataHandler: (Data?, (any Error)?, Bool) -> Void) -> Progress](hkattachmentstore/streamdata(for:datahandler:).md)
  Asynchronously returns the attachment’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachmentstore/getattachments(for:completion:))*