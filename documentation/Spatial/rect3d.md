# Rect3D

**Framework**: Spatial  
**Kind**: struct

A rectangle in a 3D coordinate system.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct Rect3D
```

## Topics

### Creating a 3D rectangle structure
- [init()](rect3d/init.md)
  Creates a rectangle structure.
- [init(BoundingBox)](rect3d/init(_:).md)
  Creates a rectangle structure from a bounding box.
- [init(center: Point3D, size: Size3D)](rect3d/init(center:size:)-133fy.md)
  Creates a rectangle with the specified center and the specified size from Spatial structures.
- [init(center: simd_double3, size: simd_double3)](rect3d/init(center:size:)-77l0z.md)
  Creates a rectangle with the specified center and the specified size from double-precision vectors.
- [init(center: Vector3D, size: Vector3D)](rect3d/init(center:size:)-9cfq7.md)
  Creates a rectangle with the specified center and the specified size from Spatial vectors.
- [init(center: simd_float3, size: simd_float3)](rect3d/init(center:size:)-zr2x.md)
  Creates a rectangle with the specified center and the specified size from single-precision vectors.
- [init(origin: simd_double3, size: simd_double3)](rect3d/init(origin:size:)-5xyrs.md)
  Creates a rectangle at the specified origin with the specified size from double-precision vectors.
- [init(origin: simd_float3, size: simd_float3)](rect3d/init(origin:size:)-7fnuf.md)
  Creates a rectangle at the specified origin with the specified size from single-precision vectors.
- [init(origin: Vector3D, size: Vector3D)](rect3d/init(origin:size:)-7o8ad.md)
  Creates a rectangle with the specified origin and the specified size from Spatial vectors.
- [init(origin: Point3D, size: Size3D)](rect3d/init(origin:size:)-7v73.md)
  Creates a rectangle at the specified origin and the specified size from Spatial structures.
- [init(origin: Point3D, size: Size3D)](rect3d/init(origin:size:)-9a089.md)
  Creates a rectangle structure.
- [init(points: [Point3D])](rect3d/init(points:).md)
  Creates a rectangle that’s the bounding box of the specified points.
### Inspecting a 3D rectangle’s properties
- [var center: Point3D](rect3d/center.md)
  The center of the rectangle.
- [var cornerPoints: [Point3D]](rect3d/cornerpoints.md)
  The corner points of the rectangle.
- [var max: Point3D](rect3d/max.md)
  A point that represents the corner of the rectangle with the largest x-, y-, and z-coordinates.
- [var min: Point3D](rect3d/min.md)
  A point that represents the corner of the rectangle with the smallest x-, y-, and z-coordinates.
- [var origin: Point3D](rect3d/origin.md)
  The origin of the rectangle.
### Transforming a 3D rectangle structure
- [func applying(Pose3D) -> Rect3D](rect3d/applying(_:)-3qdiy.md)
  Returns a rectangle that results from applying the specified pose.
- [func applying(ScaledPose3D) -> Rect3D](rect3d/applying(_:)-5hnif.md)
  Returns a rectangle that’s transformed by the specified scaled pose.
- [func applying(ScaledPose3D) -> Rect3D](rect3d/applying(_:)-5hnif.md)
  Returns a rectangle that’s transformed by the specified scaled pose.
- [func rotated(by: Rotation3D, around: Point3D) -> Rect3D](rect3d/rotated(by:around:)-3ih62.md)
  Returns a rectangle that results from applying the specified rotation around a pivot point.
- [func rotated(by: simd_quatd, around: Point3D) -> Rect3D](rect3d/rotated(by:around:)-8g1c9.md)
  Returns a rectangle that results from rotating with the specified quaternion around a pivot point.
- [func scaledBy(x: Double, y: Double, z: Double) -> Rect3D](rect3d/scaledby(x:y:z:).md)
  Returns a rectangle that results from scaling with the specified double-precision values.
- [func sheared(AxisWithFactors) -> Rect3D](rect3d/sheared(_:).md)
  Returns a rectangle that results from shearing over an axis by shear factors for the other two axes.
- [func unapplying(ProjectiveTransform3D) -> Rect3D](rect3d/unapplying(_:)-1j6g7.md)
  Returns a rectangle that results from unapplying the specified projective transform.
- [func unapplying(ScaledPose3D) -> Rect3D](rect3d/unapplying(_:)-1pbfn.md)
  Returns a rectangle that’s transformed by the inverse of the specified scaled pose.
- [func unapplying(Pose3D) -> Rect3D](rect3d/unapplying(_:)-2he5i.md)
  Returns a rectangle that results from unapplying the specified pose.
- [func unapplying(AffineTransform3D) -> Rect3D](rect3d/unapplying(_:)-7eglq.md)
  Returns a rectangle that results from unapplying the specified affine transform.
### Checking characteristics
- [func contains(anyOf: [Point3D]) -> Bool](rect3d/contains(anyof:).md)
  Returns a Boolean value that indicates whether the rectangle contains any of the specified points.
- [func intersects(Rect3D) -> Bool](rect3d/intersects(_:).md)
  Returns a Boolean value that indicates whether two rectangles intersect.
- [var isEmpty: Bool](rect3d/isempty.md)
  A Boolean value that indicates whether two or three of the dimensions are zero.
### Creating derived 3D rectangles
- [var integral: Rect3D](rect3d/integral.md)
  Returns the smallest rectangle after converting the source rectangle values to integers.
- [func formInset(by: Size3D)](rect3d/forminset(by:).md)
  Insets the rectangle by the specified size.
- [func inset(by: Size3D) -> Rect3D](rect3d/inset(by:).md)
  Returns a new rectangle with the same center point after applying the specified inset amount.
- [func intersection(Rect3D) -> Rect3D?](rect3d/intersection(_:).md)
  Returns the intersection of two rectangles.
- [var standardized: Rect3D](rect3d/standardized.md)
  A rectangle with positive dimensions.
### Comparing values
- [static func == (Rect3D, Rect3D) -> Bool](rect3d/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
### Applying arithmetic operations
- [static func * (AffineTransform3D, Rect3D) -> Rect3D](rect3d/*(_:_:)-8710d.md)
  Returns the rectangle that results from applying the affine transform to the rectangle.
- [static func * (ProjectiveTransform3D, Rect3D) -> Rect3D](rect3d/*(_:_:)-8vu0.md)
  Returns the rectangle that results from applying the projective transform to the rectangle.
- [static func * (Pose3D, Rect3D) -> Rect3D](rect3d/*(_:_:)-5lqdv.md)
  Returns a new rectangle after applying the pose to the rectangle.
### Deprecated symbols
- [func distance(to: Rect3D) -> Double](rect3d/distance(to:).md)
  Returns the distance between the origins of two rectangle.
- [func containsAny(of: [Point3D]) -> Bool](rect3d/containsany(of:).md)
  Returns a Boolean value that indicates whether the rectangle contains any of the specified points.
- [func rotation(to: Rect3D) -> Rotation3D](rect3d/rotation(to:).md)
  Returns the rotation around @p (0,0,0)  from the first rectangle to the second rectangle.
- [var maxX: Double](rect3d/maxx.md)
- [var maxY: Double](rect3d/maxy.md)
- [var maxZ: Double](rect3d/maxz.md)
- [var midX: Double](rect3d/midx.md)
- [var midY: Double](rect3d/midy.md)
- [var midZ: Double](rect3d/midz.md)
- [var minX: Double](rect3d/minx.md)
- [var minY: Double](rect3d/miny.md)
- [var minZ: Double](rect3d/minz.md)
### Default Implementations
- [CustomReflectable Implementations](rect3d/customreflectable-implementations.md)
- [Decodable Implementations](rect3d/decodable-implementations.md)
- [Encodable Implementations](rect3d/encodable-implementations.md)
- [Equatable Implementations](rect3d/equatable-implementations.md)
- [Hashable Implementations](rect3d/hashable-implementations.md)
- [Primitive3D Implementations](rect3d/primitive3d-implementations.md)
- [Scalable3D Implementations](rect3d/scalable3d-implementations.md)
- [Shearable3D Implementations](rect3d/shearable3d-implementations.md)
- [Volumetric Implementations](rect3d/volumetric-implementations.md)

## Relationships

### Conforms To
- [Animatable](../SwiftUI/Animatable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Primitive3D](primitive3d.md)
- [Rotatable3D](rotatable3d.md)
- [Scalable3D](scalable3d.md)
- [Sendable](../Swift/Sendable.md)
- [Shearable3D](shearable3d.md)
- [Translatable3D](translatable3d.md)
- [Volumetric](volumetric.md)

## See Also

- [struct Point3D](point3d.md)
  A point in a 3D coordinate system.
- [struct Size3D](size3d.md)
  A size that describes width, height, and depth in a 3D coordinate system.
- [struct Rotation3D](rotation3d.md)
  A rotation in three dimensions.
- [struct RotationAxis3D](rotationaxis3d.md)
  A 3D rotation axis.
- [struct Pose3D](pose3d.md)
  A structure that contains a 3D position and a 3D rotation.
- [struct ScaledPose3D](scaledpose3d.md)
  A structure that contains a position, rotation, and scale.
- [struct SphericalCoordinates3D](sphericalcoordinates3d.md)
  A structure that defines spherical coordinates in radial, inclination, azimuthal order.
- [struct Ray3D](ray3d.md)
  A ray in a 3D coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d)*