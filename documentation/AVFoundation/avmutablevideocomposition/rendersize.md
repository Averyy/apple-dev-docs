# renderSize

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The size at which the video composition should render.

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
var renderSize: CGSize { get set }
```

```objc
@property (nonatomic) CGSize renderSize;
```

## See Also

### Configuring video composition properties
- [var frameDuration: CMTime](./frameduration.md)
  A time interval for which the video composition should render composed video frames.
- [var renderScale: Float](./renderscale.md)
  The scale at which the video composition should render.
- [var animationTool: AVVideoCompositionCoreAnimationTool?](./animationtool.md)
  A video composition tool to use with Core Animation in offline rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/rendersize)*