# animationTool

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A video composition tool to use with Core Animation in offline rendering.

**Availability**:
- iOS 4.0+ - Deprecated in 26.0
- iPadOS 4.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.7+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use AVVideoComposition.Configuration instead

## Declaration

```swift
var animationTool: AVVideoCompositionCoreAnimationTool? { get set }
```

```objc
@property (nonatomic, retain, nullable) AVVideoCompositionCoreAnimationTool * animationTool;
```

## Discussion

This attribute may be `nil`. Set an animation tool if you are using the composition in conjunction with [`AVAssetExportSession`](../avassetexportsession.md) for offline rendering, rather than with [`AVPlayer`](../avplayer.md).

## See Also

### Configuring video composition properties
- [var frameDuration: CMTime](./frameduration.md)
  A time interval for which the video composition should render composed video frames.
- [var renderSize: CGSize](./rendersize.md)
  The size at which the video composition should render.
- [var renderScale: Float](./renderscale.md)
  The scale at which the video composition should render.
- [outputBufferDescription](./outputbufferdescription.md)
  The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of CMTagCollectionRef objects that describes the output buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/animationtool)*