# init(floatLiteral:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates an object from a single value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
init(floatLiteral value: Float)
```

## Discussion

In physically based rendering, the `metallic` property represents the reflectiveness of an entity. This initializer creates a new object that passes a single metallic value to your custom shader functions but doesn’t pass a texture.

The following Swift code shows how to specify reflectiveness using a single value for the entire entity:

```swift
material.roughness = PhysicallyBasedMaterial.Roughness(floatLiteral: 0.0)
```

To render an entity with reflectiveness, set [`lightingModel`](../lightingmodel-swift.property.md) to [`CustomMaterial.LightingModel.lit`](../lightingmodel-swift.enum/lit.md) or [`CustomMaterial.LightingModel.clearcoat`](../lightingmodel-swift.enum/clearcoat.md), and call `params.surface().set_metallic()` from its surface shader.

The following Metal code shows how to retrieve the value set in this initializer in your surface shader and use it:

```other
    // Retrieve the metallic scale from the CustomMaterial.
    float metallic = params.material_constants().metallic_scale();

    // Set the roughness value using the metallic scale value.
    params.surface().set_metallic(metallic);
```

For more information on creating custom materials and writing shader functions, see [Modifying RealityKit rendering using custom materials](../../modifying-realitykit-rendering-using-custom-materials.md).

## Parameters

- `value`: The reflectiveness value for the material.

## See Also

### Creating a metallic object
- [init(scale: Float, texture: CustomMaterial.Texture?)](./init%28scale,texture%29.md)
  Creates an object from a color or texture.
- [init(PhysicallyBasedMaterial.Metallic)](./init%28_%29.md)
  Creates a metallic object from a physically based material’s metallic property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/metallic-swift.struct/init(floatliteral:))*