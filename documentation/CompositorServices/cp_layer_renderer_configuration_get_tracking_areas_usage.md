# cp_layer_renderer_configuration_get_tracking_areas_usage

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the texture usage value to apply to the layer’s tracking areas textures.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
MTLTextureUsage cp_layer_renderer_configuration_get_tracking_areas_usage(cp_layer_renderer_configuration_t configuration);
```

#### Return Value

The Metal texture usage value to apply to the layer’s tracking areas textures.

#### Discussion

Metal optimizes texture-related operations based on the texture’s usage value. The usage value can be a combination of options. For example, a texture might be readable and writable. For more information, see [`MTLTextureUsage`](../Metal/mtltextureusage.md).

## Parameters

- `configuration`: The layer configuration type that contains the information. The system passes an instance of this type to the [`makeConfiguration(capabilities:configuration:)`](./compositorlayerconfiguration/makeconfiguration%28capabilities,configuration%29.md) method of your configuration provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_get_tracking_areas_usage)*