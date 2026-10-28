# cp_layer_renderer_properties_t

**Framework**: Compositor Services  
**Kind**: typealias  
**Role**: Type Alias

A type that describes the organization of the layer’s textures and the relationships between those textures and the views you use for drawing.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
typedef CP_OBJECT_cp_layer_renderer_properties * cp_layer_renderer_properties_t;
```

## Discussion

Use the layer’s properties to configure other parts of your app. For example, use them to configure your app’s render pipeline.

You can obtain layer properties directly from your layer. If you don’t yet have the [`LayerRenderer`](./layerrenderer.md) type, you can create an equivalent set of properties using the initializer for this type.

## See Also

### Getting a layer’s properties
- [cp_layer_renderer_get_properties](./cp_layer_renderer_get_properties.md)
  Returns the configured properties of the specified layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_properties_t)*