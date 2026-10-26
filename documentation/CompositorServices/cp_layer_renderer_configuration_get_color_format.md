# cp_layer_renderer_configuration_get_color_format

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the pixel format to use for the layer’s color textures.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
MTLPixelFormat cp_layer_renderer_configuration_get_color_format(cp_layer_renderer_configuration_t configuration);
```

#### Return Value

The pixel format to use for color textures.

#### Discussion

The compositor configures the color textures for each frame using this pixel format value.

> **Note**:  Apple Vision Pro uses the P3 color space for pixel color values.

## Parameters

- `configuration`: The layer configuration details.

## See Also

### Configuring the color textures
- [cp_layer_renderer_configuration_set_color_format](./cp_layer_renderer_configuration_set_color_format.md)
  Sets the pixel format for the layer’s color textures to the specified value.
- [cp_layer_renderer_configuration_get_color_usage](./cp_layer_renderer_configuration_get_color_usage.md)
  Returns the texture usage value to apply to the layer’s color textures.
- [cp_layer_renderer_configuration_set_color_usage](./cp_layer_renderer_configuration_set_color_usage.md)
  Sets the texture usage for the layer’s color textures to the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_get_color_format)*