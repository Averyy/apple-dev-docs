# move(to:)

**Framework**: AppKit  
**Kind**: method

Moves the path’s current point to the specified location.

**Availability**:
- macOS ?+

## Declaration

```swift
func move(to point: NSPoint)
```

#### Discussion

This method implicitly closes the current subpath (if any) and sets the current point to the value in `aPoint`. When closing the previous subpath, this method does not cause a line to be created from the first and last points in the subpath.

For many path operations, you must invoke this method before issuing any commands that cause a line or curve segment to be drawn.

## Parameters

- `point`: A point in the current coordinate system.

## See Also

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
- [func relativeCurve(to: NSPoint, controlPoint1: NSPoint, controlPoint2: NSPoint)](nsbezierpath/relativecurve(to:controlpoint1:controlpoint2:).md)
  Adds a Bezier cubic curve to the path from the current point to a new location, which is specified as a relative distance from the current point.
- [func relativeCurve(to: NSPoint, controlPoint: NSPoint)](nsbezierpath/relativecurve(to:controlpoint:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/move(to:))*