# init(postProcessingAsVideoLayers:in:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Composes the composited video frames with the Core Animation layer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(postProcessingAsVideoLayers videoLayers: [CALayer], in animationLayer: CALayer)
```

```objc
+ (instancetype) videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayers:(NSArray<CALayer *> *) videoLayers inLayer:(CALayer *) animationLayer;
```

#### Return Value

A new `AVVideoCompositionCoreAnimationTool` instance with the composited video frames and the rendered animation layer.

#### Discussion

Duplicates the composited video frames in each videoLayer and renders animationLayer to produce the final frame. The `videoLayers` should be in `animationLayer`’s sublayer tree.

The `animationLayer` should not come from, or be added to, another layer tree.

> **Note**:  On iOS, a layer instance backing a [`UIView`](../../UIKit/uiview.md) usually have their content flipped, as defined by the [`contentsAreFlipped()`](../../QuartzCore/calayer/contentsareflipped%28%29.md) method. It may be required to insert a [`CALayer`](../../QuartzCore/calayer.md) instance with its [`isGeometryFlipped`](../../QuartzCore/calayer/isgeometryflipped.md) property set to [`true`](../../Swift/true.md) in the layer hierarchy to get the same result when attaching a layer to the receiver when the layer backs a [`UIView`](../../UIKit/uiview.md).

## Parameters

- `videoLayers`: An array containing the video layers
- `animationLayer`: The animation layer.

## See Also

### Creating a composition tool
- [convenience init(additionalLayer: sending CALayer, asTrackID: CMPersistentTrackID)](./init%28additionallayer,astrackid%29.md)
  Adds a Core Animation layer to the video composition.
- [convenience init(postProcessingAsVideoLayer: CALayer, in: CALayer)](./init%28postprocessingasvideolayer,in%29.md)
  Composes the composited video frame with a Core Animation layer.
- [convenience init(configuration: sending AVVideoCompositionCoreAnimationTool.Configuration)](./init%28configuration%29.md)
  Compose the composited video frames with the Core Animation layer.
- [AVVideoCompositionCoreAnimationTool.Configuration](./configuration.md)
  Configurable properties for initializing a new AVVideoCompositionCoreAnimationTool instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/init(postprocessingasvideolayers:in:))*