# Sample Buffer Notifications

**Framework**: Core Media

Notifications the system posts when processing sample buffer objects.

## Topics

### Sample Buffer Notifications
- [let kCMSampleBufferNotification_DataBecameReady: CFString](kcmsamplebuffernotification_databecameready.md)
  Posted on a sample buffer by the [`CMSampleBufferSetDataReady(_:)`](cmsamplebuffersetdataready(_:).md) function when the buffer becomes ready.
- [let kCMSampleBufferNotification_DataFailed: CFString](kcmsamplebuffernotification_datafailed.md)
- [let kCMSampleBufferNotificationParameter_OSStatus: CFString](kcmsamplebuffernotificationparameter_osstatus.md)
- [let kCMSampleBufferConsumerNotification_BufferConsumed: CFString](kcmsamplebufferconsumernotification_bufferconsumed.md)
  Optionally posted when a sample buffer is consumed.
### Sample Buffer Conduit Notifications
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
- [let kCMSampleBufferConduitNotificationParameter_ResumeTag: CFString](kcmsamplebufferconduitnotificationparameter_resumetag.md)
  Specifies a tag to be attached to the first sample buffer following a discontinuity (type `CFNumber`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/sample-buffer-notifications)*