# move(to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves the path’s current point to the specified location.

**Availability**:
- macOS

## Declaration

```swift
func move(to point: NSPoint)
```

```objc
- (void) moveToPoint:(NSPoint) point;
```

## Discussion

This method implicitly closes the current subpath (if any) and sets the current point to the value in `aPoint`. When closing the previous subpath, this method does not cause a line to be created from the first and last points in the subpath.

For many path operations, you must invoke this method before issuing any commands that cause a line or curve segment to be drawn.

## Parameters

- `point`: A point in the current coordinate system.

## See Also

### Constructing a Path
- [func line(to: NSPoint)](./line%28to%29.md)
  Appends a straight line to the path.
- [func curve(to: NSPoint, controlPoint1: NSPoint, controlPoint2: NSPoint)](./curve%28to,controlpoint1,controlpoint2%29.md)
  Adds a Bezier cubic curve to the path.
- [func curve(to: NSPoint, controlPoint: NSPoint)](./curve%28to,controlpoint%29.md)
- [func close()](./close%28%29.md)
  Closes the most recently added subpath.
- [func relativeMove(to: NSPoint)](./relativemove%28to%29.md)
  Moves the path’s current point to a new point whose location is the specified distance from the current point.
- [func relativeLine(to: NSPoint)](./relativeline%28to%29.md)
  Appends a straight line segment to the path starting at the current point and moving towards the specified point, relative to the current location.
- [func relativeCurve(to: NSPoint, controlPoint1: NSPoint, controlPoint2: NSPoint)](./relativecurve%28to,controlpoint1,controlpoint2%29.md)
  Adds a Bezier cubic curve to the path from the current point to a new location, which is specified as a relative distance from the current point.
- [func relativeCurve(to: NSPoint, controlPoint: NSPoint)](./relativecurve%28to,controlpoint%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/move(to:))*