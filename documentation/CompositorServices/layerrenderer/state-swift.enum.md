# LayerRenderer.State

**Framework**: Compositor Services  
**Kind**: enum  
**Role**: Enumeration

The states of the layer renderer, which tell you how to proceed with drawing operations.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
enum State
```

```c
enum cp_layer_renderer_state : uint32_t;
```

## Topics

### Getting the states
- [LayerRenderer.State.paused](./state-swift.enum/paused.md)
  A state that indicates the layer is paused and not currently drawing.
- [LayerRenderer.State.running](./state-swift.enum/running.md)
  A state that indicates the layer is visible and ready for you to draw your content.
- [LayerRenderer.State.invalidated](./state-swift.enum/invalidated.md)
  A state that indicates the layer no longer supports drawing operations.
### Initializers
- [init?(rawValue: UInt32)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the rendering loop
- [var state: LayerRenderer.State](./state-swift.property.md)
  A value that indicates whether the layer renderer is currently visible and ready for you to draw content.
- [func waitUntilRunning()](./waituntilrunning%28%29.md)
  Stops further execution of your code until the layer renderer leaves the paused state.
- [LayerRenderer.Clock](./clock.md)
  A type that supports operations that require a precise time measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/state-swift.enum)*