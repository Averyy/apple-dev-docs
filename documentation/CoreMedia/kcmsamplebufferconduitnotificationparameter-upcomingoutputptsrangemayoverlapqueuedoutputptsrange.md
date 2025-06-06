# kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange

**Framework**: Core Media  
**Kind**: var

Indicates that the presentation timestamps of upcoming output samples may overlap those of samples queued for output (type `CFBoolean`).

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange: CFString
```

#### Discussion

This key is always present in the `userInfo` dictionary for the [`kCMSampleBufferConduitNotification_UpcomingOutputPTSRangeChanged`](kcmsamplebufferconduitnotification_upcomingoutputptsrangechanged.md) notification. If its value is [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue), there is a possibility that upcoming frames may have earlier presentation timestamps than the frames previously provided to the conduit, and the dictionary also contains one or both of the [`kCMSampleBufferConduitNotificationParameter_MinUpcomingOutputPTS`](kcmsamplebufferconduitnotificationparameter_minupcomingoutputpts.md) or [`kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS`](kcmsamplebufferconduitnotificationparameter_maxupcomingoutputpts.md) keys providing further information. If its value is [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse), there is no such possibility.

## See Also

- [let kCMSampleBufferConduitNotification_ResetOutput: CFString](kcmsamplebufferconduitnotification_resetoutput.md)
  Posted on a conduit of sample buffers to request invalidation of pending output data.
- [let kCMSampleBufferConduitNotification_InhibitOutputUntil: CFString](kcmsamplebufferconduitnotification_inhibitoutputuntil.md)
  Posted on a conduit of sample buffers to announce a coming discontinuity.
- [let kCMSampleBufferConduitNotification_UpcomingOutputPTSRangeChanged: CFString](kcmsamplebufferconduitnotification_upcomingoutputptsrangechanged.md)
  Posted on a conduit of video sample buffers to report information about the range of upcoming output presentation timestamps.
- [let kCMSampleBufferConduitNotificationParameter_MinUpcomingOutputPTS: CFString](kcmsamplebufferconduitnotificationparameter_minupcomingoutputpts.md)
  Specifies the minimum presentation timestamp of upcoming output samples (type `CFDictionary`).
- [let kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS: CFString](kcmsamplebufferconduitnotificationparameter_maxupcomingoutputpts.md)
  Specifies the maximum presentation timestamp of upcoming output samples (type `CFDictionary`).
- [let kCMSampleBufferConduitNotificationParameter_ResumeTag: CFString](kcmsamplebufferconduitnotificationparameter_resumetag.md)
  Specifies a tag to be attached to the first sample buffer following a discontinuity (type `CFNumber`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconduitnotificationparameter_upcomingoutputptsrangemayoverlapqueuedoutputptsrange)*