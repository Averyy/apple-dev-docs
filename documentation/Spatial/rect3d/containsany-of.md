# containsAny(of:)

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
- Unknown ?+ - Deprecated

## Declaration

```swift
func containsAny(of points: [Point3D]) -> Bool
```

#### Return Value

A Boolean value that indicates whether the rectangle contains any of the specified points.

## Parameters

- `points`: The array of points that the function compares against.

## See Also

- [func distance(to: Rect3D) -> Double](rect3d/distance(to:).md)
  Returns the distance between the origins of two rectangle.
- [func rotation(to: Rect3D) -> Rotation3D](rect3d/rotation(to:).md)
  Returns the rotation around @p (0,0,0)  from the first rectangle to the second rectangle.
- [var maxX: Double](rect3d/maxx.md)
- [var maxY: Double](rect3d/maxy.md)
- [var maxZ: Double](rect3d/maxz.md)
- [var midX: Double](rect3d/midx.md)
- [var midY: Double](rect3d/midy.md)
- [var midZ: Double](rect3d/midz.md)
- [var minX: Double](rect3d/minx.md)
- [var minY: Double](rect3d/miny.md)
- [var minZ: Double](rect3d/minz.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d/containsany(of:))*