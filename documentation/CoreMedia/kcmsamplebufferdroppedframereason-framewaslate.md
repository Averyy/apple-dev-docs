# kCMSampleBufferDroppedFrameReason_FrameWasLate

**Framework**: Core Media  
**Kind**: var

The frame was dropped because it was late.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let kCMSampleBufferDroppedFrameReason_FrameWasLate: CFString
```

#### Discussion

A video capture client has indicated         that late video frames should be dropped and the current frame is late.  This condition is typically        caused by the client’s processing taking too long.

## See Also

- [let kCMSampleBufferAttachmentKey_DisplayEmptyMediaImmediately: CFString](kcmsamplebufferattachmentkey_displayemptymediaimmediately.md)
  Tells that the empty marker should be dequeued immediately regardless of its timestamp (type `CFBoolean`, default false).
- [let kCMSampleBufferAttachmentKey_DrainAfterDecoding: CFString](kcmsamplebufferattachmentkey_drainafterdecoding.md)
  Indicates whether the sample buffer should be drained after decoding type `CFBoolean`, default false).
- [let kCMSampleBufferAttachmentKey_DroppedFrameReason: CFString](kcmsamplebufferattachmentkey_droppedframereason.md)
  Indicates the reason the current video frame was dropped (type `CFString`).
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmsamplebufferdroppedframereason_framewaslate)*