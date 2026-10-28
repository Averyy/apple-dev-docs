# cp_layer_renderer_configuration_get_depth_usage

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the texture usage value to apply to the layer’s depth textures.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
MTLTextureUsage cp_layer_renderer_configuration_get_depth_usage(cp_layer_renderer_configuration_t configuration);
```

## Return Value

The Metal texture usage value to apply to the layer’s depth textures.

## Discussion

Metal optimizes texture-related operations based on the texture’s usage value. The usage value can be a combination of options. For more information, see [`MTLTextureUsage`](../Metal/mtltextureusage.md).

## Parameters

- `configuration`: The layer configuration details.

## See Also

### Configuring the depth information
- [cp_layer_renderer_configuration_get_depth_format](./cp_layer_renderer_configuration_get_depth_format.md)
  Returns the pixel format to use for the layer’s depth textures.
- [cp_layer_renderer_configuration_set_depth_format](./cp_layer_renderer_configuration_set_depth_format.md)
  Sets the pixel format for the layer’s depth textures to the specified value.
- [cp_layer_renderer_configuration_set_depth_usage](./cp_layer_renderer_configuration_set_depth_usage.md)
  Sets the texture usage for the layer’s depth textures to the specified value.
- [cp_layer_renderer_configuration_get_default_depth_range](./cp_layer_renderer_configuration_get_default_depth_range.md)
  Returns the distances for the far and near clipping planes you use during drawing.
- [cp_layer_renderer_configuration_set_default_depth_range](./cp_layer_renderer_configuration_set_default_depth_range.md)
  Sets the default distances to the far and near clipping planes you use during drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_get_depth_usage)*