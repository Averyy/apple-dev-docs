# autoscroll(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Scrolls the clip view proportionally to `theEvent`’s distance outside of it.

**Availability**:
- macOS

## Declaration

```swift
func autoscroll(with event: NSEvent) -> Bool
```

```objc
- (BOOL) autoscroll:(NSEvent *) event;
```

## Discussion

`theEvent`‘s location should be expressed in the window’s base coordinate system (which it normally is), not the receiving [`NSClipView`](../nsclipview.md). Returns [`true`](../../Swift/true.md) if any scrolling is performed; otherwise returns [`false`](../../Swift/false.md).

Never invoke this method directly; instead, the [`NSScrollView`](../nsscrollview.md)’s document view should repeatedly send itself [`autoscroll(with:)`](../nsview/autoscroll%28with%29.md) messages when the pointer is dragged outside the [`NSScrollView`](../nsscrollview.md)‘s frame during a modal event loop initiated by a mouse-down event. The [`NSView`](../nsview.md) class implements [`autoscroll(with:)`](../nsview/autoscroll%28with%29.md) to forward the message to the receiver’s superview; thus the message is ultimately forwarded to the [`NSClipView`](../nsclipview.md).

## See Also

### Scrolling
- [func scroll(to: NSPoint)](./scroll%28to%29.md)
  Changes the origin of the clip view’s bounds rectangle to `newOrigin`.
- [func constrainBoundsRect(NSRect) -> NSRect](./constrainboundsrect%28_%29.md)
  Constrains the bounds of the clip view while the user is magnifying and scrolling.
- [func constrainScroll(NSPoint) -> NSPoint](./constrainscroll%28_%29.md)
  Returns a scroll point adjusted from the proposed new origin, if necessary, to guarantee the view will lie within its document view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclipview/autoscroll(with:))*