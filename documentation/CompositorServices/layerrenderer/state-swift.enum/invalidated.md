# LayerRenderer.State.invalidated

**Framework**: Compositor Services  
**Kind**: case

A state that indicates the layer no longer supports drawing operations.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
case invalidated
```

## Mentions

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)

#### Discussion

A layer enters this state shortly before the system releases its resources. When the layer enters this state, exit your rendering loop and release any drawing-related structures.

## See Also

- [LayerRenderer.State.paused](layerrenderer/state-swift.enum/paused.md)
  A state that indicates the layer is paused and not currently drawing.
- [LayerRenderer.State.running](layerrenderer/state-swift.enum/running.md)
  A state that indicates the layer is visible and ready for you to draw your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/state-swift.enum/invalidated)*