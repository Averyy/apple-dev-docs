# kCMSampleBufferConduitNotification_UpcomingOutputPTSRangeChanged

**Framework**: Core Media  
**Kind**: var

Posted on a conduit of video sample buffers to report information about the range of upcoming output presentation timestamps.

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
let kCMSampleBufferConduitNotification_UpcomingOutputPTSRangeChanged: CFString
```

#### Discussion

This information can be important for frame-reordered video and for certain types of decoding where samples are transmitted in a different order from the order they will be displayed. If you need to process frames in presentation order, you can use this information to ensure that you do not process a frame too early (that is, when there are upcoming frames that will have earlier presentation timestamps than a frame to be processed).

The `userInfo` dictionary for this notification contains the [`kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange`](kcmsamplebufferconduitnotificationparameter_upcomingoutputptsrangemayoverlapqueuedoutputptsrange.md) key. If the value for that key is [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue), the dictionary also contains one or both of the [`kCMSampleBufferConduitNotificationParameter_MinUpcomingOutputPTS`](kcmsamplebufferconduitnotificationparameter_minupcomingoutputpts.md) or [`kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS`](kcmsamplebufferconduitnotificationparameter_maxupcomingoutputpts.md) keys providing information about the range of overlapping presentation timestamps.

## See Also

- [let kCMSampleBufferConduitNotification_ResetOutput: CFString](kcmsamplebufferconduitnotification_resetoutput.md)
  Posted on a conduit of sample buffers to request invalidation of pending output data.
- [let kCMSampleBufferConduitNotification_InhibitOutputUntil: CFString](kcmsamplebufferconduitnotification_inhibitoutputuntil.md)
  Posted on a conduit of sample buffers to announce a coming discontinuity.
- [let kCMSampleBufferConduitNotificationParameter_UpcomingOutputPTSRangeMayOverlapQueuedOutputPTSRange: CFString](kcmsamplebufferconduitnotificationparameter_upcomingoutputptsrangemayoverlapqueuedoutputptsrange.md)
  Indicates that the presentation timestamps of upcoming output samples may overlap those of samples queued for output (type `CFBoolean`).
- [let kCMSampleBufferConduitNotificationParameter_MinUpcomingOutputPTS: CFString](kcmsamplebufferconduitnotificationparameter_minupcomingoutputpts.md)
  Specifies the minimum presentation timestamp of upcoming output samples (type `CFDictionary`).
- [let kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS: CFString](kcmsamplebufferconduitnotificationparameter_maxupcomingoutputpts.md)
  Specifies the maximum presentation timestamp of upcoming output samples (type `CFDictionary`).
- [let kCMSampleBufferConduitNotificationParameter_ResumeTag: CFString](kcmsamplebufferconduitnotificationparameter_resumetag.md)
  Specifies a tag to be attached to the first sample buffer following a discontinuity (type `CFNumber`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconduitnotification_upcomingoutputptsrangechanged)*