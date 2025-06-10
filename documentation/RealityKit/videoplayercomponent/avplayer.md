# avPlayer

**Framework**: RealityKit  
**Kind**: property

The AV player that the component plays.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
var avPlayer: AVPlayer? { get }
```

#### Discussion

Pass this player to the component as a parameter in the initializer; you can’t replace it afterward.

## See Also

- [var playerScreenSize: SIMD2<Float>](videoplayercomponent/playerscreensize.md)
  The screen entity size of the current video player in meters.
- [var screenVideoDimension: SIMD2<Float>](videoplayercomponent/screenvideodimension.md)
  The video resolution size.
- [var videoRenderer: AVSampleBufferVideoRenderer?](videoplayercomponent/videorenderer.md)
  The component’s video renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videoplayercomponent/avplayer)*