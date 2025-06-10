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
- visionOS ?+

## Declaration

```swift
init(scale: Float = 1.0, texture: PhysicallyBasedMaterial.Texture? = nil)
```

#### Discussion

In PBR rendering, the `metallic` property represents the reflectiveness of an entity. This initializer creates a new object from a single value to describe the reflectiveness of the entire material. This initializer creates a new object from a single value or a grayscale image texture, or from both.

If you specify `texture`, RealityKit calculates the `metallic` for the entity by UV-mapping `texture` onto the entity and multiplying the value of each mapped pixel by `scale`. If you don’t specify `texture`, then RealityKit uses `scale` as the entire entity’s reflectiveness. If you provide a color image for `texture` rather than a grayscale image, RealityKit only uses the intensity of the image’s red channel.

![An illustration showing two spheres rendered in RealityKit. The](https://docs-assets.developer.apple.com/published/ae4a36e0823c65c0745717fb7067de18/PhysicallyBasedMaterial-Metallic-swift-struct-init%28scale%3Atexture%3A%29-1%402x.png)

## Parameters

- `scale`: The reflectiveness value.
- `texture`: An optional image texture.

## See Also

- [init(floatLiteral: Float)](physicallybasedmaterial/metallic-swift.struct/init(floatliteral:).md)
  Creates an object from single value.
- [init(CustomMaterial.Metallic)](physicallybasedmaterial/metallic-swift.struct/init(_:).md)
  Creates a metallic object from a custom material’s metallic property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/metallic-swift.struct/init(scale:texture:))*