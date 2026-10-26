# SPRect3DUnion

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

Returns the smallest rectangle that contains two rectangles.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static SPRect3D SPRect3DUnion(SPRect3D rect, SPRect3D other);
```

#### Return Value

A new rectangle that is the union of two rectangles.

## Parameters

- `rect`: The rectangle to compare.
- `other`: The rectangle that the function compares against.

## See Also

### Creating derived 3D rectangles
- [var integral: Rect3D](./rect3d/integral.md)
  Returns the smallest rectangle after converting the source rectangle values to integers.
- [func inset(by: Size3D) -> Rect3D](./rect3d/inset%28by%29.md)
  Returns a new rectangle with the same center point after applying the specified inset amount.
- [var standardized: Rect3D](./rect3d/standardized.md)
  A rectangle with positive dimensions.
- [SPRect3DIntersection](./sprect3dintersection.md)
  Returns the intersection of two rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sprect3dunion)*