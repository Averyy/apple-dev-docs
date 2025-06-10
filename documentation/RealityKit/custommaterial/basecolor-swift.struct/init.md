# init(_:)

**Framework**: RealityKit  
**Kind**: init

Creates a custom base color object from an existing physically based material’s base color object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
init(_ value: PhysicallyBasedMaterial.BaseColor)
```

#### Discussion

Use this initializer to create a [`CustomMaterial.BaseColor`](custommaterial/basecolor-swift.struct.md) that contains the same tint and texture values as an existing [`PhysicallyBasedMaterial.BaseColor`](physicallybasedmaterial/basecolor-swift.struct.md) object.

Both `tint` and `texture` from the [`PhysicallyBasedMaterial.BaseColor`](physicallybasedmaterial/basecolor-swift.struct.md) object are available in your surface shader, but RealityKit doesn’t automatically use those values to render the entity. Your surface shader needs to calculate the final base color value for each pixel and assign it by calling `params.surface().set_base_color()`.

For more information on creating custom materials and writing shader functions, see [`Modifying RealityKit rendering using custom materials`](modifying-realitykit-rendering-using-custom-materials.md).

## Parameters

- `value`: The base color object from a physically based material.

## See Also

- [init(tint: UIColor, texture: CustomMaterial.Texture?)](custommaterial/basecolor-swift.struct/init(tint:texture:)-5c2fr.md)
  Creates a base color object from a color or texture on macOS.
- [init(tint: NSColor, texture: CustomMaterial.Texture?)](custommaterial/basecolor-swift.struct/init(tint:texture:)-71h0i.md)
  Creates a base color object from a color or texture on macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/basecolor-swift.struct/init(_:))*