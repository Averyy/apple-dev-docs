# hitTest(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the farthest descendant of the view in the view hierarchy (including itself) that contains a specified point, or `nil` if that point lies completely outside the view.

**Availability**:
- macOS

## Declaration

```swift
func hitTest(_ point: NSPoint) -> NSView?
```

```objc
- (NSView *) hitTest:(NSPoint) point;
```

## Mentions

- [Handling AppKit gestures](../handling-appkit-gestures.md)

## Return Value

A view object that is the farthest descendent of `aPoint`.

## Discussion

This method is used primarily by an [`NSWindow`](../nswindow.md) object to determine which view should receive a mouse-down event. You’d rarely need to invoke this method, but you might want to override it to have a view object hide mouse-down events from its subviews. This method ignores hidden views.

## Parameters

- `point`: A point that is in the coordinate system of the view’s superview, not of the view itself.

## See Also

### Related Documentation
- [func convert(NSPoint, to: NSView?) -> NSPoint](./convert%28_,to%29-6u9ir.md)
  Converts a point from the view’s coordinate system to that of a given view.
### Handling Events in the View
- [func acceptsFirstMouse(for: NSEvent?) -> Bool](./acceptsfirstmouse%28for%29.md)
  Returns a Boolean value that indicates whether the view accepts the initial mouse-down event.
- [func isMousePoint(NSPoint, in: NSRect) -> Bool](./ismousepoint%28_,in%29.md)
  Returns whether a region of the view contains a specified point, accounting for whether the view is flipped or not.
- [func performKeyEquivalent(with: NSEvent) -> Bool](./performkeyequivalent%28with%29.md)
  Implemented by subclasses to respond to key equivalents (also known as keyboard shortcuts).
- [func rightMouseDown(with: NSEvent)](../nsresponder/rightmousedown%28with%29.md)
  Informs the receiver that the user has pressed the right mouse button.
- [var mouseDownCanMoveWindow: Bool](./mousedowncanmovewindow.md)
  A Boolean value indicating whether the view can pass mouse down events through to its superviews.
- [var inputContext: NSTextInputContext?](./inputcontext.md)
  The text input context object for the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/hittest(_:))*