# addAttachment(to:name:contentType:url:metadata:)

**Framework**: HealthKit  
**Kind**: method

Asynchronously adds an attachment to the specified object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func addAttachment(to object: HKObject, name: String, contentType: UTType, url: URL, metadata: [String : Any] = [:]) async throws -> HKAttachment
```

#### Discussion

Use this method to add an attachment to an object in the HealthKit store. You can add more than one attachment to the specified object.

To add an attachment, start by creating an attachment store.

```swift
// Get the attachment store.
let attachmentStore = HKAttachmentStore(healthStore: store)
```

Next, add the attachment to an object that you’ve already saved to the HealthKit store.

```swift
// Attach the image to the sample.
do {
    _ = try await attachmentStore.addAttachment(to: prescription,
                                                name: "Glasses Prescription",
                                                contentType: type,
                                                url: url)
} catch {
    // Handle the error.
    fatalError("*** An error occurred while attaching the image: \(error.localizedDescription) ***")
}
```

You can only add attachments to [`HKVisionPrescription`](hkvisionprescription.md), [`HKGlassesPrescription`](hkglassesprescription.md), and [`HKContactsPrescription`](hkcontactsprescription.md) samples. The attachment must be a static image or PDF (no videos or GIFs). HealthKit supports attaching Live Photos, however it automatically selects and attaches the key photo.

## Parameters

- `object`: An object stored in the HealthKit store.
- `name`: The filename for the attachment.
- `contentType`: The type of data stored in the attachment.
- `url`: The url for the attachment. This must be a local file url.
- `metadata`: Additional data associated with the attachment.

## See Also

- [func addAttachment(to: HKObject, name: String, contentType: UTType, url: URL, metadata: [String : Any], completion: (HKAttachment?, (any Error)?) -> Void)](hkattachmentstore/addattachment(to:name:contenttype:url:metadata:completion:).md)
  Adds an attachment to the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachmentstore/addattachment(to:name:contenttype:url:metadata:))*