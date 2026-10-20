# pointCount

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

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

- [Importing Bézier path data into PencilKit](../../importing-external-drawing-data-into-pencilkit.md)

## See Also

### Getting the point data
- [let index: Int](./index.md)
  The index of the point along the path.
- [let location: CGPoint](./location.md)
  The location of the cubic uniform B-Spline control point.
- [let bezierSegmentIndex: Int](./beziersegmentindex.md)
  The index of the Bézier segment the point originates from, not including `move to` elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/convertedbezierpoint/pointcount)*