# cp_layer_renderer_configuration_set_depth_format

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Sets the pixel format for the layer’s depth textures to the specified value.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
void cp_layer_renderer_configuration_set_depth_format(cp_layer_renderer_configuration_t configuration, MTLPixelFormat depth_format);
```

## Discussion

Use this function to modify the configuration details for your layer. Fetch the layer’s supported pixel formats using the [`cp_layer_renderer_capabilities_supported_depth_format`](./cp_layer_renderer_capabilities_supported_depth_format.md) function.

## Parameters

- `configuration`: The layer configuration details.
- `depth_format`: The pixel format to apply to your layer’s depth textures. The value you specify must be one of the values obtained from the [`cp_layer_renderer_capabilities_supported_depth_format`](./cp_layer_renderer_capabilities_supported_depth_format.md) function.

## See Also

### Configuring the depth information
- [cp_layer_renderer_configuration_get_depth_format](./cp_layer_renderer_configuration_get_depth_format.md)
  Returns the pixel format to use for the layer’s depth textures.
- [cp_layer_renderer_configuration_get_depth_usage](./cp_layer_renderer_configuration_get_depth_usage.md)
  Returns the texture usage value to apply to the layer’s depth textures.
- [cp_layer_renderer_configuration_set_depth_usage](./cp_layer_renderer_configuration_set_depth_usage.md)
  Sets the texture usage for the layer’s depth textures to the specified value.
- [cp_layer_renderer_configuration_get_default_depth_range](./cp_layer_renderer_configuration_get_default_depth_range.md)
  Returns the distances for the far and near clipping planes you use during drawing.
- [cp_layer_renderer_configuration_set_default_depth_range](./cp_layer_renderer_configuration_set_default_depth_range.md)
  Sets the default distances to the far and near clipping planes you use during drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_set_depth_format)*