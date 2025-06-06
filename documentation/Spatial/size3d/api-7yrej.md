# +=(_:_:)

**Framework**: Spatial  
**Kind**: op

Adds a size and a vector, and stores the result in the left-hand-side variable.

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
static func += (lhs: inout Size3D, rhs: Vector3D)
```

## Parameters

- `lhs`: The left-hand-side value.
- `rhs`: The right-hand-side value.

## See Also

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
- [static func -= (inout Size3D, Size3D)](size3d/-=(_:_:)-8t5kg.md)
  Subtracts a size from a size and stores the difference in the left-hand-side variable.
- [static func -= (inout Size3D, Vector3D)](size3d/-=(_:_:)-3te52.md)
  Subtracts a size from a vector and stores the difference in the left-hand-side variable.
- [static func / (Size3D, Double) -> Size3D](size3d/_(_:_:).md)
  Returns a size with each element divided by a scalar value.
- [static func /= (inout Size3D, Double)](size3d/_=(_:_:).md)
  Divides a size by a scalar vaue and stores the result in the left-hand-side variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/size3d/+=(_:_:)-7yrej)*