# clearcoat

**Framework**: RealityKit  
**Kind**: property

The transparent highlights that simulate a clear, shiny coating on an entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var clearcoat: PhysicallyBasedMaterial.Clearcoat { get set }
```

#### Discussion

An entity in RealityKit can display a clearcoat, which is a separate layer of transparent specular highlights used to simulate a clear transparent coating, like the paint on a car, or the surface of lacquered objects. By default, materials don’t have clearcoat enabled.

Use this property to enable clearcoat rendering. Specifying any value greater than `0.0` turns clearcoat rendering on. A value of `1.0` indicates a full clearcoat. RealityKit treats values above `1.0` as if they’re `1.0`.

You can specify [`clearcoat`](physicallybasedmaterial/clearcoat-swift.property.md) using a single `Float` that applies to the entire material, or a UV-mapped grayscale image to provide different values for different parts of an entity.

The following example specifies `clearcoat` using a single value:

```swift
material.clearcoat = .init(floatLiteral: 0.8)
```

And this example shows how to specify `clearcoat` using a UV-mapped image texture:

```swift
if let clearcoatResource = try? TextureResource.load(named:"entity_clearcoat") {
    let clearcoatMap = MaterialParameters.Texture(clearcoatResource)
    material.clearcoat = .init(texture: clearcoatMap)
}
```

## See Also

- [var baseColor: PhysicallyBasedMaterial.BaseColor](physicallybasedmaterial/basecolor-swift.property.md)
  The color of an entity unmodified by lighting.
- [var roughness: PhysicallyBasedMaterial.Roughness](physicallybasedmaterial/roughness-swift.property.md)
  The amount the surface of the 3D object scatters reflected light.
- [var metallic: PhysicallyBasedMaterial.Metallic](physicallybasedmaterial/metallic-swift.property.md)
  The reflectiveness of an entity.
- [var normal: PhysicallyBasedMaterial.Normal](physicallybasedmaterial/normal-swift.property.md)
  The normal map for the entity.
- [var ambientOcclusion: PhysicallyBasedMaterial.AmbientOcclusion](physicallybasedmaterial/ambientocclusion-swift.property.md)
  The ambient occlusion values for a material.
- [var specular: PhysicallyBasedMaterial.Specular](physicallybasedmaterial/specular-swift.property.md)
  The specular highlight applied to the entity.
- [var clearcoatRoughness: PhysicallyBasedMaterial.ClearcoatRoughness](physicallybasedmaterial/clearcoatroughness-swift.property.md)
  The degree to which an entity’s clear, shiny coating scatters light to create soft highlights.
- [var clearcoatNormal: PhysicallyBasedMaterial.ClearcoatNormal](physicallybasedmaterial/clearcoatnormal-swift.property.md)
  Waviness and imperfections for the top clearcoat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/clearcoat-swift.property)*