# standardized

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

A rectangle with positive dimensions.

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
var standardized: Rect3D { get }
```

```c
static SPRect3D SPRect3DStandardize(SPRect3D rect);
```

## See Also

### Creating derived 3D rectangles
- [var integral: Rect3D](./integral.md)
  Returns the smallest rectangle after converting the source rectangle values to integers.
- [func formInset(by: Size3D)](./forminset%28by%29.md)
  Insets the rectangle by the specified size.
- [func inset(by: Size3D) -> Rect3D](./inset%28by%29.md)
  Returns a new rectangle with the same center point after applying the specified inset amount.
- [func intersection(Rect3D) -> Rect3D?](./intersection%28_%29.md)
  Returns the intersection of two rectangles.
- [SPRect3DIntersection](../sprect3dintersection.md)
  Returns the intersection of two rectangles.
- [SPRect3DUnion](../sprect3dunion.md)
  Returns the smallest rectangle that contains two rectangles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d/standardized)*