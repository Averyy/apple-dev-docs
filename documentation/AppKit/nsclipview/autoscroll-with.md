# autoscroll(with:)

**Framework**: AppKit  
**Kind**: method

Scrolls the clip view proportionally to `theEvent`’s distance outside of it.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func autoscroll(with event: NSEvent) -> Bool
```

#### Discussion

`theEvent`‘s location should be expressed in the window’s base coordinate system (which it normally is), not the receiving [`NSClipView`](nsclipview.md). Returns [`true`](https://developer.apple.com/documentation/Swift/true) if any scrolling is performed; otherwise returns [`false`](https://developer.apple.com/documentation/Swift/false).

Never invoke this method directly; instead, the [`NSScrollView`](nsscrollview.md)’s document view should repeatedly send itself [`autoscroll(with:)`](nsview/autoscroll(with:).md) messages when the pointer is dragged outside the [`NSScrollView`](nsscrollview.md)‘s frame during a modal event loop initiated by a mouse-down event. The [`NSView`](nsview.md) class implements [`autoscroll(with:)`](nsview/autoscroll(with:).md) to forward the message to the receiver’s superview; thus the message is ultimately forwarded to the [`NSClipView`](nsclipview.md).

## See Also

- [func scroll(to: NSPoint)](nsclipview/scroll(to:).md)
  Changes the origin of the clip view’s bounds rectangle to `newOrigin`.
- [func constrainScroll(NSPoint) -> NSPoint](nsclipview/constrainscroll(_:).md)
  Returns a scroll point adjusted from the proposed new origin, if necessary, to guarantee the view will lie within its document view.
- [func constrainBoundsRect(NSRect) -> NSRect](nsclipview/constrainboundsrect(_:).md)
  Constrains the bounds of the clip view while the user is magnifying and scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/autoscroll(with:))*