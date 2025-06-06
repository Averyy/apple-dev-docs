# init(floatLiteral:)

**Framework**: RealityKit  
**Kind**: init

Creates an object from a single value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
init(floatLiteral value: Float)
```

#### Discussion

RealityKit automatically draws  for physically based materials using the values of various properties, primarily [`roughness`](physicallybasedmaterial/roughness-swift.property.md) and [`metallic`](physicallybasedmaterial/metallic-swift.property.md). Specular highlights are bright spots of reflected light that appear on shiny objects.

![An illustration showing a sphere and a cube with rounded corners.](https://docs-assets.developer.apple.com/published/3e6c8711de5c00df45e2911543d778f2/CustomMaterial-Specular-swift-struct-init%28floatLiteral%3A%29-1%402x.png)

While many real-world objects can be accurately and realistically simulated with just the core physically based rendering (PBR) properties, you can create additional realistic effects by augmenting the specular highlights.

This initializer creates a [`PhysicallyBasedMaterial.Specular`](physicallybasedmaterial/specular-swift.struct.md) object from a single value that applies to the entire material. The specular [`scale`](custommaterial/specular-swift.struct/scale.md) value is available to the material’s surface shader, but RealityKit doesn’t create additional specular highlights unless the surface shader function calls `params.surface().set_specular()`.

The following Metal code demonstrates using the specular `scale` value in a surface shader function:

```other
    // Retrieve the opacity scale from the CustomMaterial and assign it.
    float specularScale = params.material_constants().specular_scale();
    params.surface().set_specular(specular);
```

## Parameters

- `value`: A value from   to   to use as the specular value   for the material.

## See Also

- [init(scale: Float, texture: CustomMaterial.Texture?)](custommaterial/specular-swift.struct/init(scale:texture:).md)
  Creates an object from a single value, a UV-mapped texture, or both.
- [init(PhysicallyBasedMaterial.Specular)](custommaterial/specular-swift.struct/init(_:).md)
  Creates an object from a physically based material’s specular property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/specular-swift.struct/init(floatliteral:))*