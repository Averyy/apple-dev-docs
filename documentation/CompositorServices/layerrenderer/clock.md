# LayerRenderer.Clock

**Framework**: Compositor Services  
**Kind**: struct  
**Role**: Structure

A type that supports operations that require a precise time measurement.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct Clock
```

## Overview

Use this type to perform time-related operations during the rendering of a frame. For example, call [`wait(until:tolerance:)`](./clock/wait%28until,tolerance%29.md) to pause your render loop until the optimal rendering time arrives.

## Topics

### Putting the current thread to sleep
- [func wait(until: LayerRenderer.Clock.Instant, tolerance: Duration?)](./clock/wait%28until,tolerance%29.md)
  Blocks the current thread until the specified time.
### Creating a clock
- [init()](./clock/init%28%29.md)
  Creates a new clock type.

## Relationships

### Conforms To
- [Clock](../../Swift/clock.md)
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the rendering loop
- [var state: LayerRenderer.State](./state-swift.property.md)
  A value that indicates whether the layer renderer is currently visible and ready for you to draw content.
- [func waitUntilRunning()](./waituntilrunning%28%29.md)
  Stops further execution of your code until the layer renderer leaves the paused state.
- [LayerRenderer.State](./state-swift.enum.md)
  The states of the layer renderer, which tell you how to proceed with drawing operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/clock)*