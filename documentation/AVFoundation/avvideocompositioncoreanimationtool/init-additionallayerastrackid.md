# init(additionalLayer:asTrackID:)

**Framework**: AVFoundation  
**Kind**: init

Adds a Core Animation layer to the video composition.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(additionalLayer layer: sending CALayer, asTrackID trackID: CMPersistentTrackID)
```

#### Return Value

A new Core Animation tool for the layer.

#### Discussion

You use this method to include a Core Animation layer as an individual track input in video composition.

Video composition instructions should reference `trackID` where the rendered animation should be included.

## Parameters

- `layer`: The Core Animation layer to add.
- `trackID`:  should not match any real trackID in the source.

## See Also

- [convenience init(postProcessingAsVideoLayer: CALayer, in: CALayer)](avvideocompositioncoreanimationtool/init(postprocessingasvideolayer:in:).md)
  Composes the composited video frame with a Core Animation layer.
- [convenience init(postProcessingAsVideoLayers: [CALayer], in: CALayer)](avvideocompositioncoreanimationtool/init(postprocessingasvideolayers:in:).md)
  Composes the composited video frames with the Core Animation layer.
- [convenience init(configuration: sending AVVideoCompositionCoreAnimationTool.Configuration)](avvideocompositioncoreanimationtool/init(configuration:).md)
  Compose the composited video frames with the Core Animation layer.
- [AVVideoCompositionCoreAnimationTool.Configuration](avvideocompositioncoreanimationtool/configuration.md)
  Configurable properties for initializing a new AVVideoCompositionCoreAnimationTool instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/init(additionallayer:astrackid:))*