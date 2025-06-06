# init(scale:texture:)

**Framework**: RealityKit  
**Kind**: init

Creates an object from a single value, a UV-mapped texture, or both.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
init(scale: Float = 1.0, texture: CustomMaterial.Texture? = nil)
```

#### Discussion

RealityKit automatically draws  for physically based materials using the values of various properties, primarily [`roughness`](physicallybasedmaterial/roughness-swift.property.md) and [`metallic`](physicallybasedmaterial/metallic-swift.property.md). Specular highlights are bright spots of reflected light that appear on shiny objects.

![An illustration showing a sphere and a cube with rounded corners.](https://docs-assets.developer.apple.com/published/3e6c8711de5c00df45e2911543d778f2/CustomMaterial-Specular-swift-struct-init%28scale%3Atexture%3A%29-1%402x.png)

While many real-world objects can be accurately and realistically simulated with just the core physically based rendering (PBR) properties, you can create additional realistic effects by augmenting the specular highlights.

The specular [`scale`](custommaterial/specular-swift.struct/scale.md) and [`texture`](custommaterial/specular-swift.struct/texture.md) values are available to the material’s surface shader, but RealityKit doesn’t render additional specular highlights unless the surface shader function calls `params.surface().set_specular()`.

The following Metal code demonstrates using the specular `scale` and `texture` values in a surface shader function to calculate specular highlights, emulating the specular behavior of [`PhysicallyBasedMaterial`](physicallybasedmaterial.md):

```other
    // Retrieve the opacity scale from the CustomMaterial.
    float specularScale = params.material_constants().specular_scale();

    // Retrieve the entity's texture coordinates.
    float2 uv = params.geometry().uv0();

    // Entities loaded from a USDZ or .reality file use texture coordinates
    // with a flipped y-axis. This compensates for that.
    uv.y = 1.0 - uv.y;

    // Sample the specular texture.
    auto tex = params.textures();
    half specular = tex.specular().sample(textureSampler, uv).r;

    // Multiply the tint and the sampled value from the texture and assign
    // the result.
    specular *= specularScale;
    params.surface().set_specular(specular);
```

## Parameters

- `scale`: A value from   to   to use as the specular value   for the material.
- `texture`: An optional UV-mapped image texture.

## See Also

- [init(floatLiteral: Float)](custommaterial/specular-swift.struct/init(floatliteral:).md)
  Creates an object from a single value.
- [init(PhysicallyBasedMaterial.Specular)](custommaterial/specular-swift.struct/init(_:).md)
  Creates an object from a physically based material’s specular property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/specular-swift.struct/init(scale:texture:))*