# LayerRenderer.Clock

**Framework**: Compositor Services  
**Kind**: struct

A type that supports operations that require a precise time measurement.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct Clock
```

#### Overview

Use this type to perform time-related operations during the rendering of a frame. For example, call [`wait(until:tolerance:)`](layerrenderer/clock/wait(until:tolerance:).md) to pause your render loop until the optimal rendering time arrives.

## Topics

### Putting the current thread to sleep
- [func wait(until: LayerRenderer.Clock.Instant, tolerance: Duration?)](layerrenderer/clock/wait(until:tolerance:).md)
  Blocks the current thread until the specified time.
### Creating a clock
- [init()](layerrenderer/clock/init.md)
  Creates a new clock type.

## Relationships

### Conforms To
- [Clock](../Swift/Clock.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var state: LayerRenderer.State](layerrenderer/state-swift.property.md)
  A value that indicates whether the layer renderer is currently visible and ready for you to draw content.
- [func waitUntilRunning()](layerrenderer/waituntilrunning.md)
  Stops further execution of your code until the layer renderer leaves the paused state.
- [LayerRenderer.State](layerrenderer/state-swift.enum.md)
  The states of the layer renderer, which tell you how to proceed with drawing operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/clock)*