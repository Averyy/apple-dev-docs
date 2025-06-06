# state

**Framework**: Compositor Services  
**Kind**: property

A value that indicates whether the layer renderer is currently visible and ready for you to draw content.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var state: LayerRenderer.State { get }
```

#### Discussion

Use the state of the layer to determine when to start and stop your rendering loop. When the layer is in the [`LayerRenderer.State.running`](layerrenderer/state-swift.enum/running.md) state, draw frames of content using your rendering loop. Stop your rendering loop when the layer enters other states. When the layer reaches the [`LayerRenderer.State.invalidated`](layerrenderer/state-swift.enum/invalidated.md) state, clean up and deallocate your render loop structures.

## See Also

- [func waitUntilRunning()](layerrenderer/waituntilrunning.md)
  Stops further execution of your code until the layer renderer leaves the paused state.
- [LayerRenderer.State](layerrenderer/state-swift.enum.md)
  The states of the layer renderer, which tell you how to proceed with drawing operations.
- [LayerRenderer.Clock](layerrenderer/clock.md)
  A type that supports operations that require a precise time measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/state-swift.property)*