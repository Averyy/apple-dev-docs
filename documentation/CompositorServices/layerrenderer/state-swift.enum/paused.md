# LayerRenderer.State.paused

**Framework**: Compositor Services  
**Kind**: case

A state that indicates the layer is paused and not currently drawing.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
case paused
```

## Mentions

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)

#### Discussion

A layer starts in this state and later transitions to other states over time. Don’t run your render loop or do any drawing while in this state. Wait until the layer changes to one of the other states to take further action.

## See Also

- [LayerRenderer.State.running](layerrenderer/state-swift.enum/running.md)
  A state that indicates the layer is visible and ready for you to draw your content.
- [LayerRenderer.State.invalidated](layerrenderer/state-swift.enum/invalidated.md)
  A state that indicates the layer no longer supports drawing operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/state-swift.enum/paused)*