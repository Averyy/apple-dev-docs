# init(postProcessingAsVideoLayer:containingLayer:)

**Framework**: AVFoundation  
**Kind**: init

Place composited video frames in videoLayer and render animationLayer to produce the final frame. Normally videoLayer should be in animationLayer’s sublayer tree. The animationLayer should not come from, or be added to, another layer tree. Be aware that on iOS, CALayers backing a UIView usually have their content flipped (as defined by the -contentsAreFlipped method). It may be required to insert a CALayer with its geometryFlipped property set to YES in the layer hierarchy to get the same result when attaching a CALayer to a AVVideoCompositionCoreAnimationTool as when using it to back a UIView.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(postProcessingAsVideoLayer layer: CALayer, containingLayer: CALayer)
```

## See Also

- [init(postProcessingAsVideoLayers: [CALayer], containingLayer: CALayer)](avvideocompositioncoreanimationtool/configuration/init(postprocessingasvideolayers:containinglayer:).md)
  Duplicate the composited video frames in each videoLayer and render animationLayer to produce the final frame. Normally videoLayers should be in animationLayer’s sublayer tree. The animationLayer should not come from, or be added to, another layer tree. Be aware that on iOS, CALayers backing a UIView usually have their content flipped (as defined by the -contentsAreFlipped method). It may be required to insert a CALayer with its geometryFlipped property set to YES in the layer hierarchy to get the same result when attaching a CALayer to a AVVideoCompositionCoreAnimationTool as when using it to back a UIView.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/configuration/init(postprocessingasvideolayer:containinglayer:))*