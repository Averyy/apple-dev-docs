# AVPlayerVideoOutput.Sample

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A video frame along with auxiliary information for display at the specified presentation time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct Sample
```

## Topics

### Inspecting a sample
- [let activeConfiguration: AVPlayerVideoOutput.Configuration](./sample/activeconfiguration.md)
  The active configuration that this sample was derived from.
- [let presentationTime: CMTime](./sample/presentationtime.md)
  A CMTime representing the true display deadline for this sample in terms of the corresponding AVPlayerItem’s timebase.
- [let taggedBuffers: [CMTaggedDynamicBuffer]](./sample/taggedbuffers.md)
  An array of CMTaggedBuffers containing the frame for the specified time.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing video data
- [func sample(forHostTime: CMTime) -> AVPlayerVideoOutput.Sample?](./sample%28forhosttime%29.md)
  Retrieves a video sample along with auxiliary information for display at the specified host time.
- [func taggedBuffers(forHostTime: CMTime) -> (taggedBufferGroup: [CMTaggedBuffer], presentationTime: CMTime, activeConfiguration: AVPlayerVideoOutput.Configuration)?](./taggedbuffers%28forhosttime%29.md)
- [AVPlayerVideoOutput.Configuration](./configuration.md)
  An object that provides configuration information for the related player item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayervideooutput/sample)*