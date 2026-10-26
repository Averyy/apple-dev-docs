# renderScale

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The scale at which the video composition should render.

**Availability**:
- iOS 4.0+ - Deprecated in 26.0
- iPadOS 4.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.14+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
var renderScale: Float { get set }
```

```objc
@property (nonatomic) float renderScale;
```

#### Discussion

May only be other than `1.0` for a video composition set on an [`AVPlayerItem`](../avplayeritem.md).

## See Also

### Configuring video composition properties
- [var frameDuration: CMTime](./frameduration.md)
  A time interval for which the video composition should render composed video frames.
- [var renderSize: CGSize](./rendersize.md)
  The size at which the video composition should render.
- [var animationTool: AVVideoCompositionCoreAnimationTool?](./animationtool.md)
  A video composition tool to use with Core Animation in offline rendering.
- [outputBufferDescription](./outputbufferdescription.md)
  The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of CMTagCollectionRef objects that describes the output buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/renderscale)*