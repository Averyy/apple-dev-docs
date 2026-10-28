# state

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

A value that indicates whether the layer renderer is currently visible and ready for you to draw content.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var state: LayerRenderer.State { get }
```

```c
enum cp_layer_renderer_state cp_layer_renderer_get_state(cp_layer_renderer_t layer_renderer);
```

## Discussion

Use the state of the layer to determine when to start and stop your rendering loop. When the layer is in the [`LayerRenderer.State.running`](./state-swift.enum/running.md) state, draw frames of content using your rendering loop. Stop your rendering loop when the layer enters other states. When the layer reaches the [`LayerRenderer.State.invalidated`](./state-swift.enum/invalidated.md) state, clean up and deallocate your render loop structures.

## See Also

### Managing the rendering loop
- [func waitUntilRunning()](./waituntilrunning%28%29.md)
  Stops further execution of your code until the layer renderer leaves the paused state.
- [LayerRenderer.State](./state-swift.enum.md)
  The states of the layer renderer, which tell you how to proceed with drawing operations.
- [LayerRenderer.Clock](./clock.md)
  A type that supports operations that require a precise time measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/state-swift.property)*