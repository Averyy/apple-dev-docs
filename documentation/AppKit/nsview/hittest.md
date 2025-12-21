# hitTest(_:)

**Framework**: AppKit  
**Kind**: method

Returns the farthest descendant of the view in the view hierarchy (including itself) that contains a specified point, or `nil` if that point lies completely outside the view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func hitTest(_ point: NSPoint) -> NSView?
```

#### Return Value

A view object that is the farthest descendent of `aPoint`.

#### Discussion

This method is used primarily by an [`NSWindow`](nswindow.md) object to determine which view should receive a mouse-down event. You’d rarely need to invoke this method, but you might want to override it to have a view object hide mouse-down events from its subviews. This method ignores hidden views.

## Parameters

- `point`: A point that is in the coordinate system of the view’s superview, not of the view itself.

## See Also

- [func convert(NSPoint, to: NSView?) -> NSPoint](nsview/convert(_:to:)-6u9ir.md)
  Converts a point from the view’s coordinate system to that of a given view.
- [func acceptsFirstMouse(for: NSEvent?) -> Bool](nsview/acceptsfirstmouse(for:).md)
  Returns a Boolean value that indicates whether the view accepts the initial mouse-down event.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/hittest(_:))*