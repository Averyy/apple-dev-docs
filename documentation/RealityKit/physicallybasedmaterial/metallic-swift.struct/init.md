# init(_:)

**Framework**: RealityKit  
**Kind**: init

Creates a metallic object from a custom material’s metallic property.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
init(_ value: CustomMaterial.Metallic)
```

#### Discussion

In PBR rendering, the `metallic` property represents the reflectiveness of an entity. This initializer creates a new object from the [`metallic`](custommaterial/metallic-swift.property.md) property of a [`CustomMaterial`](custommaterial.md).

## Parameters

- `value`: The custom material’s metallic property.

## See Also

- [init(floatLiteral: Float)](physicallybasedmaterial/metallic-swift.struct/init(floatliteral:).md)
  Creates an object from single value.
- [init(scale: Float, texture: PhysicallyBasedMaterial.Texture?)](physicallybasedmaterial/metallic-swift.struct/init(scale:texture:).md)
  Creates an object from a color or texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/metallic-swift.struct/init(_:))*