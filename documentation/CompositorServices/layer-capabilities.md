# Layer capabilities

**Framework**: Compositor Services  
**Role**: API Collection

The color formats, depth formats, and features that you can use to configure your rendering engine.

## Overview

A `cp_layer_capabilities_t` type provides information about the capabilities of the current device. Simulator and devices support different sets of options. Use the information in this type to specify the configuration details for your layer.

## Topics

### Getting the supported color formats
- [cp_layer_renderer_capabilities_supported_color_formats_count](./cp_layer_renderer_capabilities_supported_color_formats_count.md)
  Returns the number of color formats the layer supports.
- [cp_layer_renderer_capabilities_supported_color_format](./cp_layer_renderer_capabilities_supported_color_format.md)
  Returns the color format at the specified index in the layer capabilities.
### Getting the supported depth formats
- [cp_layer_renderer_capabilities_supported_depth_formats_count](./cp_layer_renderer_capabilities_supported_depth_formats_count.md)
  Returns the number of depth formats the layer supports.
- [cp_layer_renderer_capabilities_supported_depth_format](./cp_layer_renderer_capabilities_supported_depth_format.md)
  Returns the depth format at the specified index in the layer capabilities.
### Getting the supported layouts
- [cp_layer_renderer_capabilities_supported_layouts_count](./cp_layer_renderer_capabilities_supported_layouts_count.md)
  Returns the number of layouts the layer supports.
- [cp_layer_renderer_capabilities_supported_layout](./cp_layer_renderer_capabilities_supported_layout.md)
  Returns the layout at the specified index in the layer capabilities.
- [cp_supported_layouts_options](./cp_supported_layouts_options.md)
  The options you can pass to functions that relate to rendering capabilities and layout support.
### Getting the supported features
- [cp_layer_renderer_capabilities_supports_foveation](./cp_layer_renderer_capabilities_supports_foveation.md)
  Returns a Boolean value that indicates whether the layer supports variable rasterization rates.
- [cp_layer_renderer_capabilities_supported_minimum_near_plane_distance](./cp_layer_renderer_capabilities_supported_minimum_near_plane_distance.md)
  Returns the minimum distance in meters to the layer’s near projection plane.
### Getting the capabilities type
- [cp_layer_renderer_capabilities_t](./cp_layer_renderer_capabilities_t.md)
  A type that stores the texture formats and options the layer supports.

## See Also

### Configuring the layer
- [Layer configuration](./layer-configuration.md)
  The pixel formats, depth mask, texture layout, and other drawing-related settings you use to configure your drawing code.
- [Layer properties](./layer-properties.md)
  Information about the textures and views that the system created for your drawing code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layer-capabilities)*