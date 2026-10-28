# cp_layer_renderer_configuration_set_default_depth_range

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Sets the default distances to the far and near clipping planes you use during drawing.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
void cp_layer_renderer_configuration_set_default_depth_range(cp_layer_renderer_configuration_t configuration, simd_float2 depth_range);
```

## Discussion

Use this function to modify the configuration details for your layer. The near and far planes reflect the distances from the person viewing the content. Compositor Services uses these values to compute the perspective projection matrix and to clip content that is between the camera and the near plane, or located beyond the far plane.

This function modifies the layer’s default depth values. You can also change these values separately for the [`cp_drawable_t`](./cp_drawable_t.md) type of individual frames.

## Parameters

- `configuration`: The layer configuration details.
- `depth_range`: The distances to the far and near planes in meters. Compositor Services returns values in reverse-z ordering, so put the value for the far plane in the vector’s `x` property and the value for the near plane in the vector’s `y` property.

## See Also

### Configuring the depth information
- [cp_layer_renderer_configuration_get_depth_format](./cp_layer_renderer_configuration_get_depth_format.md)
  Returns the pixel format to use for the layer’s depth textures.
- [cp_layer_renderer_configuration_set_depth_format](./cp_layer_renderer_configuration_set_depth_format.md)
  Sets the pixel format for the layer’s depth textures to the specified value.
- [cp_layer_renderer_configuration_get_depth_usage](./cp_layer_renderer_configuration_get_depth_usage.md)
  Returns the texture usage value to apply to the layer’s depth textures.
- [cp_layer_renderer_configuration_set_depth_usage](./cp_layer_renderer_configuration_set_depth_usage.md)
  Sets the texture usage for the layer’s depth textures to the specified value.
- [cp_layer_renderer_configuration_get_default_depth_range](./cp_layer_renderer_configuration_get_default_depth_range.md)
  Returns the distances for the far and near clipping planes you use during drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_set_default_depth_range)*