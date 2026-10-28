# cp_layer_renderer_configuration_get_layout

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the texture configuration for the drawable views in the layer.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
cp_layer_renderer_layout cp_layer_renderer_configuration_get_layout(cp_layer_renderer_configuration_t configuration);
```

## Return Value

The layout of the textures in the layer.

## Discussion

Layouts define how Compositor Services creates the color and depth textures it passes to your app. A layout might use separate textures for each view, or combine the content from multiple views into a single texture. The layout type also determines which Metal texture type the compositor creates for you. For more information about the supported layouts, see `cp_layer_renderer_layout`.

## Parameters

- `configuration`: The layer configuration details.

## See Also

### Configuring the texture layout
- [cp_layer_renderer_configuration_set_layout](./cp_layer_renderer_configuration_set_layout.md)
  Changes the layout configuration for the drawable views in the layer.
- [LayerRenderer.Layout](./layerrenderer/layout.md)
  Constants that specify the organization of the textures you use for drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_configuration_get_layout)*