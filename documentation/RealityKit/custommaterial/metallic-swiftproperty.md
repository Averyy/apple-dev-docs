# metallic

**Framework**: RealityKit  
**Kind**: property

The reflectiveness of an entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
var metallic: CustomMaterial.Metallic { get set }
```

#### Discussion

In physically based rendering, the `metallic` property represents the reflectiveness of an entity. Use this property to specify whether the entity displays metallic qualities and reflects the surrounding environment, or displays dielectric qualities and doesn’t reflect the environment. With custom materials, RealityKit doesn’t automatically use the values set on this property. To render a custom material using the metallic property, set [`lightingModel`](custommaterial/lightingmodel-swift.property.md) to [`CustomMaterial.LightingModel.lit`](custommaterial/lightingmodel-swift.enum/lit.md) or [`CustomMaterial.LightingModel.clearcoat`](custommaterial/lightingmodel-swift.enum/clearcoat.md) and call `params.surface().set_roughness()` from its surface shader.

![An illustration showing two spheres rendered in RealityKit. The sphere](https://docs-assets.developer.apple.com/published/905cfc9b323ae0c410a550342e2dc378/CustomMaterial-metallic-swift-property-1%402x.png)

The following Swift code shows how to use an image and a scale to specify roughness:

```swift
if let metallicResource = try? TextureResource.load(named:"entity_metallic") {
    let metallic = MaterialParameters.Texture(metallicResource)
    material.metallic = PhysicallyBasedMaterial.Metallic(scale: 1.0, texture:metallic)
}
```

The following surface shader takes the scale and texture values from the [`metallic`](custommaterial/metallic-swift.property.md) property, multiplies them together, and uses the result to specify the metallic value for rendering, which emulates the behavior of [`PhysicallyBasedMaterial`](physicallybasedmaterial.md).

```cpp
#include <metal_stdlib>
#include <RealityKit/RealityKit.h>
using namespace metal;

// Use samplers to retrieve a color value from a texture based on // the
entity's UV coordinates. Samplers can be reused with different textures.
// Surface shader functions should define no more than eight samplers.
constexpr sampler textureSampler(address::clamp_to_edge,
filter::bicubic);

[[visible]] void mySurfaceShader(realitykit::surface_parameters params)
{
    // Retrieve the metallic scale from the CustomMaterial.
    float metallicScale = params.material_constants().metallic_scale();

    // Retrieve the entity's texture coordinates.
    float2 uv = params.geometry().uv0();

    // Entities loaded from USDZ or .reality files have texture coordinates
    // with a flipped y-axis. This adjusts for that.
    uv.y = 1.0 - uv.y;

    // Sample the metallic texture based on the UV coordinates.
    auto tex = params.textures();
    half metallic = tex.metallic().sample(textureSampler, uv).r;

    // Multiply the tint and the sampled value from the texture,
    // and assign the result to the shader's metallic property.
    metallic *= metallicScale;
    params.surface().set_metallic(metallic);
}
```

For more information on creating custom materials and writing shader functions, see [`Modifying RealityKit rendering using custom materials`](modifying-realitykit-rendering-using-custom-materials.md).

## See Also

- [var baseColor: CustomMaterial.BaseColor](custommaterial/basecolor-swift.property.md)
  The color of an entity unmodified by lighting.
- [var roughness: CustomMaterial.Roughness](custommaterial/roughness-swift.property.md)
  The amount the surface of the 3D object scatters reflected light.
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
- [var clearcoatNormal: CustomMaterial.ClearcoatNormal](custommaterial/clearcoatnormal-swift.property.md)
  Waviness and imperfections for the top clearcoat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/metallic-swift.property)*