# cp_layer_renderer_configuration_get_supports_mtl4

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Get whether the layer can use Metal4 when drawing to the drawables.

**Availability**:
- macOS
- visionOS 26.0+

## Declaration

```c
bool cp_layer_renderer_configuration_get_supports_mtl4(cp_layer_renderer_configuration_t configuration);
```

## Return Value

Whether the layer supports using Metal4, otherwise defaults to Metal3.

## Parameters

- `configuration`: The layer configuration type to modify. The system passes an instance of this type to the [`makeConfiguration(capabilities:configuration:)`](./compositorlayerconfiguration/makeconfiguration%28capabilities,configuration%29.md) method of your configuration provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_get_supports_mtl4)*