# rotation(to:)

**Framework**: Spatial  
**Kind**: method

Returns the rotation around @p (0,0,0)  from the first rectangle to the second rectangle.

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
func rotation(to other: Rect3D) -> Rotation3D
```

## See Also

- [func distance(to: Rect3D) -> Double](rect3d/distance(to:).md)
  Returns the distance between the origins of two rectangle.
- [func containsAny(of: [Point3D]) -> Bool](rect3d/containsany(of:).md)
  Returns a Boolean value that indicates whether the rectangle contains any of the specified points.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d/rotation(to:))*