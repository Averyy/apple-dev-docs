# MDLMaterialFace

**Framework**: Model I/O  
**Kind**: enum

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum MDLMaterialFace
```

## Topics

### Constants
- [MDLMaterialFace.back](mdlmaterialface/back.md)
- [MDLMaterialFace.doubleSided](mdlmaterialface/doublesided.md)
- [MDLMaterialFace.front](mdlmaterialface/front.md)
### Initializers
- [init?(rawValue: UInt)](mdlmaterialface/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum MDLCameraProjection](mdlcameraprojection.md)
  Options for camera projection styles, used by the [`projection`](mdlcamera/projection.md) property.
- [enum MDLGeometryType](mdlgeometrytype.md)
  Types of geometric primitives for rendering a submesh, used by the [`geometryType`](mdlsubmesh/geometrytype.md) property.
- [enum MDLIndexBitDepth](mdlindexbitdepth.md)
  Options for the size of integer data in a submesh’s index buffer, used by the [`indexType`](mdlsubmesh/indextype.md) property.
- [enum MDLLightType](mdllighttype.md)
  Options for the shape and style of illumination provided by a light, used by the [`lightType`](mdllight/lighttype.md) property.
- [enum MDLMaterialMipMapFilterMode](mdlmaterialmipmapfiltermode.md)
  Modes for sampling textures at sizes between mipmap levels, used by the [`mipFilter`](mdltexturefilter/mipfilter.md) property.
- [enum MDLMaterialPropertyType](mdlmaterialpropertytype.md)
  Options for the data type of a material property, used by the [`type`](mdlmaterialproperty/type.md) property.
- [enum MDLMaterialSemantic](mdlmaterialsemantic.md)
  Options for the semantic use of a material property’s value in rendering a particular surface appearance; used by the [`semantic`](mdlmaterialproperty/semantic.md) property.
- [enum MDLMaterialTextureFilterMode](mdlmaterialtexturefiltermode.md)
  Modes for sampling textures at coordinates between texels, used by the [`minFilter`](mdltexturefilter/minfilter.md) and [`magFilter`](mdltexturefilter/magfilter.md) properties.
- [enum MDLMaterialTextureWrapMode](mdlmaterialtexturewrapmode.md)
  Modes for sampling textures at coordinates outside the texture bounds, used by the [`sWrapMode`](mdltexturefilter/swrapmode.md), [`tWrapMode`](mdltexturefilter/twrapmode.md), and [`rWrapMode`](mdltexturefilter/rwrapmode.md) properties.
- [enum MDLMeshBufferType](mdlmeshbuffertype.md)
  Options for the content of a mesh buffer, used by the [`type`](mdlmeshbuffer/type.md) property and by [`MDLMeshBufferAllocator`](mdlmeshbufferallocator.md) methods for creating buffers.
- [enum MDLProbePlacement](mdlprobeplacement.md)
  Options affecting automatic placement of light probes in a scene, used with the [`placeLightProbes(withDensity:heuristic:using:)`](mdlasset/placelightprobes(withdensity:heuristic:using:).md) method.
- [enum MDLTextureChannelEncoding](mdltexturechannelencoding.md)
  Options for the data size and type of texel channel values, used by the [`channelEncoding`](mdltexture/channelencoding.md) property.
- [enum MDLVertexFormat](mdlvertexformat.md)
  Descriptions of the data size and layout for a vertex attribute, used by the [`format`](mdlvertexattribute/format.md) property.
- [enum MDLAnimatedValueInterpolation](mdlanimatedvalueinterpolation.md)
- [enum MDLDataPrecision](mdldataprecision.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterialface)*