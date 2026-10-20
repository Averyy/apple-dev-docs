# LayerRenderer.State.running

**Framework**: Compositor Services  
**Kind**: case  
**Role**: Case

A state that indicates the layer is visible and ready for you to draw your content.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
case running
```

```c
cp_layer_renderer_state_running
```

## Mentions

- [Drawing fully immersive content using Metal](../../drawing-fully-immersive-content-using-metal.md)

#### Discussion

When the layer enters this state, start your rendering loop and begin drawing frames of content. Keep drawing frames of content until the layer transitions to another state.

## See Also

### Getting the states
- [LayerRenderer.State.paused](./paused.md)
  A state that indicates the layer is paused and not currently drawing.
- [LayerRenderer.State.invalidated](./invalidated.md)
  A state that indicates the layer no longer supports drawing operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/state-swift.enum/running)*