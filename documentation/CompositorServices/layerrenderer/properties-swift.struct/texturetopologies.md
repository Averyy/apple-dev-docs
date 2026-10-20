# textureTopologies

**Framework**: Compositor Services  
**Kind**: property  
**Role**: Instance Property

The texture topologies available for the layer.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
var textureTopologies: [TextureTopology] { get }
```

#### Discussion

Use the topology information to allocate the resources you need to manage your Metal data structures.

## See Also

### Getting the layer’s texture topology
- [struct TextureTopology](../../texturetopology.md)
  A type that specifies the organization of one of the drawable’s textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/properties-swift.struct/texturetopologies)*