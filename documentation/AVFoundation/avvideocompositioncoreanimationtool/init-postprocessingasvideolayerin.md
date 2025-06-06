# init(postProcessingAsVideoLayer:in:)

**Framework**: AVFoundation  
**Kind**: init

Composes the composited video frame with a Core Animation layer.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(postProcessingAsVideoLayer videoLayer: CALayer, in animationLayer: CALayer)
```

#### Return Value

A new animation tool for the composition.

#### Discussion

Place composited video frames in `videoLayer` and render `animationLayer` to produce the final frame.

The `videoLayer` should be in the `animationLayer` sublayer tree. The `animationLayer` should not come from, or be added to, another layer tree.

## Parameters

- `videoLayer`: A video layer.
- `animationLayer`: An animation layer.

## See Also

- [convenience init(additionalLayer: CALayer, asTrackID: CMPersistentTrackID)](avvideocompositioncoreanimationtool/init(additionallayer:astrackid:).md)
  Adds a Core Animation layer to the video composition.
- [convenience init(postProcessingAsVideoLayers: [CALayer], in: CALayer)](avvideocompositioncoreanimationtool/init(postprocessingasvideolayers:in:).md)
  Composes the composited video frames with the Core Animation layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/init(postprocessingasvideolayer:in:))*