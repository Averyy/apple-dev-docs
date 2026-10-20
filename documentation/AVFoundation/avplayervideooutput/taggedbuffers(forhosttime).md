# taggedBuffers(forHostTime:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 17.2+ - Deprecated in 27.0
- iPadOS 17.2+ - Deprecated in 27.0
- Mac Catalyst 17.2+ - Deprecated in 27.0
- macOS 14.2+ - Deprecated in 27.0
- tvOS 17.2+ - Deprecated in 27.0
- visionOS 1.1+ - Deprecated in 27.0
- watchOS 10.2+ - Deprecated in 27.0

> **Deprecated**: Use AVPlayerVideoOutput.sample instead

## Declaration

```swift
func taggedBuffers(forHostTime hostTime: CMTime) -> (taggedBufferGroup: [CMTaggedBuffer], presentationTime: CMTime, activeConfiguration: AVPlayerVideoOutput.Configuration)?
```

## See Also

### Accessing video data
- [func sample(forHostTime: CMTime) -> AVPlayerVideoOutput.Sample?](./sample%28forhosttime%29.md)
  Retrieves a video sample along with auxiliary information for display at the specified host time.
- [AVPlayerVideoOutput.Sample](./sample.md)
  A video frame along with auxiliary information for display at the specified presentation time.
- [AVPlayerVideoOutput.Configuration](./configuration.md)
  An object that provides configuration information for the related player item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayervideooutput/taggedbuffers(forhosttime:))*