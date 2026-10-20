# baseColor

**Framework**: RealityKit  
**Kind**: property

The color of an entity unmodified by lighting.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
var baseColor: CustomMaterial.BaseColor { get set }
```

#### Discussion

In physically based rendering, the base color of an entity is its color before RealityKit applies any lighting calculations or other rendering calculations to it. With custom materials, the base color `texture` and `tint` are available as inputs in your surface shader. With custom materials, RealityKit doesn’t automatically use the values set on the [`baseColor`](custommaterial/basecolor-swift.property.md) property. The material’s surface shader is responsible for calculating or setting the actual base color value for rendering by calling `params.surface().set_base_color()`.

The following code shows how to create a base color from a tint color and a texture, and then assign it to a custom material:

```swift
// Load entity_basecolor.jpg from the app's bundle.
if let baseResource = try? TextureResource.load(named: "entity_basecolor") {
    let baseColor = CustomMaterial.Texture(baseResource)
    customMaterial.baseColor = CustomMaterial.BaseColor(tint: .blue,
                                                        texture:baseColor)
}
```

In your surface shader, you can access the `tint` of the material’s base color property by calling `params.material_constants().base_color_tint()`. You can access the texture by calling `params.textures().base_color()`.

The following surface shader function takes the tint and texture values from the [`baseColor`](custommaterial/basecolor-swift.property.md) property, multiplies them together, and sets the resulting value as the base color for rendering, which emulates the behavior of [`PhysicallyBasedMaterial`](physicallybasedmaterial.md):

```cpp
#include <metal_stdlib>
#include <RealityKit/RealityKit.h>
using namespace metal;

// Use samplers to retrieve a color value from a texture based on // UV
coordinates. Samplers can be reused with different textures. //
RealityKit reserves eight samplers for itself, so surface shaders should
// never define more than eight samplers. constexpr sampler
textureSampler(address::clamp_to_edge, filter::bicubic);

[[visible]] void mySurfaceShader(realitykit::surface_parameters params)
{
    // Retrieve the base color tint from the CustomMaterial.
    half3 baseColorTint = (half3)params.material_constants().base_color_tint();

    // Sample a value from the CustomMaterial's base color texture
    // using the entity's UV coordinates.
    auto uv = params.geometry().uv0();
    auto tex = params.textures();
    half3 color = (half3)tex.base_color().sample(textureSampler, uv).rgb;

    // Multiply the tint and color sampled from the base color texture and
    // assign the result to the shader's base color property.
    color *= baseColorTint;
    params.surface().set_base_color(color);
}
```

For more information on creating custom materials and writing shader functions, see [`Modifying RealityKit rendering using custom materials`](modifying-realitykit-rendering-using-custom-materials.md).

## See Also

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
- [var clearcoatNormal: CustomMaterial.ClearcoatNormal](custommaterial/clearcoatnormal-swift.property.md)
  Waviness and imperfections for the top clearcoat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/basecolor-swift.property)*