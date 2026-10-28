# SPRect3DDistanceToRect

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 16.0+ - Deprecated in 16.0
- iPadOS 16.0+ - Deprecated in 16.0
- Mac Catalyst 16.0+ - Deprecated in 16.0
- macOS 13.0+ - Deprecated in 13.0
- tvOS 16.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.0+ - Deprecated in 9.0

## Declaration

```c
static double SPRect3DDistanceToRect(SPRect3D rect, SPRect3D other);
```

## Return Value

The distance between the two rectangle.

## Discussion

Returns the distance between the origins of two rectangle.

## Parameters

- `rect`: The first rectangle.
- `other`: The second rectangle.

## See Also

### Checking characteristics
- [func intersects(Rect3D) -> Bool](./rect3d/intersects%28_%29.md)
  Returns a Boolean value that indicates whether two rectangles intersect.
- [var isEmpty: Bool](./rect3d/isempty.md)
  A Boolean value that indicates whether two or three of the dimensions are zero.
- [SPRect3DContainsAnyPoint](./sprect3dcontainsanypoint.md)
  Returns a Boolean value that indicates whether the rectangle contains any of the specified points.
- [SPRect3DContainsPoint](./sprect3dcontainspoint.md)
  Returns a Boolean value that indicates whether the rectangle contains the specified point.
- [SPRect3DContainsRect](./sprect3dcontainsrect.md)
  Returns a Boolean value that indicates whether the rectangle contains the specified rectangle.
- [SPRect3DIsFinite](./sprect3disfinite.md)
  A Boolean value that indicates whether all of the coordinates and dimensions of the rectangle are finite.
- [SPRect3DIsNaN](./sprect3disnan.md)
  A Boolean value that indicates whether any of the coordinates and dimensions of the rectangle are NaN.
- [SPRect3DIsNull](./sprect3disnull.md)
  A Boolean value that indicates whether the rectangle is equal to the null rectangle.
- [SPRect3DIsZero](./sprect3diszero.md)
  A Boolean value that indicates whether the rectangle’s origin and size are zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3ddistancetorect)*