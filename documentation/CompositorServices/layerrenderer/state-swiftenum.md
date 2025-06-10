# LayerRenderer.State

**Framework**: Compositor Services  
**Kind**: enum

The states of the layer renderer, which tell you how to proceed with drawing operations.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
enum State
```

## Topics

### Getting the states
- [LayerRenderer.State.paused](layerrenderer/state-swift.enum/paused.md)
  A state that indicates the layer is paused and not currently drawing.
- [LayerRenderer.State.running](layerrenderer/state-swift.enum/running.md)
  A state that indicates the layer is visible and ready for you to draw your content.
- [LayerRenderer.State.invalidated](layerrenderer/state-swift.enum/invalidated.md)
  A state that indicates the layer no longer supports drawing operations.
### Initializers
- [init?(rawValue: UInt32)](layerrenderer/state-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var state: LayerRenderer.State](layerrenderer/state-swift.property.md)
  A value that indicates whether the layer renderer is currently visible and ready for you to draw content.
- [func waitUntilRunning()](layerrenderer/waituntilrunning.md)
  Stops further execution of your code until the layer renderer leaves the paused state.
- [LayerRenderer.Clock](layerrenderer/clock.md)
  A type that supports operations that require a precise time measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/state-swift.enum)*