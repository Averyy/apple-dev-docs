# scrollerStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The scroller style used by the scroll view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var scrollerStyle: NSScroller.Style { get set }
```

```objc
@property NSScrollerStyle scrollerStyle;
```

## Discussion

See [`NSScroller.Style`](../nsscroller/style.md) for possible values.

This setting is automatically set at runtime, based on the user’s preference setting and, if relevant, the set of connected pointing devices and their configured scroll capabilities, as determined by the [`NSScroller`](../nsscroller.md) method [`preferredScrollerStyle`](../nsscroller/preferredscrollerstyle.md).

Setting an scroll view’s scroller style sets the style of both the horizontal and vertical scrollers.  If the scroll view subsequently creates or is assigned a new horizontal or vertical scroller, they are assigned the same scroller style assigned to the scroll view.

## See Also

### Scroller style
- [var scrollerKnobStyle: NSScroller.KnobStyle](./scrollerknobstyle.md)
  The knob style of scroll views that use the overlay scroller style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrollview/scrollerstyle)*