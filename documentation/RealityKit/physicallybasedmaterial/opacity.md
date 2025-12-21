# PhysicallyBasedMaterial.Opacity

**Framework**: RealityKit  
**Kind**: struct

An object that defines the opacity of an entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct Opacity
```

## Topics

### Creating an opacity object
- [init(floatLiteral: Float)](physicallybasedmaterial/opacity/init(floatliteral:).md)
  Creates an opacity object using a single value.
- [init(scale: Float, texture: PhysicallyBasedMaterial.Texture?)](physicallybasedmaterial/opacity/init(scale:texture:).md)
  Creates an opacity object using a single value or a texture.
- [init(CustomMaterial.Opacity)](physicallybasedmaterial/opacity/init(_:).md)
  Creates an opacity object using a custom material’s opacity property.
### Accessing opacity values
- [var texture: PhysicallyBasedMaterial.Texture?](physicallybasedmaterial/opacity/texture.md)
  The amount of opacity specified using a UV-mapped image.
- [static var textureSemantic: TextureResource.Semantic](physicallybasedmaterial/opacity/texturesemantic.md)
  The intended use of the object’s texture property.
- [var scale: Float](physicallybasedmaterial/opacity/scale.md)
- [var opacityThreshold: Float?](physicallybasedmaterial/opacitythreshold.md)
  A threshold below which RealityKit ignores opacity.

## Relationships

### Conforms To
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)

## See Also

- [PhysicallyBasedMaterial.Blending.opaque](physicallybasedmaterial/blending-swift.enum/opaque.md)
  An opaque surface.
- [case transparent(opacity: PhysicallyBasedMaterial.Opacity)](physicallybasedmaterial/blending-swift.enum/transparent(opacity:).md)
  A surface that’s transparent.
- [var opacityThreshold: Float?](physicallybasedmaterial/opacitythreshold.md)
  A threshold below which RealityKit ignores opacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/opacity)*