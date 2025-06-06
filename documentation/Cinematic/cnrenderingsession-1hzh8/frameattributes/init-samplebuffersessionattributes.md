# init(sampleBuffer:sessionAttributes:)

**Framework**: Cinematic  
**Kind**: init

Creates a structure representing a Cinematic rendering session based a sample buffer and session attributes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
init?(sampleBuffer: CMSampleBuffer, sessionAttributes: CNRenderingSession.Attributes)
```

## Parameters

- `sampleBuffer`: A sample buffer read from the timed Cinematic metadata track of a cinematic asset.
- `sessionAttributes`: Rendering session attributes loaded from a Cinematic asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnrenderingsession-1hzh8/frameattributes/init(samplebuffer:sessionattributes:))*