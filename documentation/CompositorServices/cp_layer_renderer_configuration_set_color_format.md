# cp_layer_renderer_configuration_set_color_format

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Sets the pixel format for the layer’s color textures to the specified value.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
void cp_layer_renderer_configuration_set_color_format(cp_layer_renderer_configuration_t configuration, MTLPixelFormat color_format);
```

#### Discussion

Use this function to modify the configuration details for your layer. Fetch the layer’s supported pixel formats using the [`cp_layer_renderer_capabilities_supported_color_format`](./cp_layer_renderer_capabilities_supported_color_format.md) function.

> **Note**:  Apple Vision Pro uses the P3 color space for pixel color values.

## Parameters

- `configuration`: The layer configuration details.
- `color_format`: The pixel format to apply to your layer’s color textures. The value you specify must be one of the values obtained from the [`cp_layer_renderer_capabilities_supported_color_format`](./cp_layer_renderer_capabilities_supported_color_format.md) function.

## See Also

### Configuring the color textures
- [cp_layer_renderer_configuration_get_color_format](./cp_layer_renderer_configuration_get_color_format.md)
  Returns the pixel format to use for the layer’s color textures.
- [cp_layer_renderer_configuration_get_color_usage](./cp_layer_renderer_configuration_get_color_usage.md)
  Returns the texture usage value to apply to the layer’s color textures.
- [cp_layer_renderer_configuration_set_color_usage](./cp_layer_renderer_configuration_set_color_usage.md)
  Sets the texture usage for the layer’s color textures to the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_set_color_format)*