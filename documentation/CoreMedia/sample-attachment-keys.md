# Sample Attachment Keys

**Framework**: Core Media

Keys that specify attachments to individual samples in a buffer.

#### Overview

You can get and set sample-level attachments in a sample buffer using the [`CMSampleBufferGetSampleAttachmentsArray(_:createIfNecessary:)`](cmsamplebuffergetsampleattachmentsarray(_:createifnecessary:).md) function.

## Topics

### Sample Keys
- [let kCMSampleAttachmentKey_NotSync: CFString](kcmsampleattachmentkey_notsync.md)
  Indicates whether the sample is a sync sample (type `CFBoolean`, default false).
- [let kCMSampleAttachmentKey_PartialSync: CFString](kcmsampleattachmentkey_partialsync.md)
  Indicates whether the sample is a partial sync sample (type `CFBoolean`, default false).
- [let kCMSampleAttachmentKey_DependsOnOthers: CFString](kcmsampleattachmentkey_dependsonothers.md)
  Indicates whether the sample depends on other samples for decoding (type `CFBoolean`).
- [let kCMSampleAttachmentKey_IsDependedOnByOthers: CFString](kcmsampleattachmentkey_isdependedonbyothers.md)
  Indicates whether other samples depend on this sample for decoding (type `CFBoolean`).
- [let kCMSampleAttachmentKey_DisplayImmediately: CFString](kcmsampleattachmentkey_displayimmediately.md)
  Indicates whether the sample should be displayed immediately (type `CFBoolean`, default false).
- [let kCMSampleAttachmentKey_DoNotDisplay: CFString](kcmsampleattachmentkey_donotdisplay.md)
  Indicates whether the sample should be decoded but not displayed (type `CFBoolean`, default false).
- [let kCMSampleAttachmentKey_EarlierDisplayTimesAllowed: CFString](kcmsampleattachmentkey_earlierdisplaytimesallowed.md)
  Indicates whether later samples may have earlier display times (type `CFBoolean`).
- [let kCMSampleAttachmentKey_HasRedundantCoding: CFString](kcmsampleattachmentkey_hasredundantcoding.md)
  Indicates whether the sample has redundant coding (type `CFBoolean`).
- [let kCMSampleAttachmentKey_PostDecodeProcessingMetadata: CFString](kcmsampleattachmentkey_postdecodeprocessingmetadata.md)
### Sample Buffer Keys
- [let kCMSampleBufferAttachmentKey_DisplayEmptyMediaImmediately: CFString](kcmsamplebufferattachmentkey_displayemptymediaimmediately.md)
  Tells that the empty marker should be dequeued immediately regardless of its timestamp (type `CFBoolean`, default false).
- [let kCMSampleBufferAttachmentKey_DrainAfterDecoding: CFString](kcmsamplebufferattachmentkey_drainafterdecoding.md)
  Indicates whether the sample buffer should be drained after decoding type `CFBoolean`, default false).
- [let kCMSampleBufferAttachmentKey_DroppedFrameReason: CFString](kcmsamplebufferattachmentkey_droppedframereason.md)
  Indicates the reason the current video frame was dropped (type `CFString`).
- [let kCMSampleBufferDroppedFrameReason_FrameWasLate: CFString](kcmsamplebufferdroppedframereason_framewaslate.md)
  The frame was dropped because it was late.
- [let kCMSampleBufferDroppedFrameReason_OutOfBuffers: CFString](kcmsamplebufferdroppedframereason_outofbuffers.md)
  The frame was dropped because the module providing frames is out of buffers.
- [let kCMSampleBufferDroppedFrameReason_Discontinuity: CFString](kcmsamplebufferdroppedframereason_discontinuity.md)
  An unknown number of frames were dropped.
- [let kCMSampleBufferAttachmentKey_DroppedFrameReasonInfo: CFString](kcmsamplebufferattachmentkey_droppedframereasoninfo.md)
  Indicates additional information regarding the dropped video frame (type `CFString`).
- [let kCMSampleBufferDroppedFrameReasonInfo_CameraModeSwitch: CFString](kcmsamplebufferdroppedframereasoninfo_cameramodeswitch.md)
  A discontinuity was caused by a camera mode switch.
- [let kCMSampleBufferAttachmentKey_EmptyMedia: CFString](kcmsamplebufferattachmentkey_emptymedia.md)
  Marks an intentionally empty interval in the sequence of samples (type `CFBoolean`, default false).
- [let kCMSampleBufferAttachmentKey_EndsPreviousSampleDuration: CFString](kcmsamplebufferattachmentkey_endsprevioussampleduration.md)
  Indicates that sample buffer’s decode timestamp may be used to define the previous sample buffer’s duration (type `CFBoolean`, default false).
- [let kCMSampleBufferAttachmentKey_FillDiscontinuitiesWithSilence: CFString](kcmsamplebufferattachmentkey_filldiscontinuitieswithsilence.md)
  Fill the difference between discontiguous sample buffers with silence (type `CFBoolean`, default false).
- [let kCMSampleBufferAttachmentKey_ForceKeyFrame: CFString](kcmsamplebufferattachmentkey_forcekeyframe.md)
  Indicates that the current or next video sample buffer should be forced to be encoded as a key frame.
- [let kCMSampleBufferAttachmentKey_GradualDecoderRefresh: CFString](kcmsamplebufferattachmentkey_gradualdecoderrefresh.md)
  Indicates the decoder refresh count (type `CFNumber`).
- [let kCMSampleBufferAttachmentKey_PermanentEmptyMedia: CFString](kcmsamplebufferattachmentkey_permanentemptymedia.md)
  Marks the end of the sequence of samples (type `CFBoolean`, default false).
- [let kCMSampleBufferAttachmentKey_PostNotificationWhenConsumed: CFString](kcmsamplebufferattachmentkey_postnotificationwhenconsumed.md)
  If present, indicates that decode pipelines should post a notification when consuming the sample buffer(type `CFDictionary`).
- [let kCMSampleBufferAttachmentKey_ResetDecoderBeforeDecoding: CFString](kcmsamplebufferattachmentkey_resetdecoderbeforedecoding.md)
  Indicates whether the sample buffer should be reset before decoding (type `CFBoolean`, default false).
- [let kCMSampleBufferAttachmentKey_ResumeOutput: CFString](kcmsamplebufferattachmentkey_resumeoutput.md)
  If present, indicates that output should be resumed following a discontinuity `CFBoolean`, default false).
- [let kCMSampleBufferAttachmentKey_Reverse: CFString](kcmsamplebufferattachmentkey_reverse.md)
  Indicates that the decoded contents of the sample buffer should be reversed (type `CFBoolean`, default false).
- [let kCMSampleBufferAttachmentKey_SampleReferenceByteOffset: CFString](kcmsamplebufferattachmentkey_samplereferencebyteoffset.md)
  Indicates the byte offset at which the sample data begins (type `CFNumber`).
- [let kCMSampleBufferAttachmentKey_SampleReferenceURL: CFString](kcmsamplebufferattachmentkey_samplereferenceurl.md)
  Indicates the URL where the sample data is (type `CFURL`).
- [let kCMSampleBufferAttachmentKey_SpeedMultiplier: CFString](kcmsamplebufferattachmentkey_speedmultiplier.md)
  The factor by which the sample buffer’s presentation should be accelerated (type `CFNumber`, default 1.0).
- [let kCMSampleBufferAttachmentKey_StillImageLensStabilizationInfo: CFString](kcmsamplebufferattachmentkey_stillimagelensstabilizationinfo.md)
  Indicates information about the lens stabilization applied to the current still image buffer.
- [let kCMSampleBufferLensStabilizationInfo_Active: CFString](kcmsamplebufferlensstabilizationinfo_active.md)
  The lens stabilization module was active for the duration this buffer.
- [let kCMSampleBufferLensStabilizationInfo_OutOfRange: CFString](kcmsamplebufferlensstabilizationinfo_outofrange.md)
  The motion of the device or duration of the capture was outside of what the stabilization mechanism could support.
- [let kCMSampleBufferLensStabilizationInfo_Unavailable: CFString](kcmsamplebufferlensstabilizationinfo_unavailable.md)
  The lens stabilization module was unavailable for use.
- [let kCMSampleBufferLensStabilizationInfo_Off: CFString](kcmsamplebufferlensstabilizationinfo_off.md)
  The lens stabilization module was not used during this capture.
- [let kCMSampleBufferAttachmentKey_TransitionID: CFString](kcmsamplebufferattachmentkey_transitionid.md)
  Marks a transition from one source of buffers to another.
- [let kCMSampleBufferAttachmentKey_TrimDurationAtEnd: CFString](kcmsamplebufferattachmentkey_trimdurationatend.md)
  The duration that should be removed at the end of the sample buffer, after decoding.
- [let kCMSampleBufferAttachmentKey_TrimDurationAtStart: CFString](kcmsamplebufferattachmentkey_trimdurationatstart.md)
  The duration that should be removed at the beginning of the sample buffer, after decoding.

## See Also

- [func CMSampleBufferGetSampleAttachmentsArray(CMSampleBuffer, createIfNecessary: Bool) -> CFArray?](cmsamplebuffergetsampleattachmentsarray(_:createifnecessary:).md)
  Retrieves an array of sample attachment dictionaries that represents each sample in a sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/sample-attachment-keys)*