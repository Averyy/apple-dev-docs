# *(_:_:)

**Framework**: Spatial  
**Kind**: op

Returns a new rectangle after applying the pose to the rectangle.

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
static func * (lhs: Pose3D, rhs: Rect3D) -> Rect3D
```

## Parameters

- `lhs`: The left-hand-side value.
- `rhs`: The right-hand-side value.

## See Also

- [static func * (AffineTransform3D, Rect3D) -> Rect3D](rect3d/*(_:_:)-8710d.md)
  Returns the rectangle that results from applying the affine transform to the rectangle.
- [static func * (ProjectiveTransform3D, Rect3D) -> Rect3D](rect3d/*(_:_:)-8vu0.md)
  Returns the rectangle that results from applying the projective transform to the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d/*(_:_:)-5lqdv)*