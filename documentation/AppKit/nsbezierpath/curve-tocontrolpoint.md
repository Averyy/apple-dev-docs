# curve(to:controlPoint:)

**Framework**: AppKit  
**Kind**: method

**Availability**:
- macOS 14.0+

## Declaration

```swift
func curve(to endPoint: NSPoint, controlPoint: NSPoint)
```

## See Also

- [func move(to: NSPoint)](nsbezierpath/move(to:).md)
  Moves the path’s current point to the specified location.
- [func line(to: NSPoint)](nsbezierpath/line(to:).md)
  Appends a straight line to the path.
- [func curve(to: NSPoint, controlPoint1: NSPoint, controlPoint2: NSPoint)](nsbezierpath/curve(to:controlpoint1:controlpoint2:).md)
  Adds a Bezier cubic curve to the path.
- [func close()](nsbezierpath/close.md)
  Closes the most recently added subpath.
- [func relativeMove(to: NSPoint)](nsbezierpath/relativemove(to:).md)
  Moves the path’s current point to a new point whose location is the specified distance from the current point.
- [func relativeLine(to: NSPoint)](nsbezierpath/relativeline(to:).md)
  Appends a straight line segment to the path starting at the current point and moving towards the specified point, relative to the current location.
- [func relativeCurve(to: NSPoint, controlPoint1: NSPoint, controlPoint2: NSPoint)](nsbezierpath/relativecurve(to:controlpoint1:controlpoint2:).md)
  Adds a Bezier cubic curve to the path from the current point to a new location, which is specified as a relative distance from the current point.
- [func relativeCurve(to: NSPoint, controlPoint: NSPoint)](nsbezierpath/relativecurve(to:controlpoint:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/curve(to:controlpoint:))*