# CTSlicingManager.TrafficClass.background

**Framework**: Core Telephony  
**Kind**: case

A traffic class for non-urgent background data transfers.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
case background
```

#### Discussion

Use the background traffic class for data that doesn’t require immediate delivery, such as backups, synchronization, and content prefetching. This traffic has lower priority and may experience higher latency.

## See Also

- [CTSlicingManager.TrafficClass.any](ctslicingmanager/trafficclass/any.md)
  A traffic class for general-purpose network traffic without specific QoS requirements.
- [CTSlicingManager.TrafficClass.responsiveData](ctslicingmanager/trafficclass/responsivedata.md)
  A traffic class for interactive data that requires quick response times.
- [CTSlicingManager.TrafficClass.avStreaming](ctslicingmanager/trafficclass/avstreaming.md)
  A traffic class for audio and video streaming.
- [CTSlicingManager.TrafficClass.responsiveAV](ctslicingmanager/trafficclass/responsiveav.md)
  A traffic class for real-time audio and video communication.
- [CTSlicingManager.TrafficClass.video](ctslicingmanager/trafficclass/video.md)
  A traffic class for video data transmission.
- [CTSlicingManager.TrafficClass.voice](ctslicingmanager/trafficclass/voice.md)
  A traffic class for voice communication with highest priority and lowest latency.
- [CTSlicingManager.TrafficClass.signaling](ctslicingmanager/trafficclass/signaling.md)
  A traffic class for network signaling and control messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/trafficclass/background)*