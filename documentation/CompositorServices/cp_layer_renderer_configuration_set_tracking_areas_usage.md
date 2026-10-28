# cp_layer_renderer_configuration_set_tracking_areas_usage

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Sets the texture usage for the layer’s tracking areas textures to the specified value.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
void cp_layer_renderer_configuration_set_tracking_areas_usage(cp_layer_renderer_configuration_t configuration, MTLTextureUsage tracking_areas_usage);
```

## Discussion

Use this function to modify the configuration details for your layer.

## Parameters

- `configuration`: The layer configuration type to modify. The system passes an instance of this type to the [`makeConfiguration(capabilities:configuration:)`](./compositorlayerconfiguration/makeconfiguration%28capabilities,configuration%29.md) method of your configuration provider.
- `tracking_areas_usage`: The usage value to apply to the layer’s tracking areas textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_set_tracking_areas_usage)*