# drawableTargetViewCount(target:)

**Framework**: Compositor Services  
**Kind**: method

Returns the number of view in the drawable target.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func drawableTargetViewCount(target drawable_target: LayerRenderer.Drawable.Target) -> Int
```

#### Return Value

The number of views available for drawing. For example, a return value of `2` indicates there are two views for this target drawable in this frame. value of `0` indicates there is no view available for this target drawable in this frame.

#### Discussion

Use the returned value as the maximum number of views to retrieve from the [`cp_frame_binocular_frustum_matrix_for_drawable_target`](cp_frame_binocular_frustum_matrix_for_drawable_target.md) or [`cp_frame_monocular_frustum_matrix_for_drawable_target`](cp_frame_monocular_frustum_matrix_for_drawable_target.md) functions.

## Parameters

- `drawable_target`: Whether this is intended for   or  drawable


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/frame/drawabletargetviewcount(target:))*