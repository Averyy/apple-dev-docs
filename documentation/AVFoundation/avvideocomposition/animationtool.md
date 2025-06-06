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
var animationTool: AVVideoCompositionCoreAnimationTool? { get }
```

#### Discussion

This attribute may be `nil`. Set an animation tool if you’re using the composition in conjunction with [`AVAssetExportSession`](avassetexportsession.md) for offline rendering, rather than with [`AVPlayer`](avplayer.md).

## See Also

- [var renderSize: CGSize](avvideocomposition/rendersize.md)
  The size at which the video composition should render.
- [var renderScale: Float](avvideocomposition/renderscale.md)
  The scale at which the video composition should render.
- [var frameDuration: CMTime](avvideocomposition/frameduration.md)
  A time interval for which the video composition should render composed video frames.
- [var colorPrimaries: String?](avvideocomposition/colorprimaries.md)
  The color primaries used for video composition.
- [var colorTransferFunction: String?](avvideocomposition/colortransferfunction.md)
  The transfer function used for video composition.
- [var colorYCbCrMatrix: String?](avvideocomposition/colorycbcrmatrix.md)
  The YCbCr matrix used for video composition.
- [var customVideoCompositorClass: (any AVVideoCompositing.Type)?](avvideocomposition/customvideocompositorclass.md)
  A custom compositor class to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocomposition/animationtool)*