# cp_drawable_set_depth_range

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Sets the distances to the near and far clipping planes for the current drawable.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
void cp_drawable_set_depth_range(cp_drawable_t drawable, simd_float2 depth_range);
```

#### Discussion

Use this function to change the depth range for this frame of content. The near and far planes correspond to distances from the person viewing the content. The compositor uses these values to compute the perspective projection matrix and to clip content not between the near and far planes.

Configure the default depth range for all frames in your layer using the [`cp_layer_renderer_configuration_set_default_depth_range`](./cp_layer_renderer_configuration_set_default_depth_range.md) function.

## Parameters

- `drawable`: The drawable for a frame.
- `depth_range`: The distances to the far and near planes in meters. Specify the values in reverse-z order, with the value for the far plane in the vector’s `x` property and the value for the near plane in the vector’s `y` property.

## See Also

### Accessing pixel depth information
- [var depthRange: simd_float2](./layerrenderer/drawable/depthrange.md)
  The distances to the far and near clipping planes from the person viewing the content, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_drawable_set_depth_range)*