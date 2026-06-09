# bentNormal

**Framework**: RealityKit  
**Kind**: property

The bent normal map for the entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var bentNormal: PhysicallyBasedMaterial.BentNormal { get set }
```

#### Discussion

*Bent normal mapping* describes the average direction of least occlusion at each surface point. This is used to modulate lighting intensity and direction of the material. Use with ambient occlusion to improve the accuracy of indirect diffuse lighting. You can generate bent normals maps from a 3D software package.

The following code loads a bent normal map texture and uses it to set this property:

```swift
if let bentNormalResource = try? TextureResource.load(named:"entity_bentNormalMap") {
    let bentNormalMap = PhysicallyBasedMaterial.Texture(bentNormalResource)
    material.bentNormal = .init(texture: bentNormalMap)
}
```

## See Also

- [PhysicallyBasedMaterial.BentNormal](physicallybasedmaterial/bentnormal-swift.struct.md)
  The bent normal map for the entity.
- [var enableSpecularOcclusion: Bool](physicallybasedmaterial/enablespecularocclusion.md)
  Enables specular occlusion computations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/bentnormal-swift.property)*