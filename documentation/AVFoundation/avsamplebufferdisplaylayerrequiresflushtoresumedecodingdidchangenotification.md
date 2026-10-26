# AVSampleBufferDisplayLayerRequiresFlushToResumeDecodingDidChangeNotification

**Framework**: AVFoundation  
**Kind**: var  
**Role**: Global Variable

A notification the system posts when a sample buffer display layer changes its decoding requirements.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```c
extern NSNotificationName const AVSampleBufferDisplayLayerRequiresFlushToResumeDecodingDidChangeNotification;
```

## See Also

### Notifications
- [AVSampleBufferAudioRendererOutputConfigurationDidChangeNotification](./avsamplebufferaudiorendereroutputconfigurationdidchangenotification.md)
  A notification that indicates the hardware configuration does not match the enqueued data format.
- [AVSampleBufferAudioRendererWasFlushedAutomaticallyNotification](./avsamplebufferaudiorendererwasflushedautomaticallynotification.md)
  A notification that fires whenever the receiver’s enqueued media data has been flushed for a reason other than a call to the -flush method.
- [AVSampleBufferDisplayLayerOutputObscuredDueToInsufficientExternalProtectionDidChangeNotification](./avsamplebufferdisplaylayeroutputobscuredduetoinsufficientexternalprotectiondidchangenotification.md)
- [AVSampleBufferDisplayLayerReadyForDisplayDidChangeNotification](./avsamplebufferdisplaylayerreadyfordisplaydidchangenotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayerrequiresflushtoresumedecodingdidchangenotification)*