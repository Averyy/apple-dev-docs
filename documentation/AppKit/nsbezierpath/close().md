# close()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Closes the most recently added subpath.

**Availability**:
- macOS

## Declaration

```swift
func close()
```

```objc
- (void) closePath;
```

## Discussion

This method closes the current subpath by creating a line segment between the first and last points in the subpath. This method subsequently updates the current point to the end of the newly created line segment, which is also the first point in the now closed subpath.

## See Also

### Related Documentation
- [func fill()](./fill%28%29.md)
  Paints the region enclosed by the path.
### Constructing a Path
- [func move(to: NSPoint)](./move%28to%29.md)
  Moves the path’s current point to the specified location.
- [func line(to: NSPoint)](./line%28to%29.md)
  Appends a straight line to the path.
- [func curve(to: NSPoint, controlPoint1: NSPoint, controlPoint2: NSPoint)](./curve%28to,controlpoint1,controlpoint2%29.md)
  Adds a Bezier cubic curve to the path.
- [func curve(to: NSPoint, controlPoint: NSPoint)](./curve%28to,controlpoint%29.md)
- [func relativeMove(to: NSPoint)](./relativemove%28to%29.md)
  Moves the path’s current point to a new point whose location is the specified distance from the current point.
- [func relativeLine(to: NSPoint)](./relativeline%28to%29.md)
  Appends a straight line segment to the path starting at the current point and moving towards the specified point, relative to the current location.
- [func relativeCurve(to: NSPoint, controlPoint1: NSPoint, controlPoint2: NSPoint)](./relativecurve%28to,controlpoint1,controlpoint2%29.md)
  Adds a Bezier cubic curve to the path from the current point to a new location, which is specified as a relative distance from the current point.
- [func relativeCurve(to: NSPoint, controlPoint: NSPoint)](./relativecurve%28to,controlpoint%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/close())*