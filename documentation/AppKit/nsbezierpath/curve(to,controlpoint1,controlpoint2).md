# curve(to:controlPoint1:controlPoint2:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds a Bezier cubic curve to the path.

**Availability**:
- macOS

## Declaration

```swift
func curve(to endPoint: NSPoint, controlPoint1: NSPoint, controlPoint2: NSPoint)
```

```objc
- (void) curveToPoint:(NSPoint) endPoint controlPoint1:(NSPoint) controlPoint1 controlPoint2:(NSPoint) controlPoint2;
```

#### Discussion

You must set the path’s current point (using the [`move(to:)`](./move%28to%29.md) method or through the creation of a preceding line or curve segment) before you invoke this method. If the path is empty, this method raises an [`genericException`](../../Foundation/nsexceptionname/genericexception.md) exception.

## Parameters

- `endPoint`: The destination point of the curve segment, specified in the current coordinate system
- `controlPoint1`: The point that determines the shape of the curve near the current point.
- `controlPoint2`: The point that determines the shape of the curve near the destination point.

## See Also

### Constructing a Path
- [func move(to: NSPoint)](./move%28to%29.md)
  Moves the path’s current point to the specified location.
- [func line(to: NSPoint)](./line%28to%29.md)
  Appends a straight line to the path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/curve(to:controlpoint1:controlpoint2:))*