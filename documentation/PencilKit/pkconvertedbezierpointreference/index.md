# index

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

The index of the point along the path.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var index: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSInteger index;
```

## See Also

### Getting the point data
- [var pointCount: Int](./pointcount.md)
  The total number of B-Spline control points in the path.
- [var location: CGPoint](./location.md)
  The location of the cubic uniform B-Spline control point.
- [var bezierSegmentIndex: Int](./beziersegmentindex.md)
  The index of the Bézier segment the point originates from, not including `move to` elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkconvertedbezierpointreference/index)*