# init(floatLiteral:)

**Framework**: RealityKit  
**Kind**: init

Creates an object to specify the amount of roughness, using a single value that applies to the entire material.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
init(floatLiteral value: Float)
```

#### Discussion

The `roughness` property represents how much the surface of the entity scatters light that it reflects. A material with a high roughness has a matte appearance, and one with a low roughness has a shiny appearance.

![An illustration showing three spheres with different amounts of](https://docs-assets.developer.apple.com/published/6bca90ebd0a4a4a329474aaf179c551a/CustomMaterial-Roughness-swift-struct-init%28floatLiteral%3A%29-1%402x.png)

The following Swift code shows how to specify roughness using a single value for the entire entity:

```swift
material.roughness = PhysicallyBasedMaterial.Roughness(floatLiteral: 0.0)
```

With custom materials, the roughness value is available in your surface shader; however, RealityKit doesn’t use it automatically to render the entity. To render an entity with roughness, the material’s [`lightingModel`](custommaterial/lightingmodel-swift.property.md) needs to be [`CustomMaterial.LightingModel.lit`](custommaterial/lightingmodel-swift.enum/lit.md) or [`CustomMaterial.LightingModel.clearcoat`](custommaterial/lightingmodel-swift.enum/clearcoat.md), and call `params.surface().set_roughness()` from its surface shader function.

The following Metal code shows how to retrieve the roughness value set using this initializer in your surface shader:

```other
    // Retrieve the roughness scale from the CustomMaterial.
    float roughnessScale = params.material_constants().roughness_scale();

    // Set the roughness value using the roughness scale.
    params.surface().set_roughness(roughnessScale);
```

For more information on creating custom materials and writing shader functions, see [`Modifying RealityKit rendering using custom materials`](modifying-realitykit-rendering-using-custom-materials.md).

## Parameters

- `value`: The roughness value.

## See Also

- [init(scale: Float, texture: CustomMaterial.Texture?)](custommaterial/roughness-swift.struct/init(scale:texture:).md)
  Creates a roughness object from a color or texture.
- [init(PhysicallyBasedMaterial.Roughness)](custommaterial/roughness-swift.struct/init(_:).md)
  Creates a roughness object from a physically based material’s roughness property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/roughness-swift.struct/init(floatliteral:))*