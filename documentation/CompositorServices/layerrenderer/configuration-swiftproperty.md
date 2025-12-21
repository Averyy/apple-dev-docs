# configuration

**Framework**: Compositor Services  
**Kind**: property

The configuration details for the specified layer.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var configuration: LayerRenderer.Configuration { get }
```

#### Discussion

Use the information in this property to set up your rendering loop. The layer ignores any modifications you make to the specified configuration data. To properly configure the layer, specify those details in the initializer for your [`CompositorLayer`](compositorlayer.md) type.

## See Also

- [LayerRenderer.Configuration](layerrenderer/configuration-swift.struct.md)
  A type that stores the texture formats, layout information, and other details you use to configure your rendering loop code.
- [LayerRenderer.Capabilities](layerrenderer/capabilities.md)
  The color formats, depth formats, and features that you can use to configure your rendering engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/configuration-swift.property)*