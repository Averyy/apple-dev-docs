# clearcoatNormal

**Framework**: RealityKit  
**Kind**: property

Waviness and imperfections for the top clearcoat.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+

## Declaration

```swift
var clearcoatNormal: CustomMaterial.ClearcoatNormal { get set }
```

#### Discussion

An entity in RealityKit can display a clearcoat, which is a separate layer of transparent specular highlights used to simulate a clear coating, like on a car or the surface of lacquered objects. This property allows you to specify a clearcoat normal and add waviness and imperfections to the top clearcoat.

This example shows how to set the `clearcoatNormal` using a UV-mapped image:

```swift
if let clearcoatNormalTextureResource = try?
TextureResource.load(named: "entity_cc_normalMap") {
    let ccNormalMap = CustomMaterial.Texture(clearcoatNormalTextureResource)
    material.clearcoatNormal = .init(texture: ccNormalMap)
}
```

With custom materials, RealityKit only renders a clearcoat if [`lightingModel`](custommaterial/lightingmodel-swift.property.md) is [`CustomMaterial.LightingModel.clearcoat`](custommaterial/lightingmodel-swift.enum/clearcoat.md) and the material’s surface shader function calls `params.surface().set_clearcoat()`. To specify [`clearcoatNormal`](custommaterial/clearcoatnormal-swift.property.md), your surface shader function also needs to call `params.surface().set_clearcoat_normal()`.

The following Metal code demonstrates using [`clearcoat`](custommaterial/clearcoat-swift.property.md) and [`clearcoatNormal`](custommaterial/clearcoatnormal-swift.property.md) in a surface shader, replicating the behavior of the [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) shader:

```cpp
// Retrieve the entity's texture coordinates.
float2 uv = params.geometry().uv0();

// Entities loaded from a USDZ or .reality file use texture coordinates with
// a flipped y-axis. This compensates for that.
uv.y = 1.0 - uv.y;

// Sample a value from the clearcoat normal texture.
auto tex = params.textures();
half3 clearcoatNormal = realitykit::unpack_normal(tex.clearcoat_normal().sample(textureSampler, uv).rgb);

// assign the result.
params.surface().set_clearcoat_normal(clearcoatNormal);
params.surface().set_clearcoat(1.0);
```

## See Also

- [var baseColor: CustomMaterial.BaseColor](custommaterial/basecolor-swift.property.md)
  The color of an entity unmodified by lighting.
- [var roughness: CustomMaterial.Roughness](custommaterial/roughness-swift.property.md)
  The amount the surface of the 3D object scatters reflected light.
- [var metallic: CustomMaterial.Metallic](custommaterial/metallic-swift.property.md)
  The reflectiveness of an entity.
- [var normal: CustomMaterial.Normal](custommaterial/normal-swift.property.md)
  A texture map that stores fine surface details for the entity.
- [var emissiveColor: CustomMaterial.EmissiveColor](custommaterial/emissivecolor-swift.property.md)
  The color of light this material emits.
- [var ambientOcclusion: CustomMaterial.AmbientOcclusion](custommaterial/ambientocclusion-swift.property.md)
  The ambient light exposure for a material.
- [var specular: CustomMaterial.Specular](custommaterial/specular-swift.property.md)
  The bright highlights to apply to the entity.
- [var clearcoat: CustomMaterial.Clearcoat](custommaterial/clearcoat-swift.property.md)
  The transparent highlights that simulate a clear, shiny coating on an entity.
- [var clearcoatRoughness: CustomMaterial.ClearcoatRoughness](custommaterial/clearcoatroughness-swift.property.md)
  The degree to which an entity’s clear, shiny coating scatters light to create soft highlights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/clearcoatnormal-swift.property)*