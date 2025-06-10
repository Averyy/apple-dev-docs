# init(scale:texture:)

**Framework**: RealityKit  
**Kind**: init

Creates an object from a color or texture.

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

In physically based rendering, the `metallic` property represents the reflectiveness of an entity. This initializer creates a new object that passes a single scale value, a texture, or both to the material’s shader functions.

The following code demonstrates creating a roughness object using this initalizer:

```swift
if let metallicResource = try? TextureResource.load(named:
"metallic_roughness") {
    let metallic = MaterialParameters.Texture(metallicResource)
    customMaterial.roughness = .init(scale: 0.5, texture: metallic)
}
```

With custom materials, the `texture` and `scale` properties you set on this property are available in your surface shader function, but RealityKit doesn’t automatically use them to render your entity. To render an entity with reflectiveness, set [`lightingModel`](custommaterial/lightingmodel-swift.property.md) to [`CustomMaterial.LightingModel.lit`](custommaterial/lightingmodel-swift.enum/lit.md) or [`CustomMaterial.LightingModel.clearcoat`](custommaterial/lightingmodel-swift.enum/clearcoat.md), and call `params.surface().set_metallic()` from its surface shader.

To achieve the same metallic behavior as [`PhysicallyBasedMaterial`](physicallybasedmaterial.md), the surface shader function multiplies the metallic scale by the sampled value from the roughness texture, as the following Metal code demonstrates:

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

    // Multiply the scale and the sampled value from the texture, and assign
    // the result to the shader's metallic property.
    metallic *= metallicScale;
    params.surface().set_metallic(metallic);
```

For more information on creating custom materials and writing shader functions, see [`Modifying RealityKit rendering using custom materials`](modifying-realitykit-rendering-using-custom-materials.md).

## Parameters

- `scale`: The reflectiveness value.
- `texture`: An optional image texture.

## See Also

- [init(floatLiteral: Float)](custommaterial/metallic-swift.struct/init(floatliteral:).md)
  Creates an object from a single value.
- [init(PhysicallyBasedMaterial.Metallic)](custommaterial/metallic-swift.struct/init(_:).md)
  Creates a metallic object from a physically based material’s metallic property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/metallic-swift.struct/init(scale:texture:))*