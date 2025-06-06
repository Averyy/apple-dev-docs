# GCPoint2

**Framework**: Game Controller  
**Kind**: struct

A structure that represents a normalized point in a two-dimensional coordinate system.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.3+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
struct GCPoint2
```

## Topics

### Creating a point
- [init()](gcpoint2/init.md)
  Creates a two dimensional point with coordinates `(0, 0)`.
- [init(x: Float, y: Float)](gcpoint2/init(x:y:).md)
  Creates a two dimensional point with the given coordinates.
- [func GCPoint2Make(Float, Float) -> GCPoint2](gcpoint2make(_:_:).md)
  Returns a point with the specified coordinates in a two-dimensional coordinate system.
- [let GCPoint2Zero: GCPoint2](gcpoint2zero.md)
  The origin for a two dimensional point.
### Accessing coordinates
- [var x: Float](gcpoint2/x.md)
  The x-coordinate for the point.
- [var y: Float](gcpoint2/y.md)
  The y-coordinate for the point.
### Comparing and converting points
- [func GCPoint2Equal(GCPoint2, GCPoint2) -> Bool](gcpoint2equal(_:_:).md)
  Returns whether two points are equal.
- [func NSStringFromGCPoint2(GCPoint2) -> String](nsstringfromgcpoint2(_:).md)
  Returns a string representation of a point.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var value: GCPoint2](gcaxis2dinput/value.md)
  The axis input represented as a normalized point in a two-dimensional coordinate system.
- [var valueDidChangeHandler: ((any GCPhysicalInputElement, any GCAxis2DInput, GCPoint2) -> Void)?](gcaxis2dinput/valuedidchangehandler.md)
  The block that the axis element calls when its value changes.
- [var lastValueTimestamp: TimeInterval](gcaxis2dinput/lastvaluetimestamp.md)
  The time of the most recent value change.
- [var lastValueLatency: TimeInterval](gcaxis2dinput/lastvaluelatency.md)
  The time in seconds between the last value change and the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcpoint2)*