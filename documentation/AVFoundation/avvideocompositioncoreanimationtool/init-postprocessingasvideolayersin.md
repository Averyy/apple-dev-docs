# init(postProcessingAsVideoLayers:in:)

**Framework**: AVFoundation  
**Kind**: init

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

#### Return Value

A new `AVVideoCompositionCoreAnimationTool` instance with the composited video frames and the rendered animation layer.

#### Discussion

Duplicates the composited video frames in each videoLayer and renders animationLayer to produce the final frame. The `videoLayers` should be in `animationLayer`’s sublayer tree.

The `animationLayer` should not come from, or be added to, another layer tree.

> **Note**:  On iOS, a layer instance backing a [`UIView`](https://developer.apple.com/documentation/UIKit/UIView) usually have their content flipped, as defined by the [`contentsAreFlipped()`](https://developer.apple.com/documentation/QuartzCore/CALayer/contentsAreFlipped()) method. It may be required to insert a [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer) instance with its [`isGeometryFlipped`](https://developer.apple.com/documentation/QuartzCore/CALayer/isGeometryFlipped) property set to [`true`](https://developer.apple.com/documentation/swift/true) in the layer hierarchy to get the same result when attaching a layer to the receiver when the layer backs a [`UIView`](https://developer.apple.com/documentation/UIKit/UIView).

## Parameters

- `videoLayers`: An array containing the video layers
- `animationLayer`: The animation layer.

## See Also

- [convenience init(additionalLayer: sending CALayer, asTrackID: CMPersistentTrackID)](avvideocompositioncoreanimationtool/init(additionallayer:astrackid:).md)
  Adds a Core Animation layer to the video composition.
- [convenience init(postProcessingAsVideoLayer: CALayer, in: CALayer)](avvideocompositioncoreanimationtool/init(postprocessingasvideolayer:in:).md)
  Composes the composited video frame with a Core Animation layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/init(postprocessingasvideolayers:in:))*