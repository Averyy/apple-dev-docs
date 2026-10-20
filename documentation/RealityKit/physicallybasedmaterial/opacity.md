# PhysicallyBasedMaterial.Opacity

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that defines the opacity of an entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct Opacity
```

## Topics

### Creating an opacity object
- [init(floatLiteral: Float)](./opacity/init%28floatliteral%29.md)
  Creates an opacity object using a single value.
- [init(scale: Float, texture: PhysicallyBasedMaterial.Texture?)](./opacity/init%28scale,texture%29.md)
  Creates an opacity object using a single value or a texture.
- [init(CustomMaterial.Opacity)](./opacity/init%28_%29.md)
  Creates an opacity object using a custom material’s opacity property.
### Accessing opacity values
- [var texture: PhysicallyBasedMaterial.Texture?](./opacity/texture.md)
  The amount of opacity specified using a UV-mapped image.
- [static var textureSemantic: TextureResource.Semantic](./opacity/texturesemantic.md)
  The intended use of the object’s texture property.
- [var scale: Float](./opacity/scale.md)
- [var opacityThreshold: Float?](./opacitythreshold.md)
  A threshold below which RealityKit ignores opacity.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByFloatLiteral](../../Swift/expressiblebyfloatliteral.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Specifying opacity
- [PhysicallyBasedMaterial.Blending.opaque](./blending-swift.enum/opaque.md)
  An opaque surface.
- [case transparent(opacity: PhysicallyBasedMaterial.Opacity)](./blending-swift.enum/transparent%28opacity%29.md)
  A surface that’s transparent.
- [var opacityThreshold: Float?](./opacitythreshold.md)
  A threshold below which RealityKit ignores opacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/opacity)*