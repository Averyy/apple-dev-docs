# pointCount

**Framework**: PencilKit  
**Kind**: property

The total number of B-Spline control points in the path.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
let pointCount: Int
```

## Mentions

- [Importing Bézier path data into PencilKit](importing-external-drawing-data-into-pencilkit.md)

## See Also

- [let index: Int](pkstrokepath-swift.struct/convertedbezierpoint/index.md)
  The index of the point along the path.
- [let location: CGPoint](pkstrokepath-swift.struct/convertedbezierpoint/location.md)
  The location of the cubic uniform B-Spline control point.
- [let bezierSegmentIndex: Int](pkstrokepath-swift.struct/convertedbezierpoint/beziersegmentindex.md)
  The index of the Bézier segment the point originates from, not including `move to` elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/convertedbezierpoint/pointcount)*