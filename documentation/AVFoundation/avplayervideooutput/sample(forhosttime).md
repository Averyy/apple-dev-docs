# sample(forHostTime:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Retrieves a video sample along with auxiliary information for display at the specified host time.

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
func sample(forHostTime hostTime: CMTime) -> AVPlayerVideoOutput.Sample?
```

#### Return Value

A sample containing the frame, presentation timestamp, and active configuration for the specified host time, or nil if no sample was available for that host time.

## Parameters

- `hostTime`: A CMTime that expresses a desired host time.

## See Also

### Accessing video data
- [AVPlayerVideoOutput.Sample](./sample.md)
  A video frame along with auxiliary information for display at the specified presentation time.
- [func taggedBuffers(forHostTime: CMTime) -> (taggedBufferGroup: [CMTaggedBuffer], presentationTime: CMTime, activeConfiguration: AVPlayerVideoOutput.Configuration)?](./taggedbuffers%28forhosttime%29.md)
- [AVPlayerVideoOutput.Configuration](./configuration.md)
  An object that provides configuration information for the related player item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayervideooutput/sample(forhosttime:))*