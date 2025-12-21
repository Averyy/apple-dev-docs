# init(floatLiteral:)

**Framework**: RealityKit  
**Kind**: init

Creates a clearcoat object using a single value.

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

A clearcoat is a separate layer of transparent specular highlights used to simulate a clear transparent coating, like the paint on a car, or the surface of lacquered objects. Use this initializer to create an object to specify the amount of clearcoat for a material using a single value that applies to the entire material.

## Parameters

- `value`: The clearcoat value to use for the entity.

## See Also

- [init(scale: Float, texture: PhysicallyBasedMaterial.Texture?)](physicallybasedmaterial/clearcoat-swift.struct/init(scale:texture:).md)
  Creates a clearcoat object using a single value or a texture.
- [init(CustomMaterial.Clearcoat)](physicallybasedmaterial/clearcoat-swift.struct/init(_:).md)
  Creates a clearcoat object from a custom material’s clearcoat property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/clearcoat-swift.struct/init(floatliteral:))*