# init(floatLiteral:)

**Framework**: RealityKit  
**Kind**: init

Creates a clearcoat object using a single value.

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

#### Discussion

A clearcoat is a separate layer of transparent specular highlights used to simulate a clear coating, like on a car or the surface of lacquered objects. Use this initializer to create an object to specify the amount of clearcoat for a material using a single value that applies to the entire material.

The clearcoat value is available in the material’s surface shader function, but RealityKit doesn’t render a clearcoat unless the material’s [`lightingModel`](custommaterial/lightingmodel-swift.property.md) is [`CustomMaterial.LightingModel.clearcoat`](custommaterial/lightingmodel-swift.enum/clearcoat.md) and its surface shader function calls `params.surface().set_clearcoat()`.

The following Metal code demonstrates how to retrieve the clearcoat [`scale`](custommaterial/clearcoat-swift.struct/scale.md) in a surface shader function and use it to set the final clearcoat value for rendering:

```other
    // Retrieve the base color tint from the CustomMaterial.
    float clearcoatScale = params.material_constants().clearcoat_scale();

    // Assign the scale value as the clearcoat value for this pixel.
    params.surface().set_clearcoat(clearcoat);
```

## Parameters

- `value`: The clearcoat value to use for the entity.

## See Also

- [init(scale: Float, texture: CustomMaterial.Texture?)](custommaterial/clearcoat-swift.struct/init(scale:texture:).md)
  Creates a clearcoat object using a single value or a texture.
- [init(PhysicallyBasedMaterial.Clearcoat)](custommaterial/clearcoat-swift.struct/init(_:).md)
  Creates a custom clearcoat object from a physically based material’s clearcoat property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/clearcoat-swift.struct/init(floatliteral:))*