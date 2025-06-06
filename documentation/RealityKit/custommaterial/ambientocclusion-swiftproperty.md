# ambientOcclusion

**Framework**: RealityKit  
**Kind**: property

The ambient light exposure for a material.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var ambientOcclusion: CustomMaterial.AmbientOcclusion { get set }
```

#### Discussion

Ambient occlusion (AO) represents the entity’s exposure to ambient light. Specify ambient occlusion using a UV-mapped image called an . In an AO map, black pixels represent parts of the model that receive no ambient light because of a crevice, dent, or recessed area, or another part of the entity blocking ambient light from reaching it. White pixels represent flat portions of the model that receive full ambient light. You generate ambient occlusion maps using a 3D software package.

The following code loads an ambient occlusion map and adds it to the custom material:

```swift
if let aoResource = try? TextureResource.load(named:"entity_ao") {
    let aoMap = MaterialParameters.Texture(aoResource)
    material.emissiveColor = .init(texture: aoMap)
}
```

In a custom material, RealityKit doesn’t automatically use the value you set on this property to render your entity. The ambient occlusion texture is available in the material’s shader functions, but RealityKit only renders ambient occlusion if the material’s [`lightingModel`](custommaterial/lightingmodel-swift.property.md) is [`CustomMaterial.LightingModel.lit`](custommaterial/lightingmodel-swift.enum/lit.md) or [`CustomMaterial.LightingModel.clearcoat`](custommaterial/lightingmodel-swift.enum/clearcoat.md) and its surface shader calls `params.surface().set_ambient_occlusion()`.

The following Metal code shows how to sample the ambient occlusion texture to set the AO value in a surface shader function:

```cpp
// Retrieve the entity's texture coordinates.
float2 uv = params.geometry().uv0();

// Entities loaded from USDZ or .reality files have texture coordinates
// with a flipped y-axis. This adjusts for that.
uv.y = 1.0 - uv.y;

// Sample the ambient occlusion texture and use it to set the
// ambient occlusion value to use during rendering.
auto tex = params.textures();
half metallic = tex.ambient_occlusion().sample(textureSampler, uv).r;
params.surface().set_ambient_occlusion(metallic);
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
- [var specular: CustomMaterial.Specular](custommaterial/specular-swift.property.md)
  The bright highlights to apply to the entity.
- [var clearcoat: CustomMaterial.Clearcoat](custommaterial/clearcoat-swift.property.md)
  The transparent highlights that simulate a clear, shiny coating on an entity.
- [var clearcoatRoughness: CustomMaterial.ClearcoatRoughness](custommaterial/clearcoatroughness-swift.property.md)
  The degree to which an entity’s clear, shiny coating scatters light to create soft highlights.
- [var clearcoatNormal: CustomMaterial.ClearcoatNormal](custommaterial/clearcoatnormal-swift.property.md)
  Waviness and imperfections for the top clearcoat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/ambientocclusion-swift.property)*