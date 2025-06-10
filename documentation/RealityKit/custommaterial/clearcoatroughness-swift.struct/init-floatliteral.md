# init(floatLiteral:)

**Framework**: RealityKit  
**Kind**: init

Creates a clearcoat object using a single value.

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

A clearcoat is a separate layer of transparent specular highlights used to simulate a clear coating, like on a car or the surface of lacquered objects. Use this initializer to create an object to specify the amount of clearcoat for a material using a single value for the entire material, a UV-mapped image to specify different values for different parts of the entity, or both.

The values from this property are available in the custom material’s surface shader function regardless of the value of [`lightingModel`](custommaterial/lightingmodel-swift.property.md) , but clearcoat isn’t drawn unless the custom material’s [`lightingModel`](custommaterial/lightingmodel-swift.property.md) is [`CustomMaterial.LightingModel.clearcoat`](custommaterial/lightingmodel-swift.enum/clearcoat.md) and the surface shader calls `params.surface().set_clearcoat()`.

The following Metal code demonstrates how to retrieve the scale and texture values from this property and use them to enable clearcoat rendering.

```other
    // Retrieve the clearcoat scale and roughness from the CustomMaterial.
    float clearcoatScale = params.material_constants().clearcoat_scale();
    float clearcoatRoughnessScale = params.material_constants().clearcoat_roughness_scale();

    // Assign the clearcoat scale to enable clearcoat rendering (if
    // lightingModel is .clearcoat).
    params.surface().set_clearcoat(clearcoatScale);

    // Assign the clearcoat roughness from the scale property set
    //  on the custom material.
    params.surface().set_clearcoat_roughness(clearcoatRoughnessScale);
```

## Parameters

- `value`: The clearcoat value to use for the entity.

## See Also

- [init(scale: Float, texture: CustomMaterial.Texture?)](custommaterial/clearcoatroughness-swift.struct/init(scale:texture:).md)
  Creates a clearcoat object using a single value or a texture.
- [init(PhysicallyBasedMaterial.ClearcoatRoughness)](custommaterial/clearcoatroughness-swift.struct/init(_:).md)
  Creates a custom clearcoat object from a physically based material’s clearcoat property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/clearcoatroughness-swift.struct/init(floatliteral:))*