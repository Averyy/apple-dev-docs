# kCMSampleBufferAttachmentKey_SpeedMultiplier

**Framework**: Core Media  
**Kind**: var

The factor by which the sample buffer’s presentation should be accelerated (type `CFNumber`, default 1.0).

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let kCMSampleBufferAttachmentKey_SpeedMultiplier: CFString
```

#### Discussion

For normal playback the speed multiplier would be `1.0` (which is used if this attachment is not present);         for double-speed playback the speed multiplier would be `2.0`, which would halve the output duration.        Speed-multiplication factors take effect after trimming; see [`CMSampleBufferGetOutputDuration(_:)`](cmsamplebuffergetoutputduration(_:).md).        Note that this attachment principally provides information about the duration-stretching effect:        by default, it should be implemented by rate conversion, but other attachments may specify richer         stretching operations—for example, scaling without pitch shift, or pitch shift without changing duration.        Sequences of speed-multiplied sample buffers should have explicit time stamps        to clarify when each should be output (see [`CMSampleBufferSetOutputPresentationTimeStamp(_:newValue:)`](cmsamplebuffersetoutputpresentationtimestamp(_:newvalue:).md)).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmsamplebufferattachmentkey_speedmultiplier)*