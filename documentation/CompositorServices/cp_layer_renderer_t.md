# cp_layer_renderer_t

**Framework**: Compositor Services  
**Kind**: typealias  
**Role**: Type Alias

A type that provides the Metal types and timing information you need to draw your content.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
typedef CP_OBJECT_cp_layer_renderer * cp_layer_renderer_t;
```

#### Discussion

A layer renderer type creates a bridge between a SwiftUI scene and the Metal code you use to draw fully immersive experiences. When you present an immersive space with [`CompositorLayer`](./compositorlayer.md) content, the system creates a [`LayerRenderer`](./layerrenderer.md) type and makes it available to the content’s closure. Use the information in the layer to set up your app’s rendering loop, and to start drawing frames of content.

Each layer has information that tells the system how to configure the Metal textures and data types your app needs. Compositor Services provides a default configuration for layers, but you can customize the configuration of your layer as needed. Specify your custom configuration details using the [`CompositorLayerConfiguration`](./compositorlayerconfiguration.md) protocol and pass a type with those details to the initializer for your immersive space’s content . Use the layer’s capability information to validate any configuration choices you make.

For information about how to create and configure a layer and use it to run your rendering loop, see [Drawing fully immersive content using Metal](./drawing-fully-immersive-content-using-metal.md).

## See Also

### Getting the layer type
- [class LayerRenderer](./layerrenderer.md)
  A type that provides the Metal types and timing information you need to draw your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_t)*