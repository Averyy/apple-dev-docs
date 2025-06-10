# videoRenderer

**Framework**: RealityKit  
**Kind**: property

The component’s video renderer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var videoRenderer: AVSampleBufferVideoRenderer? { get }
```

#### Discussion

Pass this renderer to the component as a parameter in the initializer; you can’t replace it afterward. You can’t use the same `AVSampleBufferVideoRenderer` object with more than one `VideoPlayerComponent`.

## See Also

- [var avPlayer: AVPlayer?](videoplayercomponent/avplayer.md)
  The AV player that the component plays.
- [var playerScreenSize: SIMD2<Float>](videoplayercomponent/playerscreensize.md)
  The screen entity size of the current video player in meters.
- [var screenVideoDimension: SIMD2<Float>](videoplayercomponent/screenvideodimension.md)
  The video resolution size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videoplayercomponent/videorenderer)*