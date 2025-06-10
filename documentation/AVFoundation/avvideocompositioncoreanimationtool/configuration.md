# AVVideoCompositionCoreAnimationTool.Configuration

**Framework**: AVFoundation  
**Kind**: struct

Configurable properties for initializing a new AVVideoCompositionCoreAnimationTool instance.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Configuration
```

## Topics

### Initializers
- [init(postProcessingAsVideoLayer: CALayer, containingLayer: CALayer)](avvideocompositioncoreanimationtool/configuration/init(postprocessingasvideolayer:containinglayer:).md)
  Place composited video frames in videoLayer and render animationLayer to produce the final frame. Normally videoLayer should be in animationLayer’s sublayer tree. The animationLayer should not come from, or be added to, another layer tree. Be aware that on iOS, CALayers backing a UIView usually have their content flipped (as defined by the -contentsAreFlipped method). It may be required to insert a CALayer with its geometryFlipped property set to YES in the layer hierarchy to get the same result when attaching a CALayer to a AVVideoCompositionCoreAnimationTool as when using it to back a UIView.
- [init(postProcessingAsVideoLayers: [CALayer], containingLayer: CALayer)](avvideocompositioncoreanimationtool/configuration/init(postprocessingasvideolayers:containinglayer:).md)
  Duplicate the composited video frames in each videoLayer and render animationLayer to produce the final frame. Normally videoLayers should be in animationLayer’s sublayer tree. The animationLayer should not come from, or be added to, another layer tree. Be aware that on iOS, CALayers backing a UIView usually have their content flipped (as defined by the -contentsAreFlipped method). It may be required to insert a CALayer with its geometryFlipped property set to YES in the layer hierarchy to get the same result when attaching a CALayer to a AVVideoCompositionCoreAnimationTool as when using it to back a UIView.
### Instance Properties
- [var containingLayer: CALayer](avvideocompositioncoreanimationtool/configuration/containinglayer.md)
  Containing layer to be rendered into, producing the final frame.
- [var layers: [CALayer]](avvideocompositioncoreanimationtool/configuration/layers.md)
  Layer(s) to contain the composited video frames. Frames are duplicated if there is more than one layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/configuration)*