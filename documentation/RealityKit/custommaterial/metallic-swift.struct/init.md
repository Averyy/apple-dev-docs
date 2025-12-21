# init(_:)

**Framework**: RealityKit  
**Kind**: init

Creates a metallic object from a physically based material’s metallic property.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
init(_ value: PhysicallyBasedMaterial.Metallic)
```

#### Discussion

This initializer creates a new object by copying the values from an existing [`PhysicallyBasedMaterial.Metallic`](physicallybasedmaterial/metallic-swift.struct.md) object.

To render an entity with reflectiveness, set [`lightingModel`](custommaterial/lightingmodel-swift.property.md) to [`CustomMaterial.LightingModel.lit`](custommaterial/lightingmodel-swift.enum/lit.md) or [`CustomMaterial.LightingModel.clearcoat`](custommaterial/lightingmodel-swift.enum/clearcoat.md), and call `params.surface().set_metallic()` from its surface shader function.

To achieve the same metallic behavior as [`PhysicallyBasedMaterial`](physicallybasedmaterial.md), the surface shader function multiplies metallic scale by the sampled value from the texture, as the following Metal code demonstrates:

```other
    // Retrieve the metallic scale from the CustomMaterial.
    float metallicScale = params.material_constants().metallic_scale();

    // Retrieve the entity's UV texture coordinates.
    float2 uv = params.geometry().uv0();

    // Models loaded from USDZ or Reality Composer use UVs that are flipped
    // on the y-axis. This compensates for that.
    uv.y = 1.0 - uv.y;

    // Sample the texture based on the resulting UVs.
    auto tex = params.textures();
    half metallic = tex.metallic().sample(textureSampler, uv).r;

    // Multiply the scale and the sampled value from the texture,
    // and assign the result to the shader's metallic property.
    metallic *= metallicScale;
    params.surface().set_metallic(metallic);
```

For more information on creating custom materials and writing shader functions, see [`Modifying RealityKit rendering using custom materials`](modifying-realitykit-rendering-using-custom-materials.md).

## Parameters

- `value`: The physically based material’s metallic property.

## See Also

- [init(floatLiteral: Float)](custommaterial/metallic-swift.struct/init(floatliteral:).md)
  Creates an object from a single value.
- [init(scale: Float, texture: CustomMaterial.Texture?)](custommaterial/metallic-swift.struct/init(scale:texture:).md)
  Creates an object from a color or texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/metallic-swift.struct/init(_:))*