# animationTool

**Framework**: AVFoundation  
**Kind**: property

A video composition tool to use with Core Animation in offline rendering.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var animationTool: AVVideoCompositionCoreAnimationTool? { get set }
```

#### Discussion

This attribute may be `nil`. Set an animation tool if you are using the composition in conjunction with [`AVAssetExportSession`](avassetexportsession.md) for offline rendering, rather than with [`AVPlayer`](avplayer.md).

## See Also

- [var frameDuration: CMTime](avmutablevideocomposition/frameduration.md)
  A time interval for which the video composition should render composed video frames.
- [var renderSize: CGSize](avmutablevideocomposition/rendersize.md)
  The size at which the video composition should render.
- [var renderScale: Float](avmutablevideocomposition/renderscale.md)
  The scale at which the video composition should render.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/animationtool)*