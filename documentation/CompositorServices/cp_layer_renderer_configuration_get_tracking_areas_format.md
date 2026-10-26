# cp_layer_renderer_configuration_get_tracking_areas_format

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the pixel format to apply to the layer’s tracking areas textures.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
MTLPixelFormat cp_layer_renderer_configuration_get_tracking_areas_format(cp_layer_renderer_configuration_t configuration);
```

#### Return Value

The pixel format to apply to the layer’s tracking areas textures.

#### Discussion

The compositor creates the tracking areas textures using the pixel format information you provide.

## Parameters

- `configuration`: The layer configuration type that contains the information. The system passes an instance of this type to the [`makeConfiguration(capabilities:configuration:)`](./compositorlayerconfiguration/makeconfiguration%28capabilities,configuration%29.md) method of your configuration provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_get_tracking_areas_format)*