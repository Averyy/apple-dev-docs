# enclosingScrollView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The nearest ancestor scroll view that contains the current view.

**Availability**:
- macOS

## Declaration

```swift
var enclosingScrollView: NSScrollView? { get }
```

```objc
@property (strong, readonly, nullable) NSScrollView * enclosingScrollView;
```

## Discussion

If the current view is not embedded inside a scroll view, the value of this property is `nil`. This property does not contain the current view if the current view is itself a scroll view. It always contains an ancestor scroll view.

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
- [func adjustScroll(NSRect) -> NSRect](./adjustscroll%28_%29.md)
  Overridden by subclasses to modify a given rectangle, returning the altered rectangle.
- [func scroll(NSClipView, to: NSPoint)](./scroll%28_,to%29.md)
  Notifies the superview of a clip view that the clip view needs to reset the origin of its bounds rectangle.
- [func reflectScrolledClipView(NSClipView)](./reflectscrolledclipview%28_%29.md)
  Notifies a clip view’s superview that either the clip view’s bounds rectangle or the document view’s frame rectangle has changed, and that any indicators of the scroll position need to be adjusted.
- [class var isCompatibleWithResponsiveScrolling: Bool](./iscompatiblewithresponsivescrolling.md)
  A Boolean value that indicates whether views support responsive scrolling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/enclosingscrollview)*