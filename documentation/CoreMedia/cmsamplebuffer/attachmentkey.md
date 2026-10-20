# CMSampleBuffer.AttachmentKey

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

Keys that identify sample buffer attachments.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct AttachmentKey
```

## Topics

### Attachment Keys
- [static let cameraIntrinsicMatrix: CMSampleBuffer.AttachmentKey](./attachmentkey/cameraintrinsicmatrix.md)
- [static let displayEmptyMediaImmediately: CMSampleBuffer.AttachmentKey](./attachmentkey/displayemptymediaimmediately.md)
- [static let drainAfterDecoding: CMSampleBuffer.AttachmentKey](./attachmentkey/drainafterdecoding.md)
- [static let droppedFrameReason: CMSampleBuffer.AttachmentKey](./attachmentkey/droppedframereason.md)
- [static let droppedFrameReasonInfo: CMSampleBuffer.AttachmentKey](./attachmentkey/droppedframereasoninfo.md)
- [static let emptyMedia: CMSampleBuffer.AttachmentKey](./attachmentkey/emptymedia.md)
- [static let endsPreviousSampleDuration: CMSampleBuffer.AttachmentKey](./attachmentkey/endsprevioussampleduration.md)
- [static let fillDiscontinuitiesWithSilence: CMSampleBuffer.AttachmentKey](./attachmentkey/filldiscontinuitieswithsilence.md)
- [static let forceKeyFrame: CMSampleBuffer.AttachmentKey](./attachmentkey/forcekeyframe.md)
- [static let gradualDecoderRefresh: CMSampleBuffer.AttachmentKey](./attachmentkey/gradualdecoderrefresh.md)
- [static let permanentEmptyMedia: CMSampleBuffer.AttachmentKey](./attachmentkey/permanentemptymedia.md)
- [static let postNotificationWhenConsumed: CMSampleBuffer.AttachmentKey](./attachmentkey/postnotificationwhenconsumed.md)
- [static let resetDecoderBeforeDecoding: CMSampleBuffer.AttachmentKey](./attachmentkey/resetdecoderbeforedecoding.md)
- [static let resumeOutput: CMSampleBuffer.AttachmentKey](./attachmentkey/resumeoutput.md)
- [static let reverse: CMSampleBuffer.AttachmentKey](./attachmentkey/reverse.md)
- [static let sampleReferenceByteOffset: CMSampleBuffer.AttachmentKey](./attachmentkey/samplereferencebyteoffset.md)
- [static let sampleReferenceURL: CMSampleBuffer.AttachmentKey](./attachmentkey/samplereferenceurl.md)
- [static let speedMultiplier: CMSampleBuffer.AttachmentKey](./attachmentkey/speedmultiplier.md)
- [static let stillImageLensStabilizationInfo: CMSampleBuffer.AttachmentKey](./attachmentkey/stillimagelensstabilizationinfo.md)
- [static let transitionID: CMSampleBuffer.AttachmentKey](./attachmentkey/transitionid.md)
- [static let trimDurationAtEnd: CMSampleBuffer.AttachmentKey](./attachmentkey/trimdurationatend.md)
- [static let trimDurationAtStart: CMSampleBuffer.AttachmentKey](./attachmentkey/trimdurationatstart.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing Attachments
- [var sampleAttachments: CMSampleBuffer.SampleAttachmentsArray](./sampleattachments-swift.property.md)
  An array of sample attachments.
- [CMSampleBuffer.SampleAttachmentsArray](./sampleattachmentsarray.md)
- [CMSampleBuffer.PerSampleAttachmentsDictionary](./persampleattachmentsdictionary.md)
  A structure that defines keys to identify per-sample attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/attachmentkey)*