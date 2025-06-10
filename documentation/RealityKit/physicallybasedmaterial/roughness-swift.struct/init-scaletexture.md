# init(scale:texture:)

**Framework**: RealityKit  
**Kind**: init

Creates a roughness object from a color or texture.

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

The `roughness` property represents how much the surface of the entity scatters light it reflects. A material with a high roughness has a matte appearance, while one with a low roughness has a shiny appearance.

![An illustration showing three spheres with different amounts of](https://docs-assets.developer.apple.com/published/6dccdd9884a6e12444a9f61c265d8644/PhysicallyBasedMaterial-Roughness-swift-struct-init%28scale%3Atexture%3A%29-1%402x.png)

Use this initializer to create a new object from a single roughness value, from an image texture, or from both.

If you specify `texture`, RealityKit calculates the `roughness` for the entity by UV-mapping `texture` onto the entity and multiplying the value of each mapped pixel by `scale`. If you don’t specify `texture`, then RealityKit uses `scale` as the entire entity’s roughness. If you provide a color image for `texture` rather than a grayscale image, RealityKit only uses the intensity of the image’s red channel.

## Parameters

- `scale`: The roughness value.
- `texture`: An optional image texture.

## See Also

- [init(floatLiteral: Float)](physicallybasedmaterial/roughness-swift.struct/init(floatliteral:).md)
  Creates an object from a single value.
- [init(CustomMaterial.Roughness)](physicallybasedmaterial/roughness-swift.struct/init(_:).md)
  Creates a roughness object from a custom material’s roughness property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/roughness-swift.struct/init(scale:texture:))*