# init()

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Creates an empty stroke path.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init()
```

## See Also

### Creating a new stroke path
- [init<T>(controlPoints: T, creationDate: Date)](./init%28controlpoints,creationdate%29.md)
  Creates a stroke path with the cubic B-spline control points and a date that you specify.
- [init<T>(controlPoints: T, creationDate: Date, id: UUID)](./init%28controlpoints,creationdate,id%29.md)
  Creates a stroke path with the specified cubic B-spline control points and a unique identifier.
- [init(bezierPath: CGPath, creationDate: Date, pointProvider: (PKStrokePath.ConvertedBezierPoint) -> PKStrokePoint)](./init%28bezierpath,creationdate,pointprovider%29.md)
  Creates a stroke path recreating the specified Bézier path as a cubic uniform B-Spline.
- [PKStrokePath.ConvertedBezierPoint](./convertedbezierpoint.md)
  Information about a B-spline control point converted from a Bézier path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/init())*