# CTSlicingManager.TrafficClass

**Framework**: Core Telephony  
**Kind**: enum  
**Role**: Enumeration

Quality-of-service classes for routing network traffic.

**Availability**:
- iOS 26.3+
- iPadOS 26.3+
- Mac Catalyst 26.3+

## Declaration

```swift
enum TrafficClass
```

## Discussion

The `TrafficClass` enumeration represents different quality-of-service (QoS) levels that the network uses to prioritize and route traffic. Each traffic class has specific characteristics optimized for different types of network communication.

The system automatically assigns traffic classes based on the active network slice and the type of transmitted traffic.

## Topics

### Traffic classes
- [CTSlicingManager.TrafficClass.any](./trafficclass/any.md)
  A traffic class for general-purpose network traffic without specific QoS requirements.
- [CTSlicingManager.TrafficClass.background](./trafficclass/background.md)
  A traffic class for non-urgent background data transfers.
- [CTSlicingManager.TrafficClass.responsiveData](./trafficclass/responsivedata.md)
  A traffic class for interactive data that requires quick response times.
- [CTSlicingManager.TrafficClass.avStreaming](./trafficclass/avstreaming.md)
  A traffic class for audio and video streaming.
- [CTSlicingManager.TrafficClass.responsiveAV](./trafficclass/responsiveav.md)
  A traffic class for real-time audio and video communication.
- [CTSlicingManager.TrafficClass.video](./trafficclass/video.md)
  A traffic class for video data transmission.
- [CTSlicingManager.TrafficClass.voice](./trafficclass/voice.md)
  A traffic class for voice communication with highest priority and lowest latency.
- [CTSlicingManager.TrafficClass.signaling](./trafficclass/signaling.md)
  A traffic class for network signaling and control messages.
### Traffic class information
- [var description: String](./trafficclass/description.md)
  A string representation of the traffic class.

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctslicingmanager/trafficclass)*