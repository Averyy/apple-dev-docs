# PKStrokePath.ConvertedBezierPoint

**Framework**: PencilKit  
**Kind**: struct

Information about a B-spline control point converted from a Bézier path.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ConvertedBezierPoint
```

#### Overview

`ConvertedBezierPoint` values are passed one at a time to the `pointProvider` closure of [`init(bezierPath:creationDate:pointProvider:)`](pkstrokepath-swift.struct/init(bezierpath:creationdate:pointprovider:).md). Use the provided location, index, and segment information to initialize each `PKStrokePoint` with appropriate size, opacity, force, and other drawing properties.

## Topics

### Getting the point data
- [let index: Int](pkstrokepath-swift.struct/convertedbezierpoint/index.md)
  The index of the point along the path.
- [let pointCount: Int](pkstrokepath-swift.struct/convertedbezierpoint/pointcount.md)
  The total number of B-Spline control points in the path.
- [let location: CGPoint](pkstrokepath-swift.struct/convertedbezierpoint/location.md)
  The location of the cubic uniform B-Spline control point.
- [let bezierSegmentIndex: Int](pkstrokepath-swift.struct/convertedbezierpoint/beziersegmentindex.md)
  The index of the Bézier segment the point originates from, not including `move to` elements.
### Using reference types
- [class PKConvertedBezierPointReference](pkconvertedbezierpointreference.md)
  An object that provides information about a B-spline control point converted from a Bézier path.

## See Also

- [init()](pkstrokepath-swift.struct/init.md)
  Creates an empty stroke path.
- [init<T>(controlPoints: T, creationDate: Date)](pkstrokepath-swift.struct/init(controlpoints:creationdate:).md)
  Creates a stroke path with the cubic B-spline control points and a date that you specify.
- [init<T>(controlPoints: T, creationDate: Date, id: UUID)](pkstrokepath-swift.struct/init(controlpoints:creationdate:id:).md)
  Creates a stroke path with the specified cubic B-spline control points and a unique identifier.
- [init(bezierPath: CGPath, creationDate: Date, pointProvider: (PKStrokePath.ConvertedBezierPoint) -> PKStrokePoint)](pkstrokepath-swift.struct/init(bezierpath:creationdate:pointprovider:).md)
  Creates a stroke path recreating the specified Bézier path as a cubic uniform B-Spline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/convertedbezierpoint)*