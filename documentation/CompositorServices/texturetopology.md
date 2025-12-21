# TextureTopology

**Framework**: Compositor Services  
**Kind**: struct

A type that specifies the organization of one of the drawable’s textures.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct TextureTopology
```

#### Overview

Metal supports multiple organizations for the textures you use for drawing. Use this type to identify one of the organizations available to use in your app.

## Topics

### Getting the topology type
- [var textureType: MTLTextureType](texturetopology/texturetype.md)
  The texture type value that specifies how the underlying texture organizes its views.
### Getting the array length
- [var arrayLength: UInt64](texturetopology/arraylength.md)
  The number of items in the texture array.
### Creating a topology
- [init()](texturetopology/init.md)
  Creates a texture topology.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [var textureTopologies: [TextureTopology]](layerrenderer/properties-swift.struct/texturetopologies.md)
  The texture topologies available for the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/texturetopology)*