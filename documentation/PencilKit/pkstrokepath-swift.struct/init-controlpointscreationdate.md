# init(controlPoints:creationDate:)

**Framework**: PencilKit  
**Kind**: init

Creates a stroke path with the cubic B-spline control points and a date that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init<T>(controlPoints: T, creationDate: Date) where T : Sequence, T.Element == PKStrokePoint
```

## Parameters

- `controlPoints`: An array of control points for a cubic B-spline.
- `creationDate`: The creation time of this path. The `timeOffset` of points in this stroke path is relative to this date.

## See Also

- [init()](pkstrokepath-swift.struct/init.md)
  Creates an empty stroke path.
- [init<T>(controlPoints: T, creationDate: Date, id: UUID)](pkstrokepath-swift.struct/init(controlpoints:creationdate:id:).md)
  Creates a stroke path with the specified cubic B-spline control points and a unique identifier.
- [init(bezierPath: CGPath, creationDate: Date, pointProvider: (PKStrokePath.ConvertedBezierPoint) -> PKStrokePoint)](pkstrokepath-swift.struct/init(bezierpath:creationdate:pointprovider:).md)
  Creates a stroke path recreating the specified Bézier path as a cubic uniform B-Spline.
- [PKStrokePath.ConvertedBezierPoint](pkstrokepath-swift.struct/convertedbezierpoint.md)
  Information about a B-spline control point converted from a Bézier path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/init(controlpoints:creationdate:))*