# controlPointBounds

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The bounding box of the path, including any control points.

**Availability**:
- macOS

## Declaration

```swift
var controlPointBounds: NSRect { get }
```

```objc
@property (readonly) NSRect controlPointBounds;
```

## Discussion

This property contains the rectangle that encloses the receiver’s path. If the path contains curve segments, the bounding box encloses the control points of the curves as well as the curves themselves.

## See Also

### Querying a Path
- [var bounds: NSRect](./bounds.md)
  The bounding box of the path.
- [var currentPoint: NSPoint](./currentpoint.md)
  The current point (the trailing point or ending point in the most recently added segment).
- [var isEmpty: Bool](./isempty.md)
  A Boolean value that indicates whether the path is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/controlpointbounds)*