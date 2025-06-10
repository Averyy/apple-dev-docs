# LayerRenderer.State.running

**Framework**: Compositor Services  
**Kind**: case

A state that indicates the layer is visible and ready for you to draw your content.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
case running
```

## Mentions

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)

#### Discussion

When the layer enters this state, start your rendering loop and begin drawing frames of content. Keep drawing frames of content until the layer transitions to another state.

## See Also

- [LayerRenderer.State.paused](layerrenderer/state-swift.enum/paused.md)
  A state that indicates the layer is paused and not currently drawing.
- [LayerRenderer.State.invalidated](layerrenderer/state-swift.enum/invalidated.md)
  A state that indicates the layer no longer supports drawing operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/state-swift.enum/running)*