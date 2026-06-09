# enableSpecularOcclusion

**Framework**: RealityKit  
**Kind**: property

Enables specular occlusion computations.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var enableSpecularOcclusion: Bool { get set }
```

#### Discussion

When enabled, this property reduces specular highlights in areas that are occluded from ambient light, allowing for more realistic indirect lighting. This uses bent normal maps to modulate specular reflections based on ambient occlusion and roughness.

Specular occlusion is particularly useful for character rendering and complex surfaces where traditional ambient occlusion alone may not provide sufficient detail for realistic specular lighting.

> **Note**: This feature requires bent normal maps. Enable bent normals using [`bentNormal`](physicallybasedmaterial/bentnormal-swift.property.md).

```swift
material.enableSpecularOcclusion = boolean_value
```

## See Also

- [var bentNormal: PhysicallyBasedMaterial.BentNormal](physicallybasedmaterial/bentnormal-swift.property.md)
  The bent normal map for the entity.
- [PhysicallyBasedMaterial.BentNormal](physicallybasedmaterial/bentnormal-swift.struct.md)
  The bent normal map for the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/enablespecularocclusion)*