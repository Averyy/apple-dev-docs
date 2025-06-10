# relativeCurve(to:controlPoint1:controlPoint2:)

**Framework**: AppKit  
**Kind**: method

Adds a Bezier cubic curve to the path from the current point to a new location, which is specified as a relative distance from the current point.

**Availability**:
- macOS ?+

## Declaration

```swift
func relativeCurve(to endPoint: NSPoint, controlPoint1: NSPoint, controlPoint2: NSPoint)
```

#### Discussion

You must set the path’s current point (using the [`move(to:)`](nsbezierpath/move(to:).md) method or through the creation of a preceding line or curve segment) before you invoke this method. If the path is empty, this method raises an [`genericException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/genericException) exception.

## Parameters

- `endPoint`: The destination point of the curve segment, interpreted as a relative offset from the current point.
- `controlPoint1`: The point that determines the shape of the curve near the current point, interpreted as a relative offset from the current point.
- `controlPoint2`: The point that determines the shape of the curve near the destination point, interpreted as a relative offset from the current point.

## See Also

- [func move(to: NSPoint)](nsbezierpath/move(to:).md)
  Moves the path’s current point to the specified location.
- [func line(to: NSPoint)](nsbezierpath/line(to:).md)
  Appends a straight line to the path.
- [func curve(to: NSPoint, controlPoint1: NSPoint, controlPoint2: NSPoint)](nsbezierpath/curve(to:controlpoint1:controlpoint2:).md)
  Adds a Bezier cubic curve to the path.
- [func curve(to: NSPoint, controlPoint: NSPoint)](nsbezierpath/curve(to:controlpoint:).md)
- [func close()](nsbezierpath/close.md)
  Closes the most recently added subpath.
- [func relativeMove(to: NSPoint)](nsbezierpath/relativemove(to:).md)
  Moves the path’s current point to a new point whose location is the specified distance from the current point.
- [func relativeLine(to: NSPoint)](nsbezierpath/relativeline(to:).md)
  Appends a straight line segment to the path starting at the current point and moving towards the specified point, relative to the current location.
- [func relativeCurve(to: NSPoint, controlPoint: NSPoint)](nsbezierpath/relativecurve(to:controlpoint:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/relativecurve(to:controlpoint1:controlpoint2:))*