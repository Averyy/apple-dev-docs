# Size3D

**Framework**: Spatial  
**Kind**: struct

A size that describes width, height, and depth in a 3D coordinate system.

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
struct Size3D
```

## Topics

### Creating a 3D size structure
- [init()](size3d/init.md)
  Creates a size structure.
- [init(width: Double, height: Double, depth: Double)](size3d/init(width:height:depth:)-4j9bk.md)
  Creates a size structure from the specified double-precision values.
- [init<T>(width: T, height: T, depth: T)](size3d/init(width:height:depth:)-4kscw.md)
  Creates a size structure from the specified floating-point values.
- [init(simd_float3)](size3d/init(_:)-2ibhr.md)
  Creates a size structure from the specified single-precision vector.
- [init(simd_double3)](size3d/init(_:)-3y7nr.md)
  Creates a size structure from the specified double-precision vector.
- [init(vector: simd_double3)](size3d/init(vector:).md)
  Creates a size structure from the specified double-precision vector.
- [init(Point3D)](size3d/init(_:)-7kyp0.md)
  Creates a size structure from the specified Spatial point.
- [init(Vector3D)](size3d/init(_:)-6nss1.md)
  Creates a size structure from the specified Spatial vector.
### Inspecting a 3D size’s properties
- [var width: Double](size3d/width.md)
  The width value.
- [var height: Double](size3d/height.md)
  The height value.
- [var depth: Double](size3d/depth.md)
  The depth value.
- [var size: Size3D](size3d/size.md)
  The size value.
- [var vector: simd_double3](size3d/vector.md)
### Transforming a 3D size structure
- [func applying(Pose3D) -> Size3D](size3d/applying(_:)-85mlm.md)
  Returns a size that results from applying the specified pose.
- [func applying(ScaledPose3D) -> Size3D](size3d/applying(_:)-7e2pf.md)
  Returns a size that’s transformed by the specified scaled pose.
- [func applying(Pose3D) -> Size3D](size3d/applying(_:)-85mlm.md)
  Returns a size that results from applying the specified pose.
- [func unapplying(AffineTransform3D) -> Size3D](size3d/unapplying(_:)-7qam3.md)
  Returns a size that results from unapplying the specified affine transform.
- [func unapplying(ProjectiveTransform3D) -> Size3D](size3d/unapplying(_:)-yock.md)
  Returns a size that results from unapplying the specified projective transform.
- [func unapplying(Pose3D) -> Size3D](size3d/unapplying(_:)-3ip2e.md)
  Returns a size that results from unapplying the specified pose.
- [func sheared(AxisWithFactors) -> Size3D](size3d/sheared(_:).md)
  Returns a size that results from shearing over an axis by shear factors for the other two axes.
- [func applying(ScaledPose3D) -> Size3D](size3d/applying(_:)-7e2pf.md)
  Returns a size that’s transformed by the specified scaled pose.
- [func unapplying(ScaledPose3D) -> Size3D](size3d/unapplying(_:)-42rsa.md)
  Returns a size that’s transformed by the inverse of the specified scaled pose.
### Checking characteristics
- [func contains(anyOf: [Point3D]) -> Bool](size3d/contains(anyof:).md)
  Returns a Boolean value that indicates whether the size contains the specified point.
### Creating derived 3D sizes
- [func intersection(Size3D) -> Size3D?](size3d/intersection(_:).md)
  Returns the intersection of two sizes.
### Comparing values
- [static func == (Size3D, Size3D) -> Bool](size3d/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
### 3D size constants
- [static let one: Size3D](size3d/one.md)
  The size structure with width, height, and depth values of one.
### Applying arithmetic operations
- [static func * (Size3D, Double) -> Size3D](size3d/*(_:_:)-751dt.md)
  Returns a size that’s the product of a size and a scalar value.
- [static func * (Double, Size3D) -> Size3D](size3d/*(_:_:)-8zb5j.md)
  Returns a size that’s the product of a scalar value and a size.
- [static func * (AffineTransform3D, Size3D) -> Size3D](size3d/*(_:_:)-4qpgt.md)
  Returns the size that results from applying the affine transform to the size.
- [static func * (ProjectiveTransform3D, Size3D) -> Size3D](size3d/*(_:_:)-52miz.md)
  Returns the size that results from applying the projective transform to the size.
- [static func * (Pose3D, Size3D) -> Size3D](size3d/*(_:_:)-5bb1n.md)
  Returns a new size after applying the pose to the size.
- [static func + (Size3D, Size3D) -> Size3D](size3d/+(_:_:).md)
  Returns a size that’s the element-wise sum of two sizes.
- [static func - (Size3D) -> Size3D](size3d/-(_:).md)
  Returns a size that’s the element-wise negation of the size.
- [static func - (Size3D, Size3D) -> Size3D](size3d/-(_:_:).md)
  Returns a size that’s the element-wise difference of two points.
- [static func *= (inout Size3D, Double)](size3d/*=(_:_:).md)
  Multiplies a size and a double-precision value, and stores the result in the left-hand-side variable.
- [static func += (inout Size3D, Size3D)](size3d/+=(_:_:)-75tn3.md)
  Adds two size structures and stores the result in the left-hand-side variable.
- [static func += (inout Size3D, Vector3D)](size3d/+=(_:_:)-7yrej.md)
  Adds a size and a vector, and stores the result in the left-hand-side variable.
- [static func -= (inout Size3D, Size3D)](size3d/-=(_:_:)-8t5kg.md)
  Subtracts a size from a size and stores the difference in the left-hand-side variable.
- [static func -= (inout Size3D, Vector3D)](size3d/-=(_:_:)-3te52.md)
  Subtracts a size from a vector and stores the difference in the left-hand-side variable.
- [static func / (Size3D, Double) -> Size3D](size3d/_(_:_:).md)
  Returns a size with each element divided by a scalar value.
- [static func /= (inout Size3D, Double)](size3d/_=(_:_:).md)
  Divides a size by a scalar vaue and stores the result in the left-hand-side variable.
### Deprecated symbols
- [var simd: simd_double3](size3d/simd.md)
- [func containsAny(of: [Point3D]) -> Bool](size3d/containsany(of:).md)
  Returns a Boolean value that indicates whether the size contains the specified point.
### Default Implementations
- [AdditiveArithmetic Implementations](size3d/additivearithmetic-implementations.md)
- [CustomReflectable Implementations](size3d/customreflectable-implementations.md)
- [Decodable Implementations](size3d/decodable-implementations.md)
- [Encodable Implementations](size3d/encodable-implementations.md)
- [Equatable Implementations](size3d/equatable-implementations.md)
- [Hashable Implementations](size3d/hashable-implementations.md)
- [Primitive3D Implementations](size3d/primitive3d-implementations.md)
- [Scalable3D Implementations](size3d/scalable3d-implementations.md)
- [Shearable3D Implementations](size3d/shearable3d-implementations.md)
- [Volumetric Implementations](size3d/volumetric-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](../Swift/AdditiveArithmetic.md)
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
- [VectorArithmetic](../SwiftUI/VectorArithmetic.md)
- [Volumetric](volumetric.md)

## See Also

- [struct Point3D](point3d.md)
  A point in a 3D coordinate system.
- [struct Rect3D](rect3d.md)
  A rectangle in a 3D coordinate system.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/size3d)*