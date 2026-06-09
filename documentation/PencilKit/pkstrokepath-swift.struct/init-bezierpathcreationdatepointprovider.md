# init(bezierPath:creationDate:pointProvider:)

**Framework**: PencilKit  
**Kind**: init

Creates a stroke path recreating the specified Bézier path as a cubic uniform B-Spline.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(bezierPath: CGPath, creationDate: Date, pointProvider: (PKStrokePath.ConvertedBezierPoint) -> PKStrokePoint)
```

#### Discussion

The count of control points of the generated spline is not guaranteed to be a specific value except when the provided path is the output of `bezierRepresentation->CGPath`, where it will match the original curve.

The output B-Spline will have continuous curvature and 0 curvature at the endpoints. In cases where the B-Spline cannot fully recreate the Bézier path, it will be an approximation. For example, if the given Bézier path includes `line to` elements, these will produce straight line segments in the resulting B-Spline, but if a `line to` element is adjacent to a `curve to` element, the resulting curve may not match the original.

> ⚠️ **Warning**: For a Bézier path with multiple subpaths, only the first will be converted.

## Parameters

- `bezierPath`: The Bézier path to convert to a cubic uniform B-Spline
- `creationDate`: The start time of this path.
- `pointProvider`: Closure to initialize the `PKStrokePoint`s of the path with specific values.

## See Also

- [init()](pkstrokepath-swift.struct/init.md)
  Creates an empty stroke path.
- [init<T>(controlPoints: T, creationDate: Date)](pkstrokepath-swift.struct/init(controlpoints:creationdate:).md)
  Creates a stroke path with the cubic B-spline control points and a date that you specify.
- [init<T>(controlPoints: T, creationDate: Date, id: UUID)](pkstrokepath-swift.struct/init(controlpoints:creationdate:id:).md)
  Creates a stroke path with the specified cubic B-spline control points and a unique identifier.
- [PKStrokePath.ConvertedBezierPoint](pkstrokepath-swift.struct/convertedbezierpoint.md)
  Information about a B-spline control point converted from a Bézier path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/init(bezierpath:creationdate:pointprovider:))*