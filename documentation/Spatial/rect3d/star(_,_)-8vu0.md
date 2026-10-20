# *(_:_:)

**Framework**: Spatial  
**Kind**: op  
**Role**: Operator

Returns the rectangle that results from applying the projective transform to the rectangle.

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
static func * (lhs: ProjectiveTransform3D, rhs: Rect3D) -> Rect3D
```

## Parameters

- `lhs`: The left-hand-side value.
- `rhs`: The right-hand-side value.

## See Also

### Applying arithmetic operations
- [static func * (AffineTransform3D, Rect3D) -> Rect3D](./star%28_,_%29-8710d.md)
  Returns the rectangle that results from applying the affine transform to the rectangle.
- [static func * (Pose3D, Rect3D) -> Rect3D](./star%28_,_%29-5lqdv.md)
  Returns a new rectangle after applying the pose to the rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d/*(_:_:)-8vu0)*