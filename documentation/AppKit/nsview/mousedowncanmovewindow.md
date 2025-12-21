# mouseDownCanMoveWindow

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view can pass mouse down events through to its superviews.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var mouseDownCanMoveWindow: Bool { get }
```

#### Discussion

This property lets you determine the region by which a window can be moved. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false) if the view is opaque; otherwise, it is set to [`true`](https://developer.apple.com/documentation/Swift/true). Subclasses can override this property to return different values based on the event.

## See Also

- [func acceptsFirstMouse(for: NSEvent?) -> Bool](nsview/acceptsfirstmouse(for:).md)
  Returns a Boolean value that indicates whether the view accepts the initial mouse-down event.
- [func hitTest(NSPoint) -> NSView?](nsview/hittest(_:).md)
  Returns the farthest descendant of the view in the view hierarchy (including itself) that contains a specified point, or `nil` if that point lies completely outside the view.
- [func isMousePoint(NSPoint, in: NSRect) -> Bool](nsview/ismousepoint(_:in:).md)
  Returns whether a region of the view contains a specified point, accounting for whether the view is flipped or not.
- [func performKeyEquivalent(with: NSEvent) -> Bool](nsview/performkeyequivalent(with:).md)
  Implemented by subclasses to respond to key equivalents (also known as keyboard shortcuts).
- [func rightMouseDown(with: NSEvent)](nsresponder/rightmousedown(with:).md)
  Informs the receiver that the user has pressed the right mouse button.
- [var inputContext: NSTextInputContext?](nsview/inputcontext.md)
  The text input context object for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/mousedowncanmovewindow)*