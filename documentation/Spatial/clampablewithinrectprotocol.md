# ClampableWithinRectProtocol

**Framework**: Spatial  
**Kind**: protocol

A set of methods that defines the interface for Spatial entities that can be clamped to a volume.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
protocol ClampableWithinRectProtocol<Scalar> : SpatialTypeProtocol
```

## Topics

### Instance Methods
- [func clamp(to: Self.Rect)](clampablewithinrectprotocol/clamp(to:).md)
  Clamps the mutable entity to the specified rectangle.
- [func clamped(to: Self.Rect) -> Self](clampablewithinrectprotocol/clamped(to:).md)
  Returns the entity with coordinates clamped to the specified rectangle.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [SpatialTypeProtocol](spatialtypeprotocol.md)
### Conforming Types
- [Point3D](point3d.md)
- [Point3DFloat](point3dfloat.md)

## See Also

- [protocol Primitive3D](primitive3d.md)
  A set of methods common to Spatial primitives.
- [protocol Rotatable3D](rotatable3d.md)
  A set of methods that defines the interface to rotate Spatial entities.
- [protocol Scalable3D](scalable3d.md)
  A set of methods that defines the interface to scale Spatial entities.
- [protocol Shearable3D](shearable3d.md)
  A set of methods that defines the interface to shear Spatial entities.
- [protocol Translatable3D](translatable3d.md)
  A set of methods that defines the interface to translate Spatial entities.
- [protocol Volumetric](volumetric.md)
  A set of methods for working with Spatial primitives with volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/clampablewithinrectprotocol)*