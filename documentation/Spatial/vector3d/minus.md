# -(_:_:)

**Framework**: Spatial  
**Kind**: op

Returns a size that’s the element-wise difference of a point and a vector.

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
static func - (lhs: Point3D, rhs: Vector3D) -> Point3D
```

## Parameters

- `lhs`: The left-hand-side value.
- `rhs`: The right-hand-side value.

## See Also

- [static func * (Vector3D, Double) -> Vector3D](vector3d/*(_:_:)-dcwn.md)
  Returns a vector that’s the product of a vector and a scalar value.
- [static func * (Double, Vector3D) -> Vector3D](vector3d/*(_:_:)-64lzt.md)
  Returns a vector that’s the product of a scalar value and a vector.
- [static func * (AffineTransform3D, Vector3D) -> Vector3D](vector3d/*(_:_:)-6rxsr.md)
  Returns the vector that results from applying the affine transform to the vector.
- [static func * (ProjectiveTransform3D, Vector3D) -> Vector3D](vector3d/*(_:_:)-3dpli.md)
  Returns the vector that results from applying the projective transform to the vector.
- [static func * (Pose3D, Vector3D) -> Vector3D](vector3d/*(_:_:)-8y7xq.md)
  Returns a new vector after applying the pose to the vector.
- [static func + (Vector3D, Vector3D) -> Vector3D](vector3d/+(_:_:)-7gbcj.md)
  Returns a vector that’s the element-wise sum of two sizes.
- [static func + (Vector3D, Size3D) -> Size3D](vector3d/+(_:_:)-9xfxv.md)
  Returns a vector that’s the element-wise sum of a vector and a size.
- [static func + (Size3D, Vector3D) -> Size3D](vector3d/+(_:_:)-1xufx.md)
  Returns a vector that’s the element-wise sum of a size and a vector.
- [static func + (Vector3D, Point3D) -> Point3D](vector3d/+(_:_:)-1bq1m.md)
  Returns a vector that’s the element-wise sum of a vector and a point.
- [static func + (Point3D, Vector3D) -> Point3D](vector3d/+(_:_:)-4rsou.md)
  Returns a vector that’s the element-wise sum of a point and a vector.
- [static func - (Vector3D) -> Vector3D](vector3d/-(_:).md)
  Returns a vector that’s the element-wise negation of the vector.
- [static func - (Vector3D, Vector3D) -> Vector3D](vector3d/-(_:_:)-6zam.md)
  Returns a size that’s the element-wise difference of two vectors.
- [static func - (Vector3D, Size3D) -> Size3D](vector3d/-(_:_:)-6lui1.md)
  Returns a size that’s the element-wise difference of a vector and a size.
- [static func - (Size3D, Vector3D) -> Size3D](vector3d/-(_:_:)-3qpww.md)
  Returns a size that’s the element-wise difference of a size and a vector.
- [static func - (Vector3D, Point3D) -> Point3D](vector3d/-(_:_:)-1nz82.md)
  Returns a size that’s the element-wise difference of a vector and a point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/vector3d/-(_:_:)-8sgai)*