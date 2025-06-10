# init(scale:texture:)

**Framework**: RealityKit  
**Kind**: init

Creates a clearcoat object using a single value or a texture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
init(scale: Float = 1.0, texture: CustomMaterial.Texture? = nil)
```

#### Discussion

A clearcoat is a separate layer of transparent specular highlights used to simulate a clear coating, like on a car or the surface of lacquered objects. Use this initializer to create an object to specify the amount of clearcoat for a material using a single value for the entire material, a UV-mapped image to specify different values for different parts of the entity, or both.

The values from this property are available in the custom material’s surface shader function regardless of the value of [`lightingModel`](custommaterial/lightingmodel-swift.property.md) , but clearcoat isn’t drawn unless the custom material’s [`lightingModel`](custommaterial/lightingmodel-swift.property.md) is [`CustomMaterial.LightingModel.clearcoat`](custommaterial/lightingmodel-swift.enum/clearcoat.md) and the surface shader calls `params.surface().set_clearcoat()`.

The following Metal code demonstrates retrieving `scale` and `texture` in a surface shader, and using them to specify the clearcoat and clearcoat roughness values:

```swift
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
    half clearcoatRoughess = tex.clearcoat_roughness().sample(textureSampler, uv).r;

    // Multiply the scale and sampled texture value from the clearcoat
    // and assign the result.
    clearcoat *= clearcoatScale;
    params.surface().set_clearcoat(clearcoat);

    // Multiply the scale and sampled texture value from the clearcoat roughness
    // and assign the result.
    clearcoatRoughess *= clearcoatRoughnessScale;
    params.surface().set_clearcoat_roughness(clearcoatRoughess);
```

## Parameters

- `scale`: The clearcoat value for the entire material.
- `texture`: The clearcoat values as the texture of a UV-mapped image.

## See Also

- [init(floatLiteral: Float)](custommaterial/clearcoatroughness-swift.struct/init(floatliteral:).md)
  Creates a clearcoat object using a single value.
- [init(PhysicallyBasedMaterial.ClearcoatRoughness)](custommaterial/clearcoatroughness-swift.struct/init(_:).md)
  Creates a custom clearcoat object from a physically based material’s clearcoat property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/clearcoatroughness-swift.struct/init(scale:texture:))*