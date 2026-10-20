# performKeyEquivalent(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Implemented by subclasses to respond to key equivalents (also known as keyboard shortcuts).

**Availability**:
- macOS

## Declaration

```swift
func performKeyEquivalent(with event: NSEvent) -> Bool
```

```objc
- (BOOL) performKeyEquivalent:(NSEvent *) event;
```

#### Return Value

[`true`](../../Swift/true.md) if `theEvent` is a key equivalent that the view handled, [`false`](../../Swift/false.md) if it is not a key equivalent that it should handle.

#### Discussion

If the view’s key equivalent is the same as the characters of the key-down event `theEvent`, as returned by [`charactersIgnoringModifiers`](../nsevent/charactersignoringmodifiers.md), the view should take the appropriate action and return [`true`](../../Swift/true.md). Otherwise, it should return the result of invoking `super`‘s implementation. The default implementation of this method simply passes the message down the view hierarchy (from superviews to subviews) and returns [`false`](../../Swift/false.md) if none of the view’s subviews responds [`true`](../../Swift/true.md).

## Parameters

- `event`: The key-down event object representing a key equivalent.

## See Also

### Handling Events in the View
- [func acceptsFirstMouse(for: NSEvent?) -> Bool](./acceptsfirstmouse%28for%29.md)
  Returns a Boolean value that indicates whether the view accepts the initial mouse-down event.
- [func hitTest(NSPoint) -> NSView?](./hittest%28_%29.md)
  Returns the farthest descendant of the view in the view hierarchy (including itself) that contains a specified point, or `nil` if that point lies completely outside the view.
- [func isMousePoint(NSPoint, in: NSRect) -> Bool](./ismousepoint%28_,in%29.md)
  Returns whether a region of the view contains a specified point, accounting for whether the view is flipped or not.
- [func rightMouseDown(with: NSEvent)](../nsresponder/rightmousedown%28with%29.md)
  Informs the receiver that the user has pressed the right mouse button.
- [var mouseDownCanMoveWindow: Bool](./mousedowncanmovewindow.md)
  A Boolean value indicating whether the view can pass mouse down events through to its superviews.
- [var inputContext: NSTextInputContext?](./inputcontext.md)
  The text input context object for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/performkeyequivalent(with:))*