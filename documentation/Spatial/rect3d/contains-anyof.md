# contains(anyOf:)

**Framework**: Spatial  
**Kind**: method

Returns a Boolean value that indicates whether the rectangle contains any of the specified points.

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
func contains(anyOf points: [Point3D]) -> Bool
```

#### Return Value

A Boolean value that indicates whether the rectangle contains any of the specified points.

## Parameters

- `points`: The array of points that the function compares against.

## See Also

- [func intersects(Rect3D) -> Bool](rect3d/intersects(_:).md)
  Returns a Boolean value that indicates whether two rectangles intersect.
- [var isEmpty: Bool](rect3d/isempty.md)
  A Boolean value that indicates whether two or three of the dimensions are zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d/contains(anyof:))*