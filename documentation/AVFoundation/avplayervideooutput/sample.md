# AVPlayerVideoOutput.Sample

**Framework**: AVFoundation  
**Kind**: struct

A video frame along with auxiliary information for display at the specified presentation time.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct Sample
```

## Topics

### Instance Properties
- [let activeConfiguration: AVPlayerVideoOutput.Configuration](avplayervideooutput/sample/activeconfiguration.md)
  The active configuration that this sample was derived from.
- [let presentationTime: CMTime](avplayervideooutput/sample/presentationtime.md)
  A CMTime representing the true display deadline for this sample in terms of the corresponding AVPlayerItem’s timebase.
- [let taggedBuffers: [CMTaggedDynamicBuffer]](avplayervideooutput/sample/taggedbuffers.md)
  An array of CMTaggedBuffers containing the frame for the specified time.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayervideooutput/sample)*