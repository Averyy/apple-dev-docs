# init(tint:texture:)

**Framework**: RealityKit  
**Kind**: init

Creates a base color object from a color or texture on macOS.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
init(tint: NSColor = .white, texture: CustomMaterial.Texture? = nil)
```

#### Discussion

This initializer creates a new object from a color or image texture, or from both. If you don’t provide a `tint` color, `tint` defaults to white.

Both tint and texture are available to use in your surface shader function, but RealityKit doesn’t automatically use them to render the entity. Your surface shader calculates the final base color value for each pixel and assigns it by calling `params.surface().set_base_color()`.

For more information on creating custom materials and writing shader functions, see [`Modifying RealityKit rendering using custom materials`](modifying-realitykit-rendering-using-custom-materials.md).

## Parameters

- `tint`: The tint color. Defaults to white.
- `texture`: An optional image texture.

## See Also

- [init(tint: UIColor, texture: CustomMaterial.Texture?)](custommaterial/basecolor-swift.struct/init(tint:texture:)-5c2fr.md)
  Creates a base color object from a color or texture on macOS.
- [init(PhysicallyBasedMaterial.BaseColor)](custommaterial/basecolor-swift.struct/init(_:).md)
  Creates a custom base color object from an existing physically based material’s base color object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/basecolor-swift.struct/init(tint:texture:)-71h0i)*