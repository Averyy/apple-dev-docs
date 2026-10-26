# cp_layer_renderer_capabilities_get_default_render_quality

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns default render quality for drawing on this platform.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
cp_render_quality_t cp_layer_renderer_capabilities_get_default_render_quality(cp_layer_renderer_capabilities_t layer_capabilities);
```

#### Return Value

The default render quality allowed for drawing.

#### Discussion

This should be used as a base value for the platform quality for drawing.

for usage.

## Parameters

- `layer_capabilities`: The layer capabilities to query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_capabilities_get_default_render_quality)*