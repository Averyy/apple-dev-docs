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
convenience init(bezierPath: CGPath, creationDate: Date, pointProvider: (PKConvertedBezierPointReference) -> PKStrokePoint)
```

#### Discussion

The count of control points of the generated spline is not guaranteed to be a specific value except when the provided path is the output of `bezierRepresentation->CGPathRef`, where it will match the original curve.

The output B-Spline will have continuous curvature and 0 curvature at the endpoints. In cases where the B-Spline cannot fully recreate the Bézier path, it will be an approximation. For example, if the given Bézier path includes `line to` elements, these will produce straight line segments in the resulting B-Spline, but if a `line to` element is adjacent to a `curve to` element, the resulting curve may not match the original.

> ⚠️ **Warning**: For a Bézier path with multiple subpaths, only the first will be converted.

## Parameters

- `bezierPath`: The Bézier path to convert to a cubic uniform B-Spline.
- `creationDate`: The start time of this path.
- `pointProvider`: Block to initialize the `PKStrokePoint`s of the path. A single `PKConvertedBezierPoint` instance is shared across all converted points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepathreference/init(bezierpath:creationdate:pointprovider:))*