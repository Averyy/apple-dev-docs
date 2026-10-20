# AVVideoCompositionCoreAnimationTool.Configuration

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

Configurable properties for initializing a new AVVideoCompositionCoreAnimationTool instance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration
- [init(postProcessingAsVideoLayer: CALayer, containingLayer: CALayer)](./configuration/init%28postprocessingasvideolayer,containinglayer%29.md)
  Place composited video frames in videoLayer and render animationLayer to produce the final frame. Normally videoLayer should be in animationLayer’s sublayer tree. The animationLayer should not come from, or be added to, another layer tree. Be aware that on iOS, CALayers backing a UIView usually have their content flipped (as defined by the -contentsAreFlipped method). It may be required to insert a CALayer with its geometryFlipped property set to YES in the layer hierarchy to get the same result when attaching a CALayer to a AVVideoCompositionCoreAnimationTool as when using it to back a UIView.
- [init(postProcessingAsVideoLayers: [CALayer], containingLayer: CALayer)](./configuration/init%28postprocessingasvideolayers,containinglayer%29.md)
  Duplicate the composited video frames in each videoLayer and render animationLayer to produce the final frame. Normally videoLayers should be in animationLayer’s sublayer tree. The animationLayer should not come from, or be added to, another layer tree. Be aware that on iOS, CALayers backing a UIView usually have their content flipped (as defined by the -contentsAreFlipped method). It may be required to insert a CALayer with its geometryFlipped property set to YES in the layer hierarchy to get the same result when attaching a CALayer to a AVVideoCompositionCoreAnimationTool as when using it to back a UIView.
### Inspecting the configuration
- [var containingLayer: CALayer](./configuration/containinglayer.md)
  Containing layer to be rendered into, producing the final frame.
- [var layers: [CALayer]](./configuration/layers.md)
  Layer(s) to contain the composited video frames. Frames are duplicated if there is more than one layer.

## See Also

### Creating a composition tool
- [convenience init(additionalLayer: sending CALayer, asTrackID: CMPersistentTrackID)](./init%28additionallayer,astrackid%29.md)
  Adds a Core Animation layer to the video composition.
- [convenience init(postProcessingAsVideoLayer: CALayer, in: CALayer)](./init%28postprocessingasvideolayer,in%29.md)
  Composes the composited video frame with a Core Animation layer.
- [convenience init(postProcessingAsVideoLayers: [CALayer], in: CALayer)](./init%28postprocessingasvideolayers,in%29.md)
  Composes the composited video frames with the Core Animation layer.
- [convenience init(configuration: sending AVVideoCompositionCoreAnimationTool.Configuration)](./init%28configuration%29.md)
  Compose the composited video frames with the Core Animation layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/configuration)*