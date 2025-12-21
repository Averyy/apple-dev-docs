# autoscroll(with:)

**Framework**: AppKit  
**Kind**: method

Scrolls the view’s closest ancestor [`NSClipView`](nsclipview.md) object proportionally to the distance of an event that occurs outside of it.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func autoscroll(with event: NSEvent) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if any scrolling is performed; otherwise returns [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

View objects that track mouse-dragged events can use this method to scroll automatically when the cursor is dragged outside of the [`NSClipView`](nsclipview.md) object. Repeated invocations of this method (with an appropriate delay) result in continual scrolling, even when the mouse doesn’t move.

## Parameters

- `event`: An event object whose location should be expressed in the window’s base coordinate system (which it normally is), not the receiving view’s.

## See Also

- [func isDescendant(of: NSView) -> Bool](nsview/isdescendant(of:).md)
  Returns a Boolean value that indicates whether the view is a subview of the specified view.
- [func autoscroll(with: NSEvent) -> Bool](nsclipview/autoscroll(with:).md)
  Scrolls the clip view proportionally to `theEvent`’s distance outside of it.
- [func prepareContent(in: NSRect)](nsview/preparecontent(in:).md)
  Prepares the overdraw region for drawing.
- [var preparedContentRect: NSRect](nsview/preparedcontentrect.md)
  The portion of the view that has been rendered and is available for responsive scrolling.
- [func scroll(NSPoint)](nsview/scroll(_:).md)
  Scrolls the view’s closest ancestor [`NSClipView`](nsclipview.md) object so a point in the view lies at the origin of the clip view’s bounds rectangle.
- [func scrollToVisible(NSRect) -> Bool](nsview/scrolltovisible(_:).md)
  Scrolls the view’s closest ancestor [`NSClipView`](nsclipview.md) object the minimum distance needed so a specified region of the view becomes visible in the clip view.
- [func adjustScroll(NSRect) -> NSRect](nsview/adjustscroll(_:).md)
  Overridden by subclasses to modify a given rectangle, returning the altered rectangle.
- [var enclosingScrollView: NSScrollView?](nsview/enclosingscrollview.md)
  The nearest ancestor scroll view that contains the current view.
- [func scroll(NSClipView, to: NSPoint)](nsview/scroll(_:to:).md)
  Notifies the superview of a clip view that the clip view needs to reset the origin of its bounds rectangle.
- [func reflectScrolledClipView(NSClipView)](nsview/reflectscrolledclipview(_:).md)
  Notifies a clip view’s superview that either the clip view’s bounds rectangle or the document view’s frame rectangle has changed, and that any indicators of the scroll position need to be adjusted.
- [class var isCompatibleWithResponsiveScrolling: Bool](nsview/iscompatiblewithresponsivescrolling.md)
  A Boolean value that indicates whether views support responsive scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/autoscroll(with:))*