# Layer configuration

**Framework**: Compositor Services  
**Role**: API Collection

The pixel formats, depth mask, texture layout, and other drawing-related settings you use to configure your drawing code.

## Overview

A `cp_layer_configuration_t` type stores the configuration options for your app’s `cp_layer_t` object. When configuring the content for your app’s immersive space, use this type to specify information about the texture layouts, pixel formats, and rendering options you want. The system uses the provided information to initialize the `cp_layer_t` object. It also uses the information to create the Metal textures and other data structures that you use for each frame of content.

You don’t create this type directly. When implementing the `makeConfiguration` method of your `CompositorConfiguration` type, the system passes a set of default configuration values for you to modify.

## Topics

### Getting the layer’s current configuration
- [cp_layer_renderer_get_configuration](./cp_layer_renderer_get_configuration.md)
  Returns the configuration details for the specified layer.
### Configuring the color textures
- [cp_layer_renderer_configuration_get_color_format](./cp_layer_renderer_configuration_get_color_format.md)
  Returns the pixel format to use for the layer’s color textures.
- [cp_layer_renderer_configuration_set_color_format](./cp_layer_renderer_configuration_set_color_format.md)
  Sets the pixel format for the layer’s color textures to the specified value.
- [cp_layer_renderer_configuration_get_color_usage](./cp_layer_renderer_configuration_get_color_usage.md)
  Returns the texture usage value to apply to the layer’s color textures.
- [cp_layer_renderer_configuration_set_color_usage](./cp_layer_renderer_configuration_set_color_usage.md)
  Sets the texture usage for the layer’s color textures to the specified value.
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
- [cp_layer_renderer_configuration_set_default_depth_range](./cp_layer_renderer_configuration_set_default_depth_range.md)
  Sets the default distances to the far and near clipping planes you use during drawing.
### Configuring the texture layout
- [cp_layer_renderer_configuration_get_layout](./cp_layer_renderer_configuration_get_layout.md)
  Returns the texture configuration for the drawable views in the layer.
- [cp_layer_renderer_configuration_set_layout](./cp_layer_renderer_configuration_set_layout.md)
  Changes the layout configuration for the drawable views in the layer.
- [LayerRenderer.Layout](./layerrenderer/layout.md)
  Constants that specify the organization of the textures you use for drawing.
### Configuring the foveation setting
- [cp_layer_renderer_configuration_get_foveation_enabled](./cp_layer_renderer_configuration_get_foveation_enabled.md)
  Returns a Boolean value that indicates whether the layer supports variable rasterization rates.
- [cp_layer_renderer_configuration_set_foveation_enabled](./cp_layer_renderer_configuration_set_foveation_enabled.md)
  Changes the setting that indicates whether the layer supports variable rasterization rates.
- [cp_layer_renderer_configuration_get_generate_flipped_rasterization_rate_maps](./cp_layer_renderer_configuration_get_generate_flipped_rasterization_rate_maps.md)
  Returns a Boolean value that indicates whether the layer renderer provides rasterization rate maps flipped around the y-axis.
- [cp_layer_renderer_configuration_set_generate_flipped_rasterization_rate_maps](./cp_layer_renderer_configuration_set_generate_flipped_rasterization_rate_maps.md)
  Changes the layer renderer setting that provides rasterization rate maps flipped around the y-axis.
### Getting the configuration type
- [cp_layer_renderer_configuration_t](./cp_layer_renderer_configuration_t.md)
  A type that stores the texture formats, layout information, and other details you use to configure your rendering loop code.

## See Also

### Configuring the layer
- [Layer capabilities](./layer-capabilities.md)
  The color formats, depth formats, and features that you can use to configure your rendering engine.
- [Layer properties](./layer-properties.md)
  Information about the textures and views that the system created for your drawing code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layer-configuration)*