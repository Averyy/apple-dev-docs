# containsAny(of:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the rectangle contains any of the specified points.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func containsAny(of points: [Point3D]) -> Bool
```

#### Return Value

A Boolean value that indicates whether the rectangle contains any of the specified points.

## Parameters

- `points`: The array of points that the function compares against.

## See Also

### Deprecated symbols
- [func distance(to: Rect3D) -> Double](./distance%28to%29.md)
  Returns the distance between the origins of two rectangle.
- [func rotation(to: Rect3D) -> Rotation3D](./rotation%28to%29.md)
  Returns the rotation around @p (0,0,0)  from the first rectangle to the second rectangle.
- [var maxX: Double](./maxx.md)
- [var maxY: Double](./maxy.md)
- [var maxZ: Double](./maxz.md)
- [var midX: Double](./midx.md)
- [var midY: Double](./midy.md)
- [var midZ: Double](./midz.md)
- [var minX: Double](./minx.md)
- [var minY: Double](./miny.md)
- [var minZ: Double](./minz.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rect3d/containsany(of:))*