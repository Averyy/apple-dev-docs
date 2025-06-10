# emissiveColor

**Framework**: RealityKit  
**Kind**: property

The color of light this material emits.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
var emissiveColor: CustomMaterial.EmissiveColor { get set }
```

#### Discussion

With physically based rendering (PBR), you can give entities in RealityKit the appearance of emitting light. Use this property to simulate real-world objects that glow, such as objects with LEDs or computer screens. To enable light emission from a material, set [`emissiveIntensity`](physicallybasedmaterial/emissiveintensity.md) to a value greater than zero, then specify a color (other than black) using this property. You can specify a single emissive color for the entire material, or use a UV-mapped image texture to use different colors for different parts of the entity.

With custom materials, RealityKit doesn’t use [`emissiveColor`](custommaterial/emissivecolor-swift.property.md) automatically to render your entity. Call `params.surface().set_emissive_color()` from your surface shader, otherwise RealityKit renders no light emission.

The following example assigns a tint color to the [`emissiveColor`](physicallybasedmaterial/emissivecolor-swift.property.md) property, without a texture:

```swift
self.emissiveColor = PhysicallyBasedMaterial.EmissiveColor(color: .red)
```

This next example uses a texture to specify the [`emissiveColor`](physicallybasedmaterial/emissivecolor-swift.property.md) property:

```swift
if let emissiveResource = try? TextureResource.load(named: "entity_emissive") {
    let emissiveMap = MaterialParameters.Texture(emissiveResource)
    material.emissiveColor = .init(texture: emissiveMap)
}
```

This Metal code shows how to access the emissive color tint in your shader functions:

```cpp
half3 emissiveTint = (half3)params.material_constants().emissive_color();
```

The following Metal code demonstrates how to sample the emissive color texture for the current fragment:

```cpp
// Get the entity's primary texture coordinates.
float2 uv = params.geometry().uv0();

// Flip the y-axis. You only need to do this for entities you load from
// USDZ or .reality files.
uv.y = 1.0 - uv.y;

// Sample the emissive color texture to get the value for this fragment.
auto tex = params.textures();
half3 emissiveColor = (half3)tex.emissive_color()
    .sample(textureSampler, uv).rgb;
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/emissivecolor-swift.property)*