# init(controlPoints:creationDate:id:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Creates a stroke path with the specified cubic B-spline control points and a unique identifier.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

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

### Creating a new stroke path
- [init()](./init%28%29.md)
  Creates an empty stroke path.
- [init<T>(controlPoints: T, creationDate: Date)](./init%28controlpoints,creationdate%29.md)
  Creates a stroke path with the cubic B-spline control points and a date that you specify.
- [init(bezierPath: CGPath, creationDate: Date, pointProvider: (PKStrokePath.ConvertedBezierPoint) -> PKStrokePoint)](./init%28bezierpath,creationdate,pointprovider%29.md)
  Creates a stroke path recreating the specified Bézier path as a cubic uniform B-Spline.
- [PKStrokePath.ConvertedBezierPoint](./convertedbezierpoint.md)
  Information about a B-spline control point converted from a Bézier path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/init(controlpoints:creationdate:id:))*