# bezierSegmentIndex

**Framework**: PencilKit  
**Kind**: property

The index of the Bézier segment the point originates from, not including `move to` elements.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var bezierSegmentIndex: Int { get }
```

## See Also

- [var index: Int](pkconvertedbezierpointreference/index.md)
  The index of the point along the path.
- [var pointCount: Int](pkconvertedbezierpointreference/pointcount.md)
  The total number of B-Spline control points in the path.
- [var location: CGPoint](pkconvertedbezierpointreference/location.md)
  The location of the cubic uniform B-Spline control point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkconvertedbezierpointreference/beziersegmentindex)*