# currentPoint

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The current point (the trailing point or ending point in the most recently added segment).

**Availability**:
- macOS

## Declaration

```swift
var currentPoint: NSPoint { get }
```

```objc
@property (readonly) NSPoint currentPoint;
```

## Discussion

This property contains the point from which the next drawn line or curve segment begins. If the path is empty, accessing this property raises [`genericException`](../../Foundation/nsexceptionname/genericexception.md).

## See Also

### Related Documentation
- [func curve(to: NSPoint, controlPoint1: NSPoint, controlPoint2: NSPoint)](./curve%28to,controlpoint1,controlpoint2%29.md)
  Adds a Bezier cubic curve to the path.
- [func close()](./close%28%29.md)
  Closes the most recently added subpath.
- [func move(to: NSPoint)](./move%28to%29.md)
  Moves the path’s current point to the specified location.
- [func line(to: NSPoint)](./line%28to%29.md)
  Appends a straight line to the path.
### Querying a Path
- [var bounds: NSRect](./bounds.md)
  The bounding box of the path.
- [var controlPointBounds: NSRect](./controlpointbounds.md)
  The bounding box of the path, including any control points.
- [var isEmpty: Bool](./isempty.md)
  A Boolean value that indicates whether the path is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/currentpoint)*