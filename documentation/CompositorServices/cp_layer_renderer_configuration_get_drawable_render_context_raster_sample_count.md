# cp_layer_renderer_configuration_get_drawable_render_context_raster_sample_count

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the raster sample count to use in drawable’s render context.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
int cp_layer_renderer_configuration_get_drawable_render_context_raster_sample_count(cp_layer_renderer_configuration_t configuration);
```

## Return Value

The raster sample count to use for the drawable’s render context.

## Parameters

- `configuration`: The layer configuration type that contains the information. The system passes an instance of this type to the [`makeConfiguration(capabilities:configuration:)`](./compositorlayerconfiguration/makeconfiguration%28capabilities,configuration%29.md) method of your configuration provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_get_drawable_render_context_raster_sample_count)*