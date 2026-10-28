# init(postProcessingAsVideoLayer:in:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Composes the composited video frame with a Core Animation layer.

**Availability**:
- iOS 4.0+ - Deprecated in 27.0
- iPadOS 4.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.7+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use .init(configuration: AVVideoCompositionCoreAnimationTool.Configuration) instead

## Declaration

```swift
convenience init(postProcessingAsVideoLayer videoLayer: CALayer, in animationLayer: CALayer)
```

```objc
+ (instancetype) videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayer:(CALayer *) videoLayer inLayer:(CALayer *) animationLayer;
```

## Return Value

A new animation tool for the composition.

## Discussion

Place composited video frames in `videoLayer` and render `animationLayer` to produce the final frame.

The `videoLayer` should be in the `animationLayer` sublayer tree. The `animationLayer` should not come from, or be added to, another layer tree.

## Parameters

- `videoLayer`: A video layer.
- `animationLayer`: An animation layer.

## See Also

### Creating a composition tool
- [convenience init(additionalLayer: sending CALayer, asTrackID: CMPersistentTrackID)](./init%28additionallayer,astrackid%29.md)
  Adds a Core Animation layer to the video composition.
- [convenience init(postProcessingAsVideoLayers: [CALayer], in: CALayer)](./init%28postprocessingasvideolayers,in%29.md)
  Composes the composited video frames with the Core Animation layer.
- [convenience init(configuration: sending AVVideoCompositionCoreAnimationTool.Configuration)](./init%28configuration%29.md)
  Compose the composited video frames with the Core Animation layer.
- [AVVideoCompositionCoreAnimationTool.Configuration](./configuration.md)
  Configurable properties for initializing a new AVVideoCompositionCoreAnimationTool instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/init(postprocessingasvideolayer:in:))*