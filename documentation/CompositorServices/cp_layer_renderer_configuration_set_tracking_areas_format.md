# cp_layer_renderer_configuration_set_tracking_areas_format

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Sets the pixel format for the layer’s tracking areas textures to the specified value.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
void cp_layer_renderer_configuration_set_tracking_areas_format(cp_layer_renderer_configuration_t configuration, MTLPixelFormat tracking_areas_format);
```

## Discussion

Use this function to modify the configuration details for your layer. Call the [`cp_layer_renderer_capabilities_supported_tracking_areas_format`](./cp_layer_renderer_capabilities_supported_tracking_areas_format.md) function to determine which pixel formats the layer’s tracking areas textures supports.

## Parameters

- `configuration`: The layer configuration type to modify. The system passes an instance of this type to the [`makeConfiguration(capabilities:configuration:)`](./compositorlayerconfiguration/makeconfiguration%28capabilities,configuration%29.md) method of your configuration provider.
- `tracking_areas_format`: The pixel format to apply to the layer’s tracking areas textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_set_tracking_areas_format)*