# CMSampleBufferAttachmentKeyDefinitions

**Framework**: Core Media  
**Kind**: enum

A namespace for sample buffer attachment keys.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum CMSampleBufferAttachmentKeyDefinitions
```

## Topics

### Type Properties
- [static let cameraIntrinsicMatrix: CVAttachmentKeyDefinition<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, CMCameraIntrinsicMatrix>](cmsamplebufferattachmentkeydefinitions/cameraintrinsicmatrix.md)
  Provides the 3x3 camera intrinsic matrix applied to the current sample buffer.
- [static let displayEmptyMediaImmediately: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>](cmsamplebufferattachmentkeydefinitions/displayemptymediaimmediately.md)
  Indicates that the empty marker should be dequeued immediately regardless of its timestamp.
- [static let drainAfterDecoding: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>](cmsamplebufferattachmentkeydefinitions/drainafterdecoding.md)
  Indicates whether the sample buffer should be drained after decoding.
- [static let droppedFrameReason: CVAttachmentKeyDefinition<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, CMDroppedFrameReason>](cmsamplebufferattachmentkeydefinitions/droppedframereason.md)
  Indicates the reason the current video frame was dropped.
- [static let droppedFrameReasonInfo: CVAttachmentKeyDefinition<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, CMDroppedFrameReason.Info>](cmsamplebufferattachmentkeydefinitions/droppedframereasoninfo.md)
  Indicates additional information regarding the dropped video frame.
- [static let emptyMedia: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>](cmsamplebufferattachmentkeydefinitions/emptymedia.md)
  Marks an intentionally empty interval in the sequence of samples.
- [static let endsPreviousSampleDuration: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>](cmsamplebufferattachmentkeydefinitions/endsprevioussampleduration.md)
  Indicates that sample buffer’s decode timestamp may be used to define the previous sample buffer’s duration.
- [static let fillDiscontinuitiesWithSilence: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>](cmsamplebufferattachmentkeydefinitions/filldiscontinuitieswithsilence.md)
  Fill the difference between discontiguous sample buffers with silence.
- [static let forceKeyFrame: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>](cmsamplebufferattachmentkeydefinitions/forcekeyframe.md)
  Indicates that the current or next video sample buffer should be forced to be encoded as a key frame.
- [static let gradualDecoderRefresh: CVAttachmentKeyDefinition<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Int16>](cmsamplebufferattachmentkeydefinitions/gradualdecoderrefresh.md)
  Indicates the decoder refresh count.
- [static let permanentEmptyMedia: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>](cmsamplebufferattachmentkeydefinitions/permanentemptymedia.md)
  Marks the end of the sequence of samples.
- [static let postNotificationWhenConsumed: CVAttachmentKeyDefinition<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, CMCustomNotificationInfo>](cmsamplebufferattachmentkeydefinitions/postnotificationwhenconsumed.md)
  Indicates that decode pipelines should post a notification when consuming the sample buffer.
- [static let resetDecoderBeforeDecoding: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>](cmsamplebufferattachmentkeydefinitions/resetdecoderbeforedecoding.md)
  Indicates whether the sample buffer should be reset before decoding.
- [static let resumeOutput: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>](cmsamplebufferattachmentkeydefinitions/resumeoutput.md)
  If present, indicates that output should be resumed following a discontinuity.
- [static let reverse: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>](cmsamplebufferattachmentkeydefinitions/reverse.md)
  Indicates that the decoded contents of the sample buffer should be reversed.
- [static let speedMultiplier: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Float>](cmsamplebufferattachmentkeydefinitions/speedmultiplier.md)
  The factor by which the sample buffer’s presentation should be accelerated.
- [static let stillImageLensStabilizationInfo: CVAttachmentKeyDefinition<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, CMStillImageLensStabilization>](cmsamplebufferattachmentkeydefinitions/stillimagelensstabilizationinfo.md)
  Indicates information about the lens stabilization applied to the current still image buffer.
- [static let transitionID: CVAttachmentKeyDefinition<CMSampleBufferAttachmentKeyDefinitions.ShouldNotPropagate, Int>](cmsamplebufferattachmentkeydefinitions/transitionid.md)
  Marks a transition from one source of buffers to another.
- [static let trimDurationAtEnd: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, CMTime>](cmsamplebufferattachmentkeydefinitions/trimdurationatend.md)
  The duration that should be removed at the end of the sample buffer, after decoding.
- [static let trimDurationAtStart: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, CMTime>](cmsamplebufferattachmentkeydefinitions/trimdurationatstart.md)
  The duration that should be removed at the beginning of the sample buffer, after decoding.

## Relationships

### Conforms To
- [CVAttachmentKeyDefinitions](../CoreVideo/CVAttachmentKeyDefinitions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions)*