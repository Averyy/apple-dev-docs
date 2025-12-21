# taggedBuffers(forHostTime:)

**Framework**: AVFoundation  
**Kind**: method

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst ?+
- macOS 14.2+
- tvOS 17.2+
- visionOS 1.1+
- watchOS 10.2+

## Declaration

```swift
func taggedBuffers(forHostTime hostTime: CMTime) -> (taggedBufferGroup: [CMTaggedBuffer], presentationTime: CMTime, activeConfiguration: AVPlayerVideoOutput.Configuration)?
```

## See Also

- [func sample(forHostTime: CMTime) -> AVPlayerVideoOutput.Sample?](avplayervideooutput/sample(forhosttime:).md)
  Retrieves a video sample along with auxiliary information for display at the specified host time.
- [AVPlayerVideoOutput.Sample](avplayervideooutput/sample.md)
  A video frame along with auxiliary information for display at the specified presentation time.
- [AVPlayerVideoOutput.Configuration](avplayervideooutput/configuration.md)
  An object that provides configuration information for the related player item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayervideooutput/taggedbuffers(forhosttime:))*