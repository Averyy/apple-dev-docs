# init(controlPoints:creationDate:id:)

**Framework**: PencilKit  
**Kind**: init

Creates a stroke path with the specified cubic B-spline control points and a unique identifier.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init<T>(controlPoints: T, creationDate: Date, id: UUID) where T : Sequence, T.Element == PKStrokePoint
```

#### Discussion

> ⚠️ **Warning**: Using multiple stroke paths with identical IDs but different control points will result in undefined rendering behavior. Ensure each stroke path has a unique identifier.

## Parameters

- `controlPoints`: An array of control points for a cubic B-spline.
- `creationDate`: The start time of this path.
- `id`: The unique identity of the path.

## See Also

- [init()](pkstrokepath-swift.struct/init.md)
  Creates an empty stroke path.
- [init<T>(controlPoints: T, creationDate: Date)](pkstrokepath-swift.struct/init(controlpoints:creationdate:).md)
  Creates a stroke path with the cubic B-spline control points and a date that you specify.
- [init(bezierPath: CGPath, creationDate: Date, pointProvider: (PKStrokePath.ConvertedBezierPoint) -> PKStrokePoint)](pkstrokepath-swift.struct/init(bezierpath:creationdate:pointprovider:).md)
  Creates a stroke path recreating the specified Bézier path as a cubic uniform B-Spline.
- [PKStrokePath.ConvertedBezierPoint](pkstrokepath-swift.struct/convertedbezierpoint.md)
  Information about a B-spline control point converted from a Bézier path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/init(controlpoints:creationdate:id:))*