# isCompatibleWithResponsiveScrolling

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether views support responsive scrolling.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
class var isCompatibleWithResponsiveScrolling: Bool { get }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the view class supports responsive scrolling. AppKit enables responsive scrolling when the views involved in scrolling—the [`NSScrollView`](nsscrollview.md), [`NSClipView`](nsclipview.md), and embedded document view—all have this property set to [`true`](https://developer.apple.com/documentation/Swift/true). If you want to opt out of responsive scrolling, override this property and set it to [`false`](https://developer.apple.com/documentation/Swift/false).

[`NSScrollView`](nsscrollview.md), [`NSClipView`](nsclipview.md), and other view subclasses override this property and perform additional checks.

## See Also

- [func prepareContent(in: NSRect)](nsview/preparecontent(in:).md)
  Prepares the overdraw region for drawing.
- [var preparedContentRect: NSRect](nsview/preparedcontentrect.md)
  The portion of the view that has been rendered and is available for responsive scrolling.
- [func scroll(NSPoint)](nsview/scroll(_:).md)
  Scrolls the view’s closest ancestor [`NSClipView`](nsclipview.md) object so a point in the view lies at the origin of the clip view’s bounds rectangle.
- [func scrollToVisible(NSRect) -> Bool](nsview/scrolltovisible(_:).md)
  Scrolls the view’s closest ancestor [`NSClipView`](nsclipview.md) object the minimum distance needed so a specified region of the view becomes visible in the clip view.
- [func autoscroll(with: NSEvent) -> Bool](nsview/autoscroll(with:).md)
  Scrolls the view’s closest ancestor [`NSClipView`](nsclipview.md) object proportionally to the distance of an event that occurs outside of it.
- [func adjustScroll(NSRect) -> NSRect](nsview/adjustscroll(_:).md)
  Overridden by subclasses to modify a given rectangle, returning the altered rectangle.
- [var enclosingScrollView: NSScrollView?](nsview/enclosingscrollview.md)
  The nearest ancestor scroll view that contains the current view.
- [func scroll(NSClipView, to: NSPoint)](nsview/scroll(_:to:).md)
  Notifies the superview of a clip view that the clip view needs to reset the origin of its bounds rectangle.
- [func reflectScrolledClipView(NSClipView)](nsview/reflectscrolledclipview(_:).md)
  Notifies a clip view’s superview that either the clip view’s bounds rectangle or the document view’s frame rectangle has changed, and that any indicators of the scroll position need to be adjusted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/iscompatiblewithresponsivescrolling)*