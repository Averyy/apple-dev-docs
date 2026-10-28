# cp_layer_renderer_configuration_get_drawable_render_context_stencil_format

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the pixel format to use for the stencil texture in drawable’s render context.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
MTLPixelFormat cp_layer_renderer_configuration_get_drawable_render_context_stencil_format(cp_layer_renderer_configuration_t configuration);
```

## Return Value

The pixel format to use for the drawable’s render context stencil textures.

## Parameters

- `configuration`: The layer configuration type that contains the information. The system passes an instance of this type to the [`makeConfiguration(capabilities:configuration:)`](./compositorlayerconfiguration/makeconfiguration%28capabilities,configuration%29.md) method of your configuration provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_get_drawable_render_context_stencil_format)*