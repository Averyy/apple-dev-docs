# CMSampleBuffer.AttachmentKey

**Framework**: Core Media  
**Kind**: struct

Keys that identify sample buffer attachments.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
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
- [static let cameraIntrinsicMatrix: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/cameraintrinsicmatrix.md)
- [static let displayEmptyMediaImmediately: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/displayemptymediaimmediately.md)
- [static let drainAfterDecoding: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/drainafterdecoding.md)
- [static let droppedFrameReason: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/droppedframereason.md)
- [static let droppedFrameReasonInfo: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/droppedframereasoninfo.md)
- [static let emptyMedia: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/emptymedia.md)
- [static let endsPreviousSampleDuration: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/endsprevioussampleduration.md)
- [static let fillDiscontinuitiesWithSilence: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/filldiscontinuitieswithsilence.md)
- [static let forceKeyFrame: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/forcekeyframe.md)
- [static let gradualDecoderRefresh: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/gradualdecoderrefresh.md)
- [static let permanentEmptyMedia: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/permanentemptymedia.md)
- [static let postNotificationWhenConsumed: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/postnotificationwhenconsumed.md)
- [static let resetDecoderBeforeDecoding: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/resetdecoderbeforedecoding.md)
- [static let resumeOutput: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/resumeoutput.md)
- [static let reverse: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/reverse.md)
- [static let sampleReferenceByteOffset: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/samplereferencebyteoffset.md)
- [static let sampleReferenceURL: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/samplereferenceurl.md)
- [static let speedMultiplier: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/speedmultiplier.md)
- [static let stillImageLensStabilizationInfo: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/stillimagelensstabilizationinfo.md)
- [static let transitionID: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/transitionid.md)
- [static let trimDurationAtEnd: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/trimdurationatend.md)
- [static let trimDurationAtStart: CMSampleBuffer.AttachmentKey](cmsamplebuffer/attachmentkey/trimdurationatstart.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var sampleAttachments: CMSampleBuffer.SampleAttachmentsArray](cmsamplebuffer/sampleattachments.md)
  An array of sample attachments.
- [CMSampleBuffer.SampleAttachmentsArray](cmsamplebuffer/sampleattachmentsarray.md)
  A structure that defines an array of sample attachments.
- [CMSampleBuffer.PerSampleAttachmentsDictionary](cmsamplebuffer/persampleattachmentsdictionary.md)
  A structure that defines keys to identify per-sample attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/attachmentkey)*