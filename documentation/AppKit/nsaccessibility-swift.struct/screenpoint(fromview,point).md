# screenPoint(fromView:point:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the point in screen coordinates.

**Availability**:
- macOS 10.10+

## Declaration

```swift
static func screenPoint(fromView parentView: NSView, point: NSPoint) -> NSPoint
```

```c
extern NSPoint NSAccessibilityPointInView(NSView *parentView, NSPoint point);
```

#### Discussion

Given a point in the specified view’s coordinates, it returns the same point in the screen’s coordinates.

## See Also

### Getting Screen Coordinates
- [static func screenRect(fromView: NSView, rect: NSRect) -> NSRect](./screenrect%28fromview,rect%29.md)
  Returns the frame in screen coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/screenpoint(fromview:point:))*