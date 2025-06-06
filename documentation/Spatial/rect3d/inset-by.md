# inset(by:)

**Framework**: Spatial  
**Kind**: method

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

#### Return Value

A new rectangle with the same center point after applying the specified inset amount.

## Parameters

- `dXYZ`: The size structure that defines the inset values.

## See Also

- [var integral: Rect3D](rect3d/integral.md)
  Returns the smallest rectangle after converting the source rectangle values to integers.
- [func formInset(by: Size3D)](rect3d/forminset(by:).md)
  Insets the rectangle by the specified size.
- [func intersection(Rect3D) -> Rect3D?](rect3d/intersection(_:).md)
  Returns the intersection of two rectangles.
- [var standardized: Rect3D](rect3d/standardized.md)
  A rectangle with positive dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d/inset(by:))*