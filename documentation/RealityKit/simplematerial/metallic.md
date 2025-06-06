# metallic

**Framework**: RealityKit  
**Kind**: property

A value that you set to control whether the material has a metallic look.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
var metallic: MaterialScalarParameter { get set }
```

#### Discussion

This property defines whether a material is dielectric (`0.0`) or a metallic (`1.0`). Although this property can be set to any value between `0` and `1`, to create a realistic material, set it to either `0` or `1`.).

## See Also

- [var color: SimpleMaterial.BaseColor](simplematerial/color.md)
  The material’s color.
- [var baseColor: MaterialColorParameter](simplematerial/basecolor-swift.property.md)
  The base color of the material.
- [SimpleMaterial.BaseColor](simplematerial/basecolor-swift.typealias.md)
  The type used to represent base color.
- [var tintColor: UIColor](simplematerial/tintcolor-18qur.md)
  A tint color applied to the base color in macOS.
- [var tintColor: NSColor](simplematerial/tintcolor-6aik0.md)
  A tint color applied to the base color in macOS.
- [SimpleMaterial.Texture](simplematerial/texture.md)
  The type used to represent textures.
- [var roughness: MaterialScalarParameter](simplematerial/roughness.md)
  The roughness of the material.
- [SimpleMaterial.Parameters](simplematerial/parameters.md)
  The parameter type that custom materials uses for properties the framework passes to shader functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/simplematerial/metallic)*