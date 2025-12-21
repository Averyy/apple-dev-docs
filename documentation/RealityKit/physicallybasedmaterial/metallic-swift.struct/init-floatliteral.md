# init(floatLiteral:)

**Framework**: RealityKit  
**Kind**: init

Creates an object from single value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
init(floatLiteral value: Float)
```

#### Discussion

In PBR rendering, the `metallic` property represents the reflectiveness of an entity. This initializer creates a new object from a single value to describe the reflectiveness of the entire material. A value of 0.0 creates a  (or non-reflective) material. Values greater than 0.0 result in an increasingly  (or reflective) materials.

![An illustration showing two spheres rendered in RealityKit. The](https://docs-assets.developer.apple.com/published/ae4a36e0823c65c0745717fb7067de18/PhysicallyBasedMaterial-Metallic-swift-struct-init%28floatLiteral%3A%29-1%402x.png)

## Parameters

- `value`: The reflectiveness value for the material.

## See Also

- [init(scale: Float, texture: PhysicallyBasedMaterial.Texture?)](physicallybasedmaterial/metallic-swift.struct/init(scale:texture:).md)
  Creates an object from a color or texture.
- [init(CustomMaterial.Metallic)](physicallybasedmaterial/metallic-swift.struct/init(_:).md)
  Creates a metallic object from a custom material’s metallic property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/metallic-swift.struct/init(floatliteral:))*