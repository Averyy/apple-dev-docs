# acceptsFirstMouse(for:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the view accepts the initial mouse-down event.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func acceptsFirstMouse(for event: NSEvent?) -> Bool
```

#### Discussion

Subclasses can override this method to return [`true`](https://developer.apple.com/documentation/Swift/true) if the view should be sent a [`mouseDown(with:)`](nsresponder/mousedown(with:).md) message for an initial mouse-down event, [`false`](https://developer.apple.com/documentation/Swift/false) if not.

The view can either return a value unconditionally or use the location of `event` to determine whether or not it wants the event. The default implementation ignores `event` and returns [`false`](https://developer.apple.com/documentation/Swift/false).

Override this method in a subclass to allow instances to respond to click-through. This allows the user to click on a view in an inactive window, activating the view with one click, instead of clicking first to make the window active and then clicking the view. Most view objects refuse a click-through attempt, so the event simply activates the window. Many control objects, however, such as instances of [`NSButton`](nsbutton.md) and [`NSSlider`](nsslider.md), do accept them, so the user can immediately manipulate the control without having to release the mouse button.

## Parameters

- `event`: The initial mouse-down event, which must be over the view in its window.

## See Also

- [func hitTest(NSPoint) -> NSView?](nsview/hittest(_:).md)
  Returns the farthest descendant of the view in the view hierarchy (including itself) that contains a specified point, or `nil` if that point lies completely outside the view.
- [func isMousePoint(NSPoint, in: NSRect) -> Bool](nsview/ismousepoint(_:in:).md)
  Returns whether a region of the view contains a specified point, accounting for whether the view is flipped or not.
- [func performKeyEquivalent(with: NSEvent) -> Bool](nsview/performkeyequivalent(with:).md)
  Implemented by subclasses to respond to key equivalents (also known as keyboard shortcuts).
- [func rightMouseDown(with: NSEvent)](nsresponder/rightmousedown(with:).md)
  Informs the receiver that the user has pressed the right mouse button.
- [var mouseDownCanMoveWindow: Bool](nsview/mousedowncanmovewindow.md)
  A Boolean value indicating whether the view can pass mouse down events through to its superviews.
- [var inputContext: NSTextInputContext?](nsview/inputcontext.md)
  The text input context object for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/acceptsfirstmouse(for:))*