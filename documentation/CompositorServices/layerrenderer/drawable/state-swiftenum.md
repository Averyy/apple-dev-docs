# LayerRenderer.Drawable.State

**Framework**: Compositor Services  
**Kind**: enum

The state of ownership for the drawable.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum State
```

#### Overview

Use these constants to determine whether the drawable is ready for you to use. When the drawable is in the [`LayerRenderer.Drawable.State.rendering`](layerrenderer/drawable/state-swift.enum/rendering.md)  state, you can begin drawing. Other states indicate the drawable is either busy or not assigned to a frame.

## Topics

### Getting the states
- [LayerRenderer.Drawable.State.available](layerrenderer/drawable/state-swift.enum/available.md)
  A drawable that’s not in use and ready for assignment to a frame.
- [LayerRenderer.Drawable.State.presenting](layerrenderer/drawable/state-swift.enum/presenting.md)
  A drawable that the compositor is currently displaying.
- [LayerRenderer.Drawable.State.rendering](layerrenderer/drawable/state-swift.enum/rendering.md)
  A drawable that’s assigned to a frame and ready to accept your drawing commands.
### Initializers
- [init?(rawValue: UInt32)](layerrenderer/drawable/state-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var state: LayerRenderer.Drawable.State](layerrenderer/drawable/state-swift.property.md)
  The current operational state of a drawable instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/state-swift.enum)*