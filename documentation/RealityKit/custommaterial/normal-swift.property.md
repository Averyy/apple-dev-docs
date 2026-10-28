# normal

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

A texture map that stores fine surface details for the entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
var normal: CustomMaterial.Normal { get set }
```

## Discussion

*Normal mapping* is a real-time rendering technique that captures fine surface details for a model by using a texture instead of increasing the number of polygons in the model. It works by storing *surface normals*, which are vectors perpendicular to the surface of the model, from a much higher-resolution version of the same 3D object. A normal map stores each vector in the image by storing the vectors’ `X`, `Y`, and `Z` values as the `R`, `G`, and `B` components of the corresponding pixel in the UV-mapped image.

For custom materials, [`normal`](./normal-swift.property.md) is only used when [`lightingModel`](./lightingmodel-swift.property.md) is [`CustomMaterial.LightingModel.lit`](./lightingmodel-swift.enum/lit.md) or [`CustomMaterial.LightingModel.clearcoat`](./lightingmodel-swift.enum/clearcoat.md) and its surface shader calls `params.surface().set_normal(). T`he normal map texture is still available to your surface shader function when using [`CustomMaterial.LightingModel.unlit`](./lightingmodel-swift.enum/unlit.md).

The following code loads a normal map texture and uses it to set this property:

```swift
if let normalResource = try? TextureResource.load(named:"entity_normals") {
    let normalMap = MaterialParameters.Texture(normalResource)
    material.normal = .init(texture:normalMap)
}
```

The following Metal code shows how to sample the normal map texture in a surface shader and use it to set the fragment’s surface normal:

```cpp
// Retrieve the entity's texture coordinates.
float2 uv = params.geometry().uv0();

// Entities loaded from USDZ or .reality files have texture coordinates
// with a flipped y-axis. This adjusts for that.
uv.y = 1.0 - uv.y;

// Sample the normal map to get the surface normal for this fragment.
auto tex = params.textures();
float3 color = (float3)tex.normal().sample(textureSampler, uv).rgb;

// Set the fragment's surface normal using the sampled value.
params.surface().set_normal(color);
```

For more information on creating custom materials and writing shader functions, see [Modifying RealityKit rendering using custom materials](../modifying-realitykit-rendering-using-custom-materials.md).

## See Also

### Setting the core properties
- [var baseColor: CustomMaterial.BaseColor](./basecolor-swift.property.md)
  The color of an entity unmodified by lighting.
- [var roughness: CustomMaterial.Roughness](./roughness-swift.property.md)
  The amount the surface of the 3D object scatters reflected light.
- [var metallic: CustomMaterial.Metallic](./metallic-swift.property.md)
  The reflectiveness of an entity.
- [var emissiveColor: CustomMaterial.EmissiveColor](./emissivecolor-swift.property.md)
  The color of light this material emits.
- [var ambientOcclusion: CustomMaterial.AmbientOcclusion](./ambientocclusion-swift.property.md)
  The ambient light exposure for a material.
- [var specular: CustomMaterial.Specular](./specular-swift.property.md)
  The bright highlights to apply to the entity.
- [var clearcoat: CustomMaterial.Clearcoat](./clearcoat-swift.property.md)
  The transparent highlights that simulate a clear, shiny coating on an entity.
- [var clearcoatRoughness: CustomMaterial.ClearcoatRoughness](./clearcoatroughness-swift.property.md)
  The degree to which an entity’s clear, shiny coating scatters light to create soft highlights.
- [var clearcoatNormal: CustomMaterial.ClearcoatNormal](./clearcoatnormal-swift.property.md)
  Waviness and imperfections for the top clearcoat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/normal-swift.property)*