# Rect3DFloat

**Framework**: Spatial  
**Kind**: struct

A single-precision structure that contains the location and dimensions of a 3D rectangle.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct Rect3DFloat
```

## Topics

### Operators
- [static func * (ProjectiveTransform3DFloat, Rect3DFloat) -> Rect3DFloat](rect3dfloat/*(_:_:)-1iaiz.md)
  Returns the rectangle that results from applying the transform to the rectangle.
- [static func * (Pose3DFloat, Rect3DFloat) -> Rect3DFloat](rect3dfloat/*(_:_:)-1xai0.md)
  Returns the rectangle that results from applying the pose to the rectangle.
- [static func * (AffineTransform3DFloat, Rect3DFloat) -> Rect3DFloat](rect3dfloat/*(_:_:)-2fdne.md)
  Returns the rectangle that results from applying the transform to the rectangle.
### Initializers
- [init()](rect3dfloat/init.md)
- [init(Rect3D)](rect3dfloat/init(_:).md)
  Returns a single-precision rectangle from a double-precision rectangle.
- [init(center: simd_double3, size: simd_double3)](rect3dfloat/init(center:size:)-1gsbj.md)
  Creates a rectangle from single-precision vectors that describe the center and size.
- [init(center: simd_float3, size: simd_float3)](rect3dfloat/init(center:size:)-2c8oz.md)
  Creates a rectangle from simd vectors that describe the center and size.
- [init(center: Vector3DFloat, size: Vector3DFloat)](rect3dfloat/init(center:size:)-92ay9.md)
  Creates a rectangle from Spatial vectors that describe the center and size.
- [init(center: Point3DFloat, size: Size3DFloat)](rect3dfloat/init(center:size:)-e8la.md)
  Creates a rectangle at the specified center with the specified size.
- [init(origin: simd_float3, size: simd_float3)](rect3dfloat/init(origin:size:)-27.md)
  Creates a rectangle from simd vectors that describe the origin and size.
- [init(origin: Point3DFloat, size: Size3DFloat)](rect3dfloat/init(origin:size:)-8tqau.md)
- [init(origin: Point3DFloat, size: Size3DFloat)](rect3dfloat/init(origin:size:)-9his9.md)
- [init(origin: simd_double3, size: simd_double3)](rect3dfloat/init(origin:size:)-uw6h.md)
  Creates a rectangle from double-precision vectors that describe the origin and size.
- [init(origin: Vector3DFloat, size: Vector3DFloat)](rect3dfloat/init(origin:size:)-ywzp.md)
  Creates a rectangle from Spatial vectors that describe the origin and size.
- [init(points: [Point3DFloat])](rect3dfloat/init(points:).md)
  Creates a rectangle that’s the bounding box of the specified points.
### Instance Properties
- [var center: Point3DFloat](rect3dfloat/center.md)
- [var cornerPoints: [Point3DFloat]](rect3dfloat/cornerpoints.md)
  Returns the corner points of the rectangle.
- [var integral: Rect3DFloat](rect3dfloat/integral.md)
- [var isEmpty: Bool](rect3dfloat/isempty.md)
- [var isNull: Bool](rect3dfloat/isnull.md)
- [var max: Point3DFloat](rect3dfloat/max.md)
- [var min: Point3DFloat](rect3dfloat/min.md)
- [var origin: Point3DFloat](rect3dfloat/origin.md)
  The origin of the rectangle.
- [var standardized: Rect3DFloat](rect3dfloat/standardized.md)
  Returns a rectangle with a positive width and height.
### Instance Methods
- [func applying(ScaledPose3DFloat) -> Rect3DFloat](rect3dfloat/applying(_:)-7i8x5.md)
  Returns the primitive that results from applying a scaled pose to the primitive.
- [func formInset(by: Size3DFloat)](rect3dfloat/forminset(by:).md)
  Insets the rectangle by the specified size.
- [func inset(by: Size3DFloat) -> Rect3DFloat](rect3dfloat/inset(by:).md)
- [func intersects(Rect3DFloat) -> Bool](rect3dfloat/intersects(_:).md)
- [func rotated(by: Rotation3DFloat, around: Point3DFloat) -> Rect3DFloat](rect3dfloat/rotated(by:around:)-1g90c.md)
- [func rotated(by: simd_quatf, around: Point3DFloat) -> Rect3DFloat](rect3dfloat/rotated(by:around:)-9yw64.md)
- [func sheared(AxisWithFactors) -> Rect3DFloat](rect3dfloat/sheared(_:).md)
  Returns a sheared rectangle.
- [func unapplying(ScaledPose3DFloat) -> Rect3DFloat](rect3dfloat/unapplying(_:)-4dm1d.md)
  Returns the primitive that results from applying a scaled pose to the primitive.
### Default Implementations
- [CustomReflectable Implementations](rect3dfloat/customreflectable-implementations.md)
- [Decodable Implementations](rect3dfloat/decodable-implementations.md)
- [Encodable Implementations](rect3dfloat/encodable-implementations.md)
- [Equatable Implementations](rect3dfloat/equatable-implementations.md)
- [Hashable Implementations](rect3dfloat/hashable-implementations.md)
- [Primitive3DProtocol Implementations](rect3dfloat/primitive3dprotocol-implementations.md)
- [Scalable3DProtocol Implementations](rect3dfloat/scalable3dprotocol-implementations.md)
- [VolumetricProtocol Implementations](rect3dfloat/volumetricprotocol-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Primitive3DProtocol](primitive3dprotocol.md)
- [ProjectiveTransformable3D](projectivetransformable3d.md)
- [ProjectiveTransformable3DFloat](projectivetransformable3dfloat.md)
- [Rotatable3DProtocol](rotatable3dprotocol.md)
- [Scalable3DProtocol](scalable3dprotocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpatialTypeProtocol](spatialtypeprotocol.md)
- [Translatable3DProtocol](translatable3dprotocol.md)
- [VolumetricProtocol](volumetricprotocol.md)

## See Also

- [struct Point3D](point3d.md)
  A point in a 3D coordinate system.
- [struct Point3DFloat](point3dfloat.md)
  A single-precision structure that contains a point in a three-dimensional coordinate system.
- [struct Size3D](size3d.md)
  A size that describes width, height, and depth in a 3D coordinate system.
- [struct Size3DFloat](size3dfloat.md)
  A single-precision structure that contains width, height, and depth values.
- [struct Rect3D](rect3d.md)
  A rectangle in a 3D coordinate system.
- [struct Rotation3D](rotation3d.md)
  A rotation in three dimensions.
- [struct Rotation3DFloat](rotation3dfloat.md)
  A single-precision structure that represents a rotation in three dimensions.
- [struct RotationAxis3D](rotationaxis3d.md)
  A 3D rotation axis.
- [struct RotationAxis3DFloat](rotationaxis3dfloat.md)
  A 3D axis.
- [struct Pose3D](pose3d.md)
  A structure that contains a 3D position and a 3D rotation.
- [struct Pose3DFloat](pose3dfloat.md)
  A single-precision structure that contains a position and rotation.
- [struct ScaledPose3D](scaledpose3d.md)
  A structure that contains a position, rotation, and scale.
- [struct ScaledPose3DFloat](scaledpose3dfloat.md)
  A structure that contains a position, rotation, and scale.
- [struct SphericalCoordinates3D](sphericalcoordinates3d.md)
  A structure that defines spherical coordinates in radial, inclination, azimuthal order.
- [struct SphericalCoordinates3DFloat](sphericalcoordinates3dfloat.md)
  A single-precision structure that defines spherical coordinates in radial, inclination, azimuthal order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3dfloat)*