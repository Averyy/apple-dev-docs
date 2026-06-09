# init()

**Framework**: PencilKit  
**Kind**: init

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

- [init<T>(controlPoints: T, creationDate: Date)](pkstrokepath-swift.struct/init(controlpoints:creationdate:).md)
  Creates a stroke path with the cubic B-spline control points and a date that you specify.
- [init<T>(controlPoints: T, creationDate: Date, id: UUID)](pkstrokepath-swift.struct/init(controlpoints:creationdate:id:).md)
  Creates a stroke path with the specified cubic B-spline control points and a unique identifier.
- [init(bezierPath: CGPath, creationDate: Date, pointProvider: (PKStrokePath.ConvertedBezierPoint) -> PKStrokePoint)](pkstrokepath-swift.struct/init(bezierpath:creationdate:pointprovider:).md)
  Creates a stroke path recreating the specified Bézier path as a cubic uniform B-Spline.
- [PKStrokePath.ConvertedBezierPoint](pkstrokepath-swift.struct/convertedbezierpoint.md)
  Information about a B-spline control point converted from a Bézier path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepath-swift.struct/init())*