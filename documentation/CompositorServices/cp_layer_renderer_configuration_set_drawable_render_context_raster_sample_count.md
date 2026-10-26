# cp_layer_renderer_configuration_set_drawable_render_context_raster_sample_count

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Sets the raster sample count for the drawable’s render context to the specified value.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
void cp_layer_renderer_configuration_set_drawable_render_context_raster_sample_count(cp_layer_renderer_configuration_t configuration, int raster_sample_count);
```

## Parameters

- `configuration`: The layer configuration type to modify. The system passes an instance of this type to the [`makeConfiguration(capabilities:configuration:)`](./compositorlayerconfiguration/makeconfiguration%28capabilities,configuration%29.md) method of your configuration provider.
- `raster_sample_count`: The raster sample count to apply to the drawable’s render context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_set_drawable_render_context_raster_sample_count)*