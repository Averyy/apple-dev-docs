# getAttachments(for:completion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

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
func getAttachments(for object: HKObject, completion: @escaping @Sendable ([HKAttachment]?, (any Error)?) -> Void)
```

```swift
func attachments(for object: HKObject) async throws -> [HKAttachment]
```

```objc
- (void) getAttachmentsForObject:(HKObject *) object completion:(void (^)(NSArray<HKAttachment *> *attachments, NSError *error)) completion;
```

## Discussion

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

  - **attachments**: An array of attachments. If an error occurs, the system sets this parameter to `nil`.
  - **error**: If an error occurred, this parameter contains information about the error. Otherwise, it’s `nil`.

## See Also

### Accessing attachments
- [func dataReader(for: HKAttachment) -> HKAttachmentDataReader](./datareader%28for%29.md)
  Returns a data reader for the attachment.
- [func getData(for: HKAttachment, completion: (Data?, (any Error)?) -> Void) -> Progress](./getdata%28for,completion%29.md)
  Returns an attachment’s data.
- [func streamData(for: HKAttachment, dataHandler: (Data?, (any Error)?, Bool) -> Void) -> Progress](./streamdata%28for,datahandler%29.md)
  Asynchronously returns the attachment’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachmentstore/getattachments(for:completion:))*