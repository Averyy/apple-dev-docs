# normal

**Framework**: RealityKit  
**Kind**: property

The normal map for the entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var normal: PhysicallyBasedMaterial.Normal { get set }
```

## Mentions

- [Applying realistic material and lighting effects to entities](applying-realistic-material-and-lighting-effects-to-entities.md)

#### Discussion

 is a real-time rendering technique that captures fine surface details for a model using a texture instead of increasing the number of polygons in the model. It works by storing , which are vectors perpendicular to the surface of the model, from a much higher resolution version of the same 3D object. A normal map stores each vector in the image by storing the vectors’ `X`, `Y`, and `Z` values as the `R`, `G`, and `B` components of the corresponding pixel in the UV-mapped image.

If you provide a normal map, RealityKit uses the normals stored in the image to do lighting calculations. This results in much more realistic highlights, shadows, and reflections without incurring the computational cost of using a much higher resolution 3D model. RealityKit uses tangent-space normal maps.

The following code loads a normal map texture and uses it to set this property:

```swift
if let normalResource = try? TextureResource.load(named:
"entity_normals") {
    let normalMap = MaterialParameters.Texture(normalResource)
    material.normal = PhysicallyBasedMaterial.Normal(texture:normalMap)
}
```

## See Also

- [var baseColor: PhysicallyBasedMaterial.BaseColor](physicallybasedmaterial/basecolor-swift.property.md)
  The color of an entity unmodified by lighting.
- [var roughness: PhysicallyBasedMaterial.Roughness](physicallybasedmaterial/roughness-swift.property.md)
  The amount the surface of the 3D object scatters reflected light.
- [var metallic: PhysicallyBasedMaterial.Metallic](physicallybasedmaterial/metallic-swift.property.md)
  The reflectiveness of an entity.
- [var ambientOcclusion: PhysicallyBasedMaterial.AmbientOcclusion](physicallybasedmaterial/ambientocclusion-swift.property.md)
  The ambient occlusion values for a material.
- [var specular: PhysicallyBasedMaterial.Specular](physicallybasedmaterial/specular-swift.property.md)
  The specular highlight applied to the entity.
- [var clearcoat: PhysicallyBasedMaterial.Clearcoat](physicallybasedmaterial/clearcoat-swift.property.md)
  The transparent highlights that simulate a clear, shiny coating on an entity.
- [var clearcoatRoughness: PhysicallyBasedMaterial.ClearcoatRoughness](physicallybasedmaterial/clearcoatroughness-swift.property.md)
  The degree to which an entity’s clear, shiny coating scatters light to create soft highlights.
- [var clearcoatNormal: PhysicallyBasedMaterial.ClearcoatNormal](physicallybasedmaterial/clearcoatnormal-swift.property.md)
  Waviness and imperfections for the top clearcoat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/normal-swift.property)*