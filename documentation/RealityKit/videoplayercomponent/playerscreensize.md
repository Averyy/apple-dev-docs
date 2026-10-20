# playerScreenSize

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The screen entity size of the current video player in meters.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var playerScreenSize: SIMD2<Float> { get }
```

#### Discussion

This property has the format `[width, height]`.

## See Also

### Accessing video player properties
- [var avPlayer: AVPlayer?](./avplayer.md)
  The AV player that the component plays.
- [var screenVideoDimension: SIMD2<Float>](./screenvideodimension.md)
  The video resolution size.
- [var videoRenderer: AVSampleBufferVideoRenderer?](./videorenderer.md)
  The component’s video renderer.
- [var viewingMode: VideoPlaybackController.ViewingMode?](./viewingmode.md)
  The current content-viewing mode for video playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videoplayercomponent/playerscreensize)*