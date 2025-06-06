# kCMSampleBufferConduitNotificationParameter_ResumeTag

**Framework**: Core Media  
**Kind**: var

Specifies a tag to be attached to the first sample buffer following a discontinuity (type `CFNumber`).

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
let kCMSampleBufferConduitNotificationParameter_ResumeTag: CFString
```

#### Discussion

A conduit of sample buffers posts the [`kCMSampleBufferConduitNotification_InhibitOutputUntil`](kcmsamplebufferconduitnotification_inhibitoutputuntil.md) notification when a discontinuity in decoding occurs. The value for this key will be attached to the first sample buffer following the discontinuity using the [`kCMSampleBufferAttachmentKey_ResumeOutput`](kcmsamplebufferattachmentkey_resumeoutput.md) attachment, indicating that clients should resume output.

## See Also

- [let kCMSampleBufferConduitNotification_ResetOutput: CFString](kcmsamplebufferconduitnotification_resetoutput.md)
  Posted on a conduit of sample buffers to request invalidation of pending output data.
- [let kCMSampleBufferConduitNotification_InhibitOutputUntil: CFString](kcmsamplebufferconduitnotification_inhibitoutputuntil.md)
  Posted on a conduit of sample buffers to announce a coming discontinuity.
- [let kCMSampleBufferConduitNotification_UpcomingOutputPTSRangeChanged: CFString](kcmsamplebufferconduitnotification_upcomingoutputptsrangechanged.md)
  Posted on a conduit of video sample buffers to report information about the range of upcoming output presentation timestamps.
- [let kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange: CFString](kcmsamplebufferconduitnotificationparameter_upcomingoutputptsrangemayoverlapqueuedoutputptsrange.md)
  Indicates that the presentation timestamps of upcoming output samples may overlap those of samples queued for output (type `CFBoolean`).
- [let kCMSampleBufferConduitNotificationParameter_MinUpcomingOutputPTS: CFString](kcmsamplebufferconduitnotificationparameter_minupcomingoutputpts.md)
  Specifies the minimum presentation timestamp of upcoming output samples (type `CFDictionary`).
- [let kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS: CFString](kcmsamplebufferconduitnotificationparameter_maxupcomingoutputpts.md)
  Specifies the maximum presentation timestamp of upcoming output samples (type `CFDictionary`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconduitnotificationparameter_resumetag)*