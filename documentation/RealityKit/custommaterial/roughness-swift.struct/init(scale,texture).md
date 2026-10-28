# init(scale:texture:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a roughness object from a color or texture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
init(scale: Float = 1.0, texture: CustomMaterial.Texture? = nil)
```

## Discussion

Use this initializer to create an object to specify the amount of roughness using a single value or an image texture, or both.

The `roughness` property represents how much the surface of the entity scatters light that it reflects. A material with a high roughness has a matte appearance, and one with a low roughness has a shiny appearance.

![An illustration showing three spheres with different amounts of](https://developer.apple.com/tutorials/images/com.apple.RealityKit/CustomMaterial-Roughness-swift-struct-init(scale:texture:)-1@2x.png)

The following code demonstrates creating a roughness object using this initializer:

```swift
if let roughnessResource = try? TextureResource.load(named:
"entity_roughness") {
    let roughness = MaterialParameters.Texture(roughnessResource)
    customMaterial.roughness = .init(scale: 0.5, texture: roughness)
}
```

With custom materials, the `texture` and `scale` properties you set on the [`roughness`](../roughness-swift.property.md) property are available in your surface shader function, but RealityKit doesn’t automatically use them to render your entity. To render an entity with roughness, set [`lightingModel`](../lightingmodel-swift.property.md) to [`CustomMaterial.LightingModel.lit`](../lightingmodel-swift.enum/lit.md) or [`CustomMaterial.LightingModel.clearcoat`](../lightingmodel-swift.enum/clearcoat.md), and call `params.surface().set_roughness()` from its surface shader.

To achieve the same metallic behavior as [`PhysicallyBasedMaterial`](../../physicallybasedmaterial.md), the surface shader function multiplies the roughness scale by the sampled value from the roughness texture, as the following Metal code demonstrates:

```swift
    // Retrieve the roughness scale from the CustomMaterial.
    float roughnessScale = params.material_constants().roughness_scale();

    // Retrieve the entity's UV texture coordinates.
    float2 uv = params.geometry().uv0();

    // Models loaded from USDZ or Reality Composer use UVs that are flipped
    // on the y-axis. This compensates for that.
    uv.y = 1.0 - uv.y;

    // Sample the texture based on the resulting UVs.
    auto tex = params.textures();
    half roughness = tex.roughness().sample(textureSampler, uv).r;

    // Multiply the scale and the sampled value from the texture, and assign
    // the result to the shader's base color property.
    roughness *= roughnessScale;

    // Set the roughness value to be used by the custom material shader.
    params.surface().set_roughness(roughness);
```

For more information on creating custom materials and writing shader functions, see [Modifying RealityKit rendering using custom materials](../../modifying-realitykit-rendering-using-custom-materials.md).

## Parameters

- `scale`: The roughness value.
- `texture`: An optional image texture.

## See Also

### Creating a roughness object
- [init(floatLiteral: Float)](./init%28floatliteral%29.md)
  Creates an object to specify the amount of roughness, using a single value that applies to the entire material.
- [init(PhysicallyBasedMaterial.Roughness)](./init%28_%29.md)
  Creates a roughness object from a physically based material’s roughness property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/roughness-swift.struct/init(scale:texture:))*