# cp_supported_layouts_options

**Framework**: Compositor Services  
**Kind**: enum  
**Role**: Enumeration

The options you can pass to functions that relate to rendering capabilities and layout support.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
enum cp_supported_layouts_options : uint32_t;
```

## Overview

You can pass the enumeration’s cases to functions, including [`cp_layer_renderer_capabilities_supported_layout`](./cp_layer_renderer_capabilities_supported_layout.md) and [`cp_layer_renderer_capabilities_supported_layouts_count`](./cp_layer_renderer_capabilities_supported_layouts_count.md).

## Topics

### Enumeration Cases
- [cp_supported_layouts_options_foveation_enabled](./cp_supported_layouts_options/cp_supported_layouts_options_foveation_enabled.md)
- [cp_supported_layouts_options_none](./cp_supported_layouts_options/cp_supported_layouts_options_none.md)
- [cp_supported_layouts_options_progressive_immersion_enabled](./cp_supported_layouts_options/cp_supported_layouts_options_progressive_immersion_enabled.md)

## See Also

### Getting the supported layouts
- [cp_layer_renderer_capabilities_supported_layouts_count](./cp_layer_renderer_capabilities_supported_layouts_count.md)
  Returns the number of layouts the layer supports.
- [cp_layer_renderer_capabilities_supported_layout](./cp_layer_renderer_capabilities_supported_layout.md)
  Returns the layout at the specified index in the layer capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_supported_layouts_options)*