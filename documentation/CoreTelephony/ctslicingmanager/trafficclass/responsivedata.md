# CTSlicingManager.TrafficClass.responsiveData

**Framework**: Core Telephony  
**Kind**: case

A traffic class for interactive data that requires quick response times.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
case responsiveData
```

#### Discussion

The responsive data traffic class optimizes for requests that people initiate and that benefit from low latency, such as web browsing, API calls, and interactive app features.

## See Also

- [CTSlicingManager.TrafficClass.any](ctslicingmanager/trafficclass/any.md)
  A traffic class for general-purpose network traffic without specific QoS requirements.
- [CTSlicingManager.TrafficClass.background](ctslicingmanager/trafficclass/background.md)
  A traffic class for non-urgent background data transfers.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/trafficclass/responsivedata)*