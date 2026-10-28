# cp_layer_renderer_capabilities_supported_layout

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the layout at the specified index in the layer capabilities.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
cp_layer_renderer_layout cp_layer_renderer_capabilities_supported_layout(cp_layer_renderer_capabilities_t layer_capabilities, cp_supported_layouts_options options, size_t index);
```

## Return Value

The layout at the specified index.

## Discussion

Use this function to determine what texture layouts are available for you to use.

## Parameters

- `layer_capabilities`: The layer capabilities to query.
- `options`: A bitmask of options that correspond to layout capabilities. Specify the same options you passed to the [`cp_layer_renderer_capabilities_supported_layouts_count`](./cp_layer_renderer_capabilities_supported_layouts_count.md) function.
- `index`: A zero-based index into the list of supported layouts. This index must be less than the value the [`cp_layer_renderer_capabilities_supported_layouts_count`](./cp_layer_renderer_capabilities_supported_layouts_count.md) function returns.

## See Also

### Getting the supported layouts
- [cp_layer_renderer_capabilities_supported_layouts_count](./cp_layer_renderer_capabilities_supported_layouts_count.md)
  Returns the number of layouts the layer supports.
- [cp_supported_layouts_options](./cp_supported_layouts_options.md)
  The options you can pass to functions that relate to rendering capabilities and layout support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_capabilities_supported_layout)*