# cp_layer_renderer_configuration_get_max_render_quality

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Get max render quality the layer can use when drawing to the drawables.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
cp_render_quality_t cp_layer_renderer_configuration_get_max_render_quality(cp_layer_renderer_configuration_t configuration);
```

#### Return Value

The max render qualityto use for the drawable’s.

#### Discussion

The max render quality is a value between [0, 1]. This determines the max render quality at which drawing can happen.

Setting a higher max render quality will impact the resolution that is allocated for the drawable textures. This memory will count against the app’s memory limit so should only be specified as high as renderer can reasonably achieve frame rate at. During runtime, the render quality can be changed on the layer renderer but will not impact memory usage, see [`cp_layer_renderer_set_render_quality`](./cp_layer_renderer_set_render_quality.md).

## Parameters

- `configuration`: The layer configuration type to modify. The system passes an instance of this type to the [`makeConfiguration(capabilities:configuration:)`](./compositorlayerconfiguration/makeconfiguration%28capabilities,configuration%29.md) method of your configuration provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_get_max_render_quality)*