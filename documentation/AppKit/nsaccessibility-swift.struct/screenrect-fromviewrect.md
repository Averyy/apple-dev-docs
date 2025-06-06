# screenRect(fromView:rect:)

**Framework**: AppKit  
**Kind**: method

Returns the frame in screen coordinates.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static func screenRect(fromView parentView: NSView, rect frame: NSRect) -> NSRect
```

#### Discussion

Given a frame in the specified view’s coordinates, it returns the same frame in the screen’s coordinates.

## See Also

- [static func screenPoint(fromView: NSView, point: NSPoint) -> NSPoint](nsaccessibility-swift.struct/screenpoint(fromview:point:).md)
  Returns the point in screen coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/screenrect(fromview:rect:))*