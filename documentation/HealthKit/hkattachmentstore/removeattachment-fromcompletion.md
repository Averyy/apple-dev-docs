# removeAttachment(_:from:completion:)

**Framework**: HealthKit  
**Kind**: method

Removes the specified attachment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func removeAttachment(_ attachment: HKAttachment, from object: HKObject) async throws
```

#### Discussion

Use this method to remove an attachment from an object saved in the HealthKit store.

```swift
// Remove the attachment from the specified object.
do {
    try await attachmentStore.removeAttachment(myAttachment, from: myObject)
} catch {
    // Handle the error here.
    fatalError("*** An error occurred while removing an attachment: \(error.localizedDescription) ***")
}
```

## Parameters

- `attachment`: An attachment associated with the specified object.
- `object`: An object from the HealthKit store.
- `completion`: A completion handler that the system calls after removing the attachment. This handler takes the following parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachmentstore/removeattachment(_:from:completion:))*