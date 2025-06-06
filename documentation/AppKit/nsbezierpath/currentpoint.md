# currentPoint

**Framework**: AppKit  
**Kind**: property

The current point (the trailing point or ending point in the most recently added segment).

**Availability**:
- macOS ?+

## Declaration

```swift
var currentPoint: NSPoint { get }
```

#### Discussion

This property contains the point from which the next drawn line or curve segment begins. If the path is empty, accessing this property raises [`genericException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1412113-genericexception).

## See Also

- [func curve(to: NSPoint, controlPoint1: NSPoint, controlPoint2: NSPoint)](nsbezierpath/curve(to:controlpoint1:controlpoint2:).md)
  Adds a Bezier cubic curve to the path.
- [func close()](nsbezierpath/close.md)
  Closes the most recently added subpath.
- [func move(to: NSPoint)](nsbezierpath/move(to:).md)
  Moves the path’s current point to the specified location.
- [func line(to: NSPoint)](nsbezierpath/line(to:).md)
  Appends a straight line to the path.
- [var bounds: NSRect](nsbezierpath/bounds.md)
  The bounding box of the path.
- [var controlPointBounds: NSRect](nsbezierpath/controlpointbounds.md)
  The bounding box of the path, including any control points.
- [var isEmpty: Bool](nsbezierpath/isempty.md)
  A Boolean value that indicates whether the path is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/currentpoint)*