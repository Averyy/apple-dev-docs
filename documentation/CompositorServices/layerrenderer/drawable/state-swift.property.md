# state

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The current operational state of a drawable instance.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var state: LayerRenderer.Drawable.State { get }
```

```c
enum cp_drawable_state cp_drawable_get_state(cp_drawable_t drawable);
```

#### Discussion

A state value of [`LayerRenderer.Drawable.State.rendering`](./state-swift.enum/rendering.md) indicates the drawable type is ready for you to draw your content. Other values indicate that Compositor Services currently owns the drawable.

Compositor Services reuses the underlying data structures associated with drawable types. The drawable’s state indicates whether it’s ready for you to draw to it. Run your drawing operations only when the drawable’s state is equal to [`LayerRenderer.Drawable.State.rendering`](./state-swift.enum/rendering.md).

## See Also

### Managing the state machine
- [LayerRenderer.Drawable.State](./state-swift.enum.md)
  The state of ownership for the drawable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/state-swift.property)*