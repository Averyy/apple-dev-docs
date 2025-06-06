# performKeyEquivalent(with:)

**Framework**: AppKit  
**Kind**: method

Implemented by subclasses to respond to key equivalents (also known as keyboard shortcuts).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func performKeyEquivalent(with event: NSEvent) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `theEvent` is a key equivalent that the view handled, [`false`](https://developer.apple.com/documentation/swift/false) if it is not a key equivalent that it should handle.

#### Discussion

If the view’s key equivalent is the same as the characters of the key-down event `theEvent`, as returned by [`charactersIgnoringModifiers`](nsevent/charactersignoringmodifiers.md), the view should take the appropriate action and return [`true`](https://developer.apple.com/documentation/swift/true). Otherwise, it should return the result of invoking `super`‘s implementation. The default implementation of this method simply passes the message down the view hierarchy (from superviews to subviews) and returns [`false`](https://developer.apple.com/documentation/swift/false) if none of the view’s subviews responds [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `event`: The key-down event object representing a key equivalent.

## See Also

- [func acceptsFirstMouse(for: NSEvent?) -> Bool](nsview/acceptsfirstmouse(for:).md)
  Overridden by subclasses to return [`true`](https://developer.apple.com/documentation/swift/true) if the view should be sent a [`mouseDown(with:)`](nsresponder/mousedown(with:).md) message for an initial mouse-down event, [`false`](https://developer.apple.com/documentation/swift/false) if not.
- [func hitTest(NSPoint) -> NSView?](nsview/hittest(_:).md)
  Returns the farthest descendant of the view in the view hierarchy (including itself) that contains a specified point, or `nil` if that point lies completely outside the view.
- [func isMousePoint(NSPoint, in: NSRect) -> Bool](nsview/ismousepoint(_:in:).md)
  Returns whether a region of the view contains a specified point, accounting for whether the view is flipped or not.
- [func rightMouseDown(with: NSEvent)](nsresponder/rightmousedown(with:).md)
  Informs the receiver that the user has pressed the right mouse button.
- [var mouseDownCanMoveWindow: Bool](nsview/mousedowncanmovewindow.md)
  A Boolean value indicating whether the view can pass mouse down events through to its superviews.
- [var inputContext: NSTextInputContext?](nsview/inputcontext.md)
  The text input context object for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/performkeyequivalent(with:))*