# desiredSpatialVideoMode

**Framework**: RealityKit  
**Kind**: property

The viewer’s selected spatial video rendering mode.

**Availability**:
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var desiredSpatialVideoMode: VideoPlayerComponent.SpatialVideoMode { get set }
```

#### Discussion

This is the desired spatial video rendering mode that will be attempted if the content is able to support the requested mode. If the content is not spatial video then the rendering of the video will default back to screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videoplayercomponent/desiredspatialvideomode)*