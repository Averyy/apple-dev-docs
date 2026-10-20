# taggedBuffers

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of CMTaggedBuffers containing the frame for the specified time.

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
let taggedBuffers: [CMTaggedDynamicBuffer]
```

## See Also

### Inspecting a sample
- [let activeConfiguration: AVPlayerVideoOutput.Configuration](./activeconfiguration.md)
  The active configuration that this sample was derived from.
- [let presentationTime: CMTime](./presentationtime.md)
  A CMTime representing the true display deadline for this sample in terms of the corresponding AVPlayerItem’s timebase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayervideooutput/sample/taggedbuffers)*