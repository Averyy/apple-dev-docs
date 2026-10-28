# init(_:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates an object from a custom material’s specular property.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
init(_ value: CustomMaterial.Specular)
```

## Discussion

RealityKit automatically draws *specular highlights* for physically based materials using the values of various properties, primarily [`roughness`](../roughness-swift.property.md) and [`metallic`](../metallic-swift.property.md). Specular highlights are bright spots of reflected light that appear on shiny objects.

![An illustration showing a sphere and a cube with rounded corners.](https://developer.apple.com/tutorials/images/com.apple.RealityKit/PhysicallyBasedMaterial-Specular-swift-struct-init(_:)-1@2x.png)

While many real-world objects can be accurately and realistically simulated with just the core PBR properties, you can create additional realistic effects by augmenting the specular highlights.

This initializer creates a [`PhysicallyBasedMaterial.Specular`](../specular-swift.struct.md) object from the specular property of a [`CustomMaterial`](../../custommaterial.md).

## Parameters

- `value`: The custom material’s specular property.

## See Also

### Creating a specular object
- [init(floatLiteral: Float)](./init%28floatliteral%29.md)
  Creates an object from single value.
- [init(scale: Float, texture: PhysicallyBasedMaterial.Texture?)](./init%28scale,texture%29.md)
  Creates an object from a single value or a texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/specular-swift.struct/init(_:))*