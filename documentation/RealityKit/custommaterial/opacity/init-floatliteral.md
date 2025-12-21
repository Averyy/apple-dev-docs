# init(floatLiteral:)

**Framework**: RealityKit  
**Kind**: init

Creates an opacity object from a single value.

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

This initializer creates an object that defines the opacity of an entity using a single value for the entire entity. This value is available to the material’s surface shader function, but RealityKit draws the entity fully opaque unless the surface shader function calls `params.surface().set_opacity()`.

The following Metal code demonstrates how to set the entity’s opacity in the material’s surface shader function based on `value:`

```swift
    // Retrieve the opacity scale from the CustomMaterial.
    float opacityScale = params.material_constants().opacity_scale();

    // Use the opacity scale to set the current pixel's opacity.
    params.surface().set_opacity(opacityScale);
```

## Parameters

- `value`: The opacity value.

## See Also

- [init(scale: Float, texture: CustomMaterial.Texture?)](custommaterial/opacity/init(scale:texture:).md)
  Creates an object that defines the opacity of an entity using a single value, a UV-mapped image texture, or both.
- [init(PhysicallyBasedMaterial.Opacity)](custommaterial/opacity/init(_:).md)
  Creates an object from the opacity property of an existing physically based material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/opacity/init(floatliteral:))*