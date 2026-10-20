# init(configuration:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Compose the composited video frames with the Core Animation layer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(configuration: sending AVVideoCompositionCoreAnimationTool.Configuration)
```

## See Also

### Creating a composition tool
- [convenience init(additionalLayer: sending CALayer, asTrackID: CMPersistentTrackID)](./init%28additionallayer,astrackid%29.md)
  Adds a Core Animation layer to the video composition.
- [convenience init(postProcessingAsVideoLayer: CALayer, in: CALayer)](./init%28postprocessingasvideolayer,in%29.md)
  Composes the composited video frame with a Core Animation layer.
- [convenience init(postProcessingAsVideoLayers: [CALayer], in: CALayer)](./init%28postprocessingasvideolayers,in%29.md)
  Composes the composited video frames with the Core Animation layer.
- [AVVideoCompositionCoreAnimationTool.Configuration](./configuration.md)
  Configurable properties for initializing a new AVVideoCompositionCoreAnimationTool instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/init(configuration:))*