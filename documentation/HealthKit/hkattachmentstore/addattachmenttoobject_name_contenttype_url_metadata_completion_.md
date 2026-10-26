# addAttachmentToObject:name:contentType:URL:metadata:completion:

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Adds an attachment to the specified object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```objc
- (void) addAttachmentToObject:(HKObject *) object name:(NSString *) name contentType:(UTType *) contentType URL:(NSURL *) URL metadata:(NSDictionary<NSString *,id> *) metadata completion:(void (^)(HKAttachment *attachment, NSError *error)) completion;
```

#### Discussion

Use this method to add an attachment to an object in the HealthKit store. You can add more than one attachment to the specified object.

To add an attachment, start by creating an attachment store.

```objc
// Get the attachment store.
HKAttachmentStore *attachmentStore = [[HKAttachmentStore alloc] initWithHealthStore: store];
```

Next, add the attachment to an object that you’ve already saved to the HealthKit store.

```objc
// Attach the image to the sample.
[attachmentStore addAttachmentToObject:prescription
                              name:@"Glasses Prescription"
                       contentType:type
                               URL:url
                          metadata:nil
                        completion:^(HKAttachment * _Nullable attachment, NSError * _Nullable error) {
if (error != nil) {
    // Handle the error here.
    [NSException raise:@"Attachment Error" format:@"An error occurred while attaching a file: %@", error.localizedDescription];
}
}];
```

You can only add attachments to [`HKVisionPrescription`](../hkvisionprescription.md), [`HKGlassesPrescription`](../hkglassesprescription.md), and [`HKContactsPrescription`](../hkcontactsprescription.md) samples. The attachment must be a static image or PDF (no videos or GIFs). HealthKit supports attaching Live Photos, however it automatically selects and attaches the key photo.

## Parameters

- `object`: An object stored in the HealthKit store.
- `name`: The filename for the attachment.
- `contentType`: The type of data stored in the attachment.
- `URL`: The url for the attachment. This must be a local file url.
- `metadata`: Additional data associated with the attachment.
- `completion`: A completion handler that the system calls after adding the attachment. This handler takes the following parameters:

  - **attachment**: An object that represents the attachment. If an error occurred, the system sets this parameter to `nil`.
  - **error**: If an error occurred, this parameter contains information about the error. Otherwise, it’s `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkattachmentstore/addattachmenttoobject:name:contenttype:url:metadata:completion:)*