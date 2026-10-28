# relativeLine(to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Appends a straight line segment to the path starting at the current point and moving towards the specified point, relative to the current location.

**Availability**:
- macOS

## Declaration

```swift
func relativeLine(to point: NSPoint)
```

```objc
- (void) relativeLineToPoint:(NSPoint) point;
```

## Discussion

The destination point is relative to the current point. For example, if the current point is (1, 1) and `aPoint` contains the value (1, 2), a line segment is created between the points (1, 1) and (2, 3).

You must set the path’s current point (using the [`move(to:)`](./move%28to%29.md) method or through the creation of a preceding line or curve segment) before you invoke this method. If the path is empty, this method raises an [`genericException`](../../Foundation/nsexceptionname/genericexception.md) exception.

## Parameters

- `point`: A point whose coordinates are interpreted as a relative offset from the current point.

## See Also

### Constructing a Path
- [func move(to: NSPoint)](./move%28to%29.md)
  Moves the path’s current point to the specified location.
- [func line(to: NSPoint)](./line%28to%29.md)
  Appends a straight line to the path.
- [func curve(to: NSPoint, controlPoint1: NSPoint, controlPoint2: NSPoint)](./curve%28to,controlpoint1,controlpoint2%29.md)
  Adds a Bezier cubic curve to the path.
- [func curve(to: NSPoint, controlPoint: NSPoint)](./curve%28to,controlpoint%29.md)
- [func close()](./close%28%29.md)
  Closes the most recently added subpath.
- [func relativeMove(to: NSPoint)](./relativemove%28to%29.md)
  Moves the path’s current point to a new point whose location is the specified distance from the current point.
- [func relativeCurve(to: NSPoint, controlPoint1: NSPoint, controlPoint2: NSPoint)](./relativecurve%28to,controlpoint1,controlpoint2%29.md)
  Adds a Bezier cubic curve to the path from the current point to a new location, which is specified as a relative distance from the current point.
- [func relativeCurve(to: NSPoint, controlPoint: NSPoint)](./relativecurve%28to,controlpoint%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/relativeline(to:))*