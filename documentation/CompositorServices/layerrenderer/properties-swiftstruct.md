# LayerRenderer.Properties

**Framework**: Compositor Services  
**Kind**: struct

A type that describes the organization of the layer renderer’s textures and the relationships between those textures and the views you use for drawing.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct Properties
```

## Mentions

- [Drawing fully immersive content using Metal](drawing-fully-immersive-content-using-metal.md)

#### Overview

Use the layer’s properties to configure other parts of your app. For example, use them to configure your app’s render pipeline.

You can obtain layer properties directly from your layer. If you don’t yet have the [`LayerRenderer`](layerrenderer.md) type, you can create an equivalent set of properties using the initializer for this type.

## Topics

### Creating representative properties
- [init(configuration: LayerRenderer.Configuration) throws](layerrenderer/properties-swift.struct/init(configuration:).md)
  Creates a set of properties using the specified configuration values.
### Getting view port information
- [var viewCount: Int](layerrenderer/properties-swift.struct/viewcount.md)
  The number of views that you must fill with content.
### Getting the layer’s texture topology
- [var textureTopologies: [TextureTopology]](layerrenderer/properties-swift.struct/texturetopologies.md)
  The texture topologies available for the layer.
- [struct TextureTopology](texturetopology.md)
  A type that specifies the organization of one of the drawable’s textures.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)

## See Also

- [var properties: LayerRenderer.Properties](layerrenderer/properties-swift.property.md)
  The configured properties of the layer renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/properties-swift.struct)*