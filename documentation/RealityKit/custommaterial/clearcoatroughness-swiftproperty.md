# clearcoatRoughness

**Framework**: RealityKit  
**Kind**: property

The degree to which an entity’s clear, shiny coating scatters light to create soft highlights.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
var clearcoatRoughness: CustomMaterial.ClearcoatRoughness { get set }
```

#### Discussion

An entity in RealityKit can display a clearcoat, which is a separate layer of transparent specular highlights used to simulate a clear coating, like on a car or the surface of lacquered objects. This property allows you to specify a clearcoat roughness value to indicate how much the clearcoat scatters light that bounces off of it, which softens and disperses the highlights.

You can specify a single value that applies to the entire material, or you can supply a UV-mapped image texture containing different roughness values for different parts of the entity. This value is available in your surface shader. RealityKit won’t render a clearcoat with roughness unless your surface shader calls both `params.surface().set_clearcoat_roughness()` and `params.surface().set_clearcoat()` with a value greater than `0.0`.

The following Swift code demonstrates setting the `clearcoatRoughness` using a single value:

```swift
material.clearcoatRoughness = .init(floatLiteral: 0.5)
```

This example shows how to set the `clearcoatRoughness` using a UV-mapped image:

```swift
if let clearcoatRoughnessResource = try?
TextureResource.load(named: "entity_cc_roughness") {
    let ccRoughnessMap = MaterialParameters.Texture(clearcoatRoughnessResource)
    material.clearcoat = .init(texture: ccRoughnessMap)
}
```

With custom materials, RealityKit only renders a clearcoat if [`lightingModel`](custommaterial/lightingmodel-swift.property.md) is [`CustomMaterial.LightingModel.clearcoat`](custommaterial/lightingmodel-swift.enum/clearcoat.md) and the material’s surface shader function calls `params.surface().set_clearcoat()`. To specify [`clearcoatRoughness`](custommaterial/clearcoatroughness-swift.property.md), your surface shader function needs to also call `params.surface().set_clearcoat_roughness()`.

The following Metal code demonstrates using [`clearcoat`](custommaterial/clearcoat-swift.property.md) and [`clearcoatRoughness`](custommaterial/clearcoatroughness-swift.property.md) in a surface shader, replicating the behavior of the [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) shader:

```cpp
// Retrieve the clearcoat scale and roughness from the CustomMaterial.
float clearcoatScale = params.material_constants().clearcoat_scale();
float clearcoatRoughnessScale = params.material_constants().clearcoat_roughness_scale();

// Retrieve the entity's texture coordinates.
float2 uv = params.geometry().uv0();

// Entities loaded from a USDZ or .reality file use texture coordinates with
// a flipped y-axis. This compensates for that.
uv.y = 1.0 - uv.y;

// Sample a value from the clearcoat and clearcoat roughness textures.
auto tex = params.textures();
half clearcoat = tex.clearcoat().sample(textureSampler, uv).r;
half clearcoatRoughness = tex.clearcoat_roughness().sample(textureSampler, uv).r;

// Multiply the scale and sampled texture value from the clearcoat and
// assign  the result.
clearcoat *= clearcoatScale;
params.surface().set_clearcoat(clearcoat);

// Multiply the scale and sampled texture value from the clearcoat roughness
// and assign the result.
clearcoatRoughness *= clearcoatRoughnessScale;
params.surface().set_clearcoat_roughness(clearcoatRoughness);
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
- [var clearcoatNormal: CustomMaterial.ClearcoatNormal](custommaterial/clearcoatnormal-swift.property.md)
  Waviness and imperfections for the top clearcoat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/clearcoatroughness-swift.property)*