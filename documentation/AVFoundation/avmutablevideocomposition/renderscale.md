# renderScale

**Framework**: AVFoundation  
**Kind**: property

The scale at which the video composition should render.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var renderScale: Float { get set }
```

#### Discussion

May only be other than `1.0` for a video composition set on an [`AVPlayerItem`](avplayeritem.md).

## See Also

- [var frameDuration: CMTime](avmutablevideocomposition/frameduration.md)
  A time interval for which the video composition should render composed video frames.
- [var renderSize: CGSize](avmutablevideocomposition/rendersize.md)
  The size at which the video composition should render.
- [var animationTool: AVVideoCompositionCoreAnimationTool?](avmutablevideocomposition/animationtool.md)
  A video composition tool to use with Core Animation in offline rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/renderscale)*