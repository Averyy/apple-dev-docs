# inset(by:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a new rectangle with the same center point after applying the specified inset amount.

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
func inset(by dXYZ: Size3D) -> Rect3D
```

```c
static SPRect3D SPRect3DInset(SPRect3D rect, SPSize3D dXYZ);
```

## Return Value

A new rectangle with the same center point after applying the specified inset amount.

## Parameters

- `dXYZ`: The size structure that defines the inset values.

## See Also

### Creating derived 3D rectangles
- [var integral: Rect3D](./integral.md)
  Returns the smallest rectangle after converting the source rectangle values to integers.
- [func formInset(by: Size3D)](./forminset%28by%29.md)
  Insets the rectangle by the specified size.
- [func intersection(Rect3D) -> Rect3D?](./intersection%28_%29.md)
  Returns the intersection of two rectangles.
- [var standardized: Rect3D](./standardized.md)
  A rectangle with positive dimensions.
- [SPRect3DIntersection](../sprect3dintersection.md)
  Returns the intersection of two rectangles.
- [SPRect3DUnion](../sprect3dunion.md)
  Returns the smallest rectangle that contains two rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d/inset(by:))*