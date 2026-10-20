# intersects(_:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether two rectangles intersect.

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
func intersects(_ other: Rect3D) -> Bool
```

```c
static bool SPRect3DIntersectsRect(SPRect3D rect, SPRect3D other);
```

#### Return Value

A Boolean value that indicates whether two rectangles intersect.

## Parameters

- `other`: The rectangle that the function compares against.

## See Also

### Checking characteristics
- [func contains(anyOf: [Point3D]) -> Bool](./contains%28anyof%29.md)
  Returns a Boolean value that indicates whether the rectangle contains any of the specified points.
- [var isEmpty: Bool](./isempty.md)
  A Boolean value that indicates whether two or three of the dimensions are zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d/intersects(_:))*