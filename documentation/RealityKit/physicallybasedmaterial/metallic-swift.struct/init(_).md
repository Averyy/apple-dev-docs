# init(_:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a metallic object from a custom material’s metallic property.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
init(_ value: CustomMaterial.Metallic)
```

#### Discussion

In PBR rendering, the `metallic` property represents the reflectiveness of an entity. This initializer creates a new object from the [`metallic`](../../custommaterial/metallic-swift.property.md) property of a [`CustomMaterial`](../../custommaterial.md).

## Parameters

- `value`: The custom material’s metallic property.

## See Also

### Creating a metallic object
- [init(floatLiteral: Float)](./init%28floatliteral%29.md)
  Creates an object from single value.
- [init(scale: Float, texture: PhysicallyBasedMaterial.Texture?)](./init%28scale,texture%29.md)
  Creates an object from a color or texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/metallic-swift.struct/init(_:))*