# LayerRenderer.Drawable.State

**Framework**: Compositor Services  
**Kind**: enum  
**Role**: Enumeration

The state of ownership for the drawable.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
enum State
```

```c
enum cp_drawable_state : uint32_t;
```

## Overview

Use these constants to determine whether the drawable is ready for you to use. When the drawable is in the [`LayerRenderer.Drawable.State.rendering`](./state-swift.enum/rendering.md)  state, you can begin drawing. Other states indicate the drawable is either busy or not assigned to a frame.

## Topics

### Getting the states
- [LayerRenderer.Drawable.State.available](./state-swift.enum/available.md)
  A drawable that’s not in use and ready for assignment to a frame.
- [LayerRenderer.Drawable.State.presenting](./state-swift.enum/presenting.md)
  A drawable that the compositor is currently displaying.
- [LayerRenderer.Drawable.State.rendering](./state-swift.enum/rendering.md)
  A drawable that’s assigned to a frame and ready to accept your drawing commands.
### Initializers
- [init?(rawValue: UInt32)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Managing the state machine
- [var state: LayerRenderer.Drawable.State](./state-swift.property.md)
  The current operational state of a drawable instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/state-swift.enum)*