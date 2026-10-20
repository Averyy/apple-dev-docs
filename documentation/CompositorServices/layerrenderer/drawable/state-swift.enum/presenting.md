# LayerRenderer.Drawable.State.presenting

**Framework**: Compositor Services  
**Kind**: case  
**Role**: Case

A drawable that the compositor is currently displaying.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
case presenting
```

```c
cp_drawable_state_presenting
```

## See Also

### Getting the states
- [LayerRenderer.Drawable.State.available](./available.md)
  A drawable that’s not in use and ready for assignment to a frame.
- [LayerRenderer.Drawable.State.rendering](./rendering.md)
  A drawable that’s assigned to a frame and ready to accept your drawing commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/state-swift.enum/presenting)*