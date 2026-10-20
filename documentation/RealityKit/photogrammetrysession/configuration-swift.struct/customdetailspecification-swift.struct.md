# PhotogrammetrySession.Configuration.CustomDetailSpecification

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A structure for specifying various customizable options on the reconstructed model and textures.

**Availability**:
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct CustomDetailSpecification
```

## Topics

### Structures
- [PhotogrammetrySession.Configuration.CustomDetailSpecification.TextureMapOutputs](./customdetailspecification-swift.struct/texturemapoutputs.md)
  Allows specification of the set of output texture maps to be included in the output model.
### Initializers
- [init()](./customdetailspecification-swift.struct/init%28%29.md)
### Instance Properties
- [var maximumPolygonCount: UInt](./customdetailspecification-swift.struct/maximumpolygoncount.md)
  The upper limit on polygons in the model mesh.
- [var maximumTextureDimension: PhotogrammetrySession.Configuration.CustomDetailSpecification.TextureDimension](./customdetailspecification-swift.struct/maximumtexturedimension.md)
  The maximum dimension of the reconstructed texture maps.
- [var outputTextureMaps: PhotogrammetrySession.Configuration.CustomDetailSpecification.TextureMapOutputs](./customdetailspecification-swift.struct/outputtexturemaps.md)
  The set of texture maps to create in the model.
- [var textureFormat: PhotogrammetrySession.Configuration.CustomDetailSpecification.TextureFormat](./customdetailspecification-swift.struct/textureformat-swift.property.md)
  The data type of the texture map.
### Enumerations
- [PhotogrammetrySession.Configuration.CustomDetailSpecification.TextureDimension](./customdetailspecification-swift.struct/texturedimension.md)
  One of the discrete texture dimensions to specify the size of the model texture maps. For example, a `.twoK` dimension means the texture map size can be up to size 2048x2048.
- [PhotogrammetrySession.Configuration.CustomDetailSpecification.TextureFormat](./customdetailspecification-swift.struct/textureformat-swift.enum.md)
  The output format to use for all textures.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/configuration-swift.struct/customdetailspecification-swift.struct)*