# init(scale:texture:)

**Framework**: RealityKit  
**Kind**: init

Creates an object from a single value or a texture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
init(scale: Float = 1.0, texture: PhysicallyBasedMaterial.Texture? = nil)
```

#### Discussion

RealityKit automatically draws  for physically based materials using the values of various properties, primarily [`roughness`](physicallybasedmaterial/roughness-swift.property.md) and [`metallic`](physicallybasedmaterial/metallic-swift.property.md). Specular highlights are bright spots of reflected light that appear on shiny objects.

![An illustration showing a sphere and a cube with rounded corners.](https://docs-assets.developer.apple.com/published/0b83dd2d5721a30ef708e7bf6420620b/PhysicallyBasedMaterial-Specular-swift-struct-init%28scale%3Atexture%3A%29-1%402x.png)

While many real-world objects can be accurately and realistically simulated with just the core PBR properties, you can create additional realistic effects by augmenting the specular highlights.

This initializer creates a [`PhysicallyBasedMaterial.Specular`](physicallybasedmaterial/specular-swift.struct.md) object from a single value, an image texture, or both.

If you specify `texture`, RealityKit calculates the `specular` for the entity by UV-mapping `texture` onto the entity and multiplying the value of each mapped pixel by `scale`. If you don’t specify `texture`, RealityKit uses `scale` as the entire entity’s specular. If you provide a color image for `texture` rather than a grayscale image, RealityKit only uses the intensity of the image’s red channel.

## Parameters

- `scale`: A value from 0.0 to 1.0 to use as the specular value for   the material.
- `texture`: An optional UV-mapped image texture.

## See Also

- [init(floatLiteral: Float)](physicallybasedmaterial/specular-swift.struct/init(floatliteral:).md)
  Creates an object from single value.
- [init(CustomMaterial.Specular)](physicallybasedmaterial/specular-swift.struct/init(_:).md)
  Creates an object from a custom material’s specular property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/specular-swift.struct/init(scale:texture:))*