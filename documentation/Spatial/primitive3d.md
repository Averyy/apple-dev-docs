# Primitive3D

**Framework**: Spatial  
**Kind**: protocol  
**Role**: Protocol

A set of methods common to Spatial primitives.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
protocol Primitive3D : Decodable, Encodable, Equatable
```

## Topics

### Instance properties
- [var isFinite: Bool](./primitive3d/isfinite.md)
  Returns a Boolean value that indicates whether the primitive is infinite.
- [var isNaN: Bool](./primitive3d/isnan.md)
  Returns a Boolean value that indicates whether the primitive contains any NaN values.
- [var isZero: Bool](./primitive3d/iszero.md)
  Returns a Boolean value that indicates whether the primitive is zero.
### Type properties
- [static var infinity: Self](./primitive3d/infinity.md)
  A primitive with infinite values.
- [static var zero: Self](./primitive3d/zero.md)
  A primitive with zero values.
### Transforming primitives
- [func apply(AffineTransform3D)](./primitive3d/apply%28_%29-1nv9y.md)
  Applies an affine transform.
- [func apply(ProjectiveTransform3D)](./primitive3d/apply%28_%29-64cgp.md)
  Applies a projective transform.
- [func applying(AffineTransform3D) -> Self](./primitive3d/applying%28_%29-6264n.md)
  Returns the entity that results from applying an affine transform.
- [func applying(ProjectiveTransform3D) -> Self](./primitive3d/applying%28_%29-6icvg.md)
  Returns the entity that results from applying a projective transform.
- [func apply(Pose3D)](./primitive3d/apply%28_%29-4ic73.md)
  Applies a pose.
- [func applying(Pose3D) -> Self](./primitive3d/applying%28_%29-5yia.md)
  Returns the entity that results from applying a pose.
- [func unapply(AffineTransform3D)](./primitive3d/unapply%28_%29-4z6og.md)
  Unapplies an affine transform.
- [func unapply(ProjectiveTransform3D)](./primitive3d/unapply%28_%29-5haxp.md)
  Unapplies a projective transform.
- [func unapplying(AffineTransform3D) -> Self](./primitive3d/unapplying%28_%29-8ihh5.md)
  Returns the entity that results from unapplying an affine transform.
- [func unapplying(ProjectiveTransform3D) -> Self](./primitive3d/unapplying%28_%29-5ppqi.md)
  Returns the entity that results from unapplying a projective transform.
- [func unapply(Pose3D)](./primitive3d/unapply%28_%29-2992s.md)
  Unapplies a pose.
- [func unapplying(Pose3D) -> Self](./primitive3d/unapplying%28_%29-37fbg.md)
  Returns the entity that results from unapplying a pose.

## Relationships

### Inherits From
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
### Conforming Types
- [Point3D](./point3d.md)
- [Ray3D](./ray3d.md)
- [Rect3D](./rect3d.md)
- [Size3D](./size3d.md)
- [Vector3D](./vector3d.md)

## See Also

### Protocols
- [protocol Rotatable3D](./rotatable3d.md)
  A set of methods that defines the interface to rotate Spatial entities.
- [protocol Scalable3D](./scalable3d.md)
  A set of methods that defines the interface to scale Spatial entities.
- [protocol Shearable3D](./shearable3d.md)
  A set of methods that defines the interface to shear Spatial entities.
- [protocol Translatable3D](./translatable3d.md)
  A set of methods that defines the interface to translate Spatial entities.
- [protocol Volumetric](./volumetric.md)
  A set of methods for working with Spatial primitives with volume.
- [protocol ClampableWithinRectProtocol](./clampablewithinrectprotocol.md)
  A set of methods that defines the interface for Spatial entities that can be clamped to a volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/primitive3d)*