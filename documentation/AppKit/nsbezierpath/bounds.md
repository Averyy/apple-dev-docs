# bounds

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The bounding box of the path.

**Availability**:
- macOS

## Declaration

```swift
var bounds: NSRect { get }
```

```objc
@property (readonly) NSRect bounds;
```

## Discussion

This property contains the rectangle that encloses the path of the receiver. If the path contains curve segments, the bounding box encloses the curve but may not enclose the control points used to calculate the curve.

If the path is empty, accessing this property raises [`genericException`](../../Foundation/nsexceptionname/genericexception.md).

## See Also

### Querying a Path
- [var controlPointBounds: NSRect](./controlpointbounds.md)
  The bounding box of the path, including any control points.
- [var currentPoint: NSPoint](./currentpoint.md)
  The current point (the trailing point or ending point in the most recently added segment).
- [var isEmpty: Bool](./isempty.md)
  A Boolean value that indicates whether the path is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/bounds)*