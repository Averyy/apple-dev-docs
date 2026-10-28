# cp_frame_monocular_frustum_matrix_for_drawable_target

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the transform which can be used for monocular frustum culling. A matrix to convert between the device coordinate space to normalized device coordinate space. This should be acquired after query frame via [`cp_layer_renderer_query_next_frame`](./cp_layer_renderer_query_next_frame.md) and before calling into [`endSubmission()`](./layerrenderer/frame/endsubmission%28%29.md). Renderer should not utilize this transform for actual rendering output.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
simd_float4x4 cp_frame_monocular_frustum_matrix_for_drawable_target(cp_frame_t frame, cp_drawable_target drawable_target, cp_axis_direction_convention normalized_device_coordinates_convension, size_t view_index, simd_float4 increase_tangents, simd_float2 depth_range);
```

## Return Value

A perspective projection matrix that transforms coordinates from view coordinate space to clip space.

## Discussion

The convention is defined in normalized device coordinates, which impact the rendering direction of rendering but have no impact on the convention used for model/view space. To convert from view space to the axis direction convention used by the projection matrix, a rotation/mirror matrix can be applied pre-projection matrix.

The axes are defined as: • X axes determines the horizontal direction of pixels – right convention means the left-most pixel is the left of the view • Y axes determines the vertical direction of pixels – up convention means the top-most pixel is the top of the view • Z axes determines the handedness/winding order The default convention is `cp_axis_direction_convention_right_up_back` for CompositorServices and Metal renderers which has a counter-clockwise winding order.

To avoid false positives during culling, transform should have broader tangents and depth range compared to one will be used for rendering. As the time performing culling becomes more distant from `presentation time`, renderer should request for wider tangents/depth.

## Parameters

- `frame`: Frame: The frame you finished preparing.
- `drawable_target`: Whether this is intended for `built_in` or `recorder`drawable
- `normalized_device_coordinates_convension`: The normalized device coordinate axes convention used.
- `view_index`: The index of the view you want. The index must be greater than or equal to `0` and less than the value that [`drawableTargetViewCount(target:)`](./layerrenderer/frame/drawabletargetviewcount%28target%29.md) returns.
- `increase_tangents`: The requested increased tangents for computing the projection transform. Values should be positive.
- `depth_range`: The requested depth range for computing the projection transform. The range should be bigger than the one used for rendering


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_frame_monocular_frustum_matrix_for_drawable_target)*