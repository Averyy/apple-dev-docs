# Primitive3DProtocol

**Framework**: Spatial  
**Kind**: protocol

A set of methods common to Spatial primitives.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
protocol Primitive3DProtocol<Scalar> : Rotatable3DProtocol
```

## Topics

### Instance Properties
- [var isFinite: Bool](primitive3dprotocol/isfinite.md)
  Returns whether the primitive is finite.
- [var isNaN: Bool](primitive3dprotocol/isnan.md)
  Returns whether the primitive contains any `NaN` values.
- [var isZero: Bool](primitive3dprotocol/iszero.md)
  Returns whether the primitive is zero.
### Instance Methods
- [func apply(Self.Pose)](primitive3dprotocol/apply(_:)-1qcu6.md)
  Applies a pose.
- [func apply(Self.ProjectiveTransform)](primitive3dprotocol/apply(_:)-3bne6.md)
  Applies a projective transform.
- [func apply(Self.AffineTransform)](primitive3dprotocol/apply(_:)-6b1fd.md)
  Applies an affine transform.
- [func applying(Self.AffineTransform) -> Self](primitive3dprotocol/applying(_:)-1tt2b.md)
  Returns the primitive that results from applying an affine transform to the primitive.
- [func applying(Self.Pose) -> Self](primitive3dprotocol/applying(_:)-4ylq8.md)
  Returns the primitive that results from applying a pose to the primitive.
- [func applying(Self.ProjectiveTransform) -> Self](primitive3dprotocol/applying(_:)-690k5.md)
  Returns the primitive that results from applying a projective transform to the primitive.
- [func unapply(Self.ProjectiveTransform)](primitive3dprotocol/unapply(_:)-22esh.md)
  Unapplies a projective transform.
- [func unapply(Self.AffineTransform)](primitive3dprotocol/unapply(_:)-34afa.md)
  Unapplies an affine transform.
- [func unapply(Self.Pose)](primitive3dprotocol/unapply(_:)-5dfj2.md)
  Unapplies a pose.
- [func unapplying(Self.ProjectiveTransform) -> Self](primitive3dprotocol/unapplying(_:)-1px2q.md)
  Returns the primitive that results from unapplying a projective transform to the primitive.
- [func unapplying(Self.AffineTransform) -> Self](primitive3dprotocol/unapplying(_:)-53rsn.md)
  Returns the primitive that results from unapplying an affine transform to the primitive.
- [func unapplying(Self.Pose) -> Self](primitive3dprotocol/unapplying(_:)-5fmf2.md)
  Returns the primitive that results from unapplying a pose to the primitive.
### Type Properties
- [static var infinity: Self](primitive3dprotocol/infinity.md)
  A primitive with infinite values.
- [static var zero: Self](primitive3dprotocol/zero.md)
  A primitive with zero values.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Rotatable3DProtocol](rotatable3dprotocol.md)
- [SpatialTypeProtocol](spatialtypeprotocol.md)
### Conforming Types
- [Point3D](point3d.md)
- [Point3DFloat](point3dfloat.md)
- [Ray3D](ray3d.md)
- [Ray3DFloat](ray3dfloat.md)
- [Rect3D](rect3d.md)
- [Rect3DFloat](rect3dfloat.md)
- [Size3D](size3d.md)
- [Size3DFloat](size3dfloat.md)
- [Vector3D](vector3d.md)
- [Vector3DFloat](vector3dfloat.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/primitive3dprotocol)*