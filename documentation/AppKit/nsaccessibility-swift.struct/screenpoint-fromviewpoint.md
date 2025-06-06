# screenPoint(fromView:point:)

**Framework**: AppKit  
**Kind**: method

Returns the point in screen coordinates.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static func screenPoint(fromView parentView: NSView, point: NSPoint) -> NSPoint
```

#### Discussion

Given a point in the specified view’s coordinates, it returns the same point in the screen’s coordinates.

## See Also

- [static func screenRect(fromView: NSView, rect: NSRect) -> NSRect](nsaccessibility-swift.struct/screenrect(fromview:rect:).md)
  Returns the frame in screen coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/screenpoint(fromview:point:))*