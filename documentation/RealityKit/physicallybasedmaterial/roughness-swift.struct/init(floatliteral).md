# init(floatLiteral:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates an object from a single value.

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

The `roughness` property represents how much the surface of the entity scatters light it reflects. A material with a high roughness has a matte appearance, while one with a low roughness has a shiny appearance.

![An illustration showing three spheres with different amounts of](https://developer.apple.com/tutorials/images/com.apple.RealityKit/PhysicallyBasedMaterial-Roughness-swift-struct-init(floatLiteral:)-1@2x.png)

Use this initializer to create an object to specify the amount of roughness using a single value that applies to the entire material.

## Parameters

- `value`: The roughness value.

## See Also

### Creating a roughness object
- [init(scale: Float, texture: PhysicallyBasedMaterial.Texture?)](./init%28scale,texture%29.md)
  Creates a roughness object from a color or texture.
- [init(CustomMaterial.Roughness)](./init%28_%29.md)
  Creates a roughness object from a custom material’s roughness property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/roughness-swift.struct/init(floatliteral:))*