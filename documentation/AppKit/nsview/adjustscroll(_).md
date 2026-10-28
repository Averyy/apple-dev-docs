# adjustScroll(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Overridden by subclasses to modify a given rectangle, returning the altered rectangle.

**Availability**:
- macOS

## Declaration

```swift
func adjustScroll(_ newVisible: NSRect) -> NSRect
```

```objc
- (NSRect) adjustScroll:(NSRect) newVisible;
```

## Discussion

[`NSClipView`](../nsclipview.md) invokes this method to allow its document view to adjust its position during scrolling. For example, a custom view object that displays a table of data can adjust the origin of `newVisible` so rows or columns aren’t cut off by the edge of the enclosing [`NSClipView`](../nsclipview.md). The [`NSView`](../nsview.md) implementation simply returns `newVisible`.

[`NSClipView`](../nsclipview.md) only invokes this method during automatic or user controlled scrolling. Its [`scroll(to:)`](../nsclipview/scroll%28to%29.md) method doesn’t invoke this method, so you can still force a scroll to an arbitrary point.

## Parameters

- `newVisible`: A rectangle that defines a region of the view.

## See Also

### Scrolling the View
- [func prepareContent(in: NSRect)](./preparecontent%28in%29.md)
  Prepares the overdraw region for drawing.
- [var preparedContentRect: NSRect](./preparedcontentrect.md)
  The portion of the view that has been rendered and is available for responsive scrolling.
- [func scroll(NSPoint)](./scroll%28_%29.md)
  Scrolls the view’s closest ancestor [`NSClipView`](../nsclipview.md) object so a point in the view lies at the origin of the clip view’s bounds rectangle.
- [func scrollToVisible(NSRect) -> Bool](./scrolltovisible%28_%29.md)
  Scrolls the view’s closest ancestor [`NSClipView`](../nsclipview.md) object the minimum distance needed so a specified region of the view becomes visible in the clip view.
- [func autoscroll(with: NSEvent) -> Bool](./autoscroll%28with%29.md)
  Scrolls the view’s closest ancestor [`NSClipView`](../nsclipview.md) object proportionally to the distance of an event that occurs outside of it.
- [var enclosingScrollView: NSScrollView?](./enclosingscrollview.md)
  The nearest ancestor scroll view that contains the current view.
- [func scroll(NSClipView, to: NSPoint)](./scroll%28_,to%29.md)
  Notifies the superview of a clip view that the clip view needs to reset the origin of its bounds rectangle.
- [func reflectScrolledClipView(NSClipView)](./reflectscrolledclipview%28_%29.md)
  Notifies a clip view’s superview that either the clip view’s bounds rectangle or the document view’s frame rectangle has changed, and that any indicators of the scroll position need to be adjusted.
- [class var isCompatibleWithResponsiveScrolling: Bool](./iscompatiblewithresponsivescrolling.md)
  A Boolean value that indicates whether views support responsive scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/adjustscroll(_:))*