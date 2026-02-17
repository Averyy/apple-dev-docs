# CTSlicingManager.TrafficClass.video

**Framework**: Core Telephony  
**Kind**: case

A traffic class for video data transmission.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
case video
```

#### Discussion

The video traffic class provides quality-of-service characteristics suitable for video content delivery, balancing bandwidth needs with acceptable latency levels.

## See Also

- [CTSlicingManager.TrafficClass.any](ctslicingmanager/trafficclass/any.md)
  A traffic class for general-purpose network traffic without specific QoS requirements.
- [CTSlicingManager.TrafficClass.background](ctslicingmanager/trafficclass/background.md)
  A traffic class for non-urgent background data transfers.
- [CTSlicingManager.TrafficClass.responsiveData](ctslicingmanager/trafficclass/responsivedata.md)
  A traffic class for interactive data that requires quick response times.
- [CTSlicingManager.TrafficClass.avStreaming](ctslicingmanager/trafficclass/avstreaming.md)
  A traffic class for audio and video streaming.
- [CTSlicingManager.TrafficClass.responsiveAV](ctslicingmanager/trafficclass/responsiveav.md)
  A traffic class for real-time audio and video communication.
- [CTSlicingManager.TrafficClass.voice](ctslicingmanager/trafficclass/voice.md)
  A traffic class for voice communication with highest priority and lowest latency.
- [CTSlicingManager.TrafficClass.signaling](ctslicingmanager/trafficclass/signaling.md)
  A traffic class for network signaling and control messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/trafficclass/video)*