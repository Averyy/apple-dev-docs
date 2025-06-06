# intersection(_:)

**Framework**: Spatial  
**Kind**: method

Returns the intersection of two rectangles.

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
func intersection(_ other: Rect3D) -> Rect3D?
```

#### Return Value

A new rectangle that is the intersection of two rectangles.

## Parameters

- `other`: The rectangle that the function compares against.

## See Also

- [var integral: Rect3D](rect3d/integral.md)
  Returns the smallest rectangle after converting the source rectangle values to integers.
- [func formInset(by: Size3D)](rect3d/forminset(by:).md)
  Insets the rectangle by the specified size.
- [func inset(by: Size3D) -> Rect3D](rect3d/inset(by:).md)
  Returns a new rectangle with the same center point after applying the specified inset amount.
- [var standardized: Rect3D](rect3d/standardized.md)
  A rectangle with positive dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d/intersection(_:))*