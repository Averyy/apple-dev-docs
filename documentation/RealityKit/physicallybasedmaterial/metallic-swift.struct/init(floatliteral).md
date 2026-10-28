# init(floatLiteral:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates an object from single value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
init(floatLiteral value: Float)
```

## Discussion

In PBR rendering, the `metallic` property represents the reflectiveness of an entity. This initializer creates a new object from a single value to describe the reflectiveness of the entire material. A value of 0.0 creates a *dielectric* (or non-reflective) material. Values greater than 0.0 result in an increasingly *metallic* (or reflective) materials.

![An illustration showing two spheres rendered in RealityKit. The](https://developer.apple.com/tutorials/images/com.apple.RealityKit/PhysicallyBasedMaterial-Metallic-swift-struct-init(floatLiteral:)-1@2x.png)

## Parameters

- `value`: The reflectiveness value for the material.

## See Also

### Creating a metallic object
- [init(scale: Float, texture: PhysicallyBasedMaterial.Texture?)](./init%28scale,texture%29.md)
  Creates an object from a color or texture.
- [init(CustomMaterial.Metallic)](./init%28_%29.md)
  Creates a metallic object from a custom material’s metallic property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/metallic-swift.struct/init(floatliteral:))*