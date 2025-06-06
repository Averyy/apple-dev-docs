# screenVideoDimension

**Framework**: RealityKit  
**Kind**: property

The video resolution size.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var screenVideoDimension: SIMD2<Float> { get }
```

#### Discussion

This property has the format `[width, height]`, for example, `[1920, 1080]`.

## See Also

- [var avPlayer: AVPlayer?](videoplayercomponent/avplayer.md)
  The AV player that the component plays.
- [var playerScreenSize: SIMD2<Float>](videoplayercomponent/playerscreensize.md)
  The screen entity size of the current video player in meters.
- [var videoRenderer: AVSampleBufferVideoRenderer?](videoplayercomponent/videorenderer.md)
  The component’s video renderer.
- [var viewingMode: VideoPlaybackController.ViewingMode?](videoplayercomponent/viewingmode.md)
  The current content-viewing mode for video playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videoplayercomponent/screenvideodimension)*