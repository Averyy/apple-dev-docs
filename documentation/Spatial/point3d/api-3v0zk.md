# +=(_:_:)

**Framework**: Spatial  
**Kind**: op

Adds a point and a size, and stores the result in the left-hand-side variable.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static func += (lhs: inout Point3D, rhs: Size3D)
```

## Parameters

- `lhs`: The left-hand-side value.
- `rhs`: The right-hand-side value.

## See Also

- [static func * (Point3D, Double) -> Point3D](point3d/*(_:_:)-9rqvh.md)
  Returns a point that’s the product of a point and a scalar value.
- [static func * (Double, Point3D) -> Point3D](point3d/*(_:_:)-9w7dk.md)
  Returns a point that’s the product of a scalar value and a point.
- [static func * (AffineTransform3D, Point3D) -> Point3D](point3d/*(_:_:)-8ewep.md)
  Returns the point that results from applying the affine transform to the point.
- [static func * (ProjectiveTransform3D, Point3D) -> Point3D](point3d/*(_:_:)-9ak06.md)
  Returns the point that results from applying the projective transform to the point.
- [static func * (Pose3D, Point3D) -> Point3D](point3d/*(_:_:)-8wgkb.md)
  Returns a new point after applying the pose to the point.
- [static func + (Point3D, Size3D) -> Point3D](point3d/+(_:_:)-5v6x4.md)
  Returns a point that’s the element-wise sum of a point and a size.
- [static func + (Size3D, Point3D) -> Point3D](point3d/+(_:_:)-4g55.md)
  Returns a point that’s the element-wise sum of a size and a point.
- [static func - (Point3D) -> Point3D](point3d/-(_:).md)
  Returns a point that’s the element-wise negation of the point.
- [static func - (Point3D, Size3D) -> Point3D](point3d/-(_:_:)-6om9g.md)
  Returns a point that’s the element-wise difference of a point and a size.
- [static func - (Point3D, Point3D) -> Vector3D](point3d/-(_:_:)-9l6rn.md)
  Returns a point that’s the element-wise difference of two points.
- [static func - (Size3D, Point3D) -> Point3D](point3d/-(_:_:)-5t01r.md)
  Returns a point that’s the element-wise difference of a size and a point.
- [static func += (inout Point3D, Vector3D)](point3d/+=(_:_:)-80hjz.md)
  Adds a point and a vector, and stores the result in the left-hand-side variable.
- [static func -= (inout Point3D, Vector3D)](point3d/-=(_:_:)-23bow.md)
  Subtracts a vector from a point and stores the difference in the left-hand-side variable.
- [static func -= (inout Point3D, Size3D)](point3d/-=(_:_:)-9xu2.md)
  Subtracts a vector from a point and stores the difference in the left-hand-side variable.
- [static func *= (inout Point3D, Double)](point3d/*=(_:_:).md)
  Multiplies a point and a double-precision value, and stores the result in the left-hand-side variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/point3d/+=(_:_:)-3v0zk)*