# init(postProcessingAsVideoLayers:containingLayer:)

**Framework**: AVFoundation  
**Kind**: init

Duplicate the composited video frames in each videoLayer and render animationLayer to produce the final frame. Normally videoLayers should be in animationLayer’s sublayer tree. The animationLayer should not come from, or be added to, another layer tree. Be aware that on iOS, CALayers backing a UIView usually have their content flipped (as defined by the -contentsAreFlipped method). It may be required to insert a CALayer with its geometryFlipped property set to YES in the layer hierarchy to get the same result when attaching a CALayer to a AVVideoCompositionCoreAnimationTool as when using it to back a UIView.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(postProcessingAsVideoLayers layers: [CALayer], containingLayer: CALayer)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioncoreanimationtool/configuration/init(postprocessingasvideolayers:containinglayer:))*