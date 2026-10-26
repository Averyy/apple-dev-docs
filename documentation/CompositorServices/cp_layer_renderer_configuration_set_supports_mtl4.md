# cp_layer_renderer_configuration_set_supports_mtl4

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Set whether the layer can use Metal4 when drawing to the drawables.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
void cp_layer_renderer_configuration_set_supports_mtl4(cp_layer_renderer_configuration_t configuration, bool supports_mtl4);
```

## Parameters

- `configuration`: The layer configuration type to modify. The system passes an instance of this type to the [`makeConfiguration(capabilities:configuration:)`](./compositorlayerconfiguration/makeconfiguration%28capabilities,configuration%29.md) method of your configuration provider.
- `supports_mtl4`: Whether the layer supports using Metal4, otherwise defaults to Metal3.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_set_supports_mtl4)*