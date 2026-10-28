# scrollerWidth

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the width for scrollers of the receiving class, assuming a control size [`NSRegularControlSize`](../nsregularcontrolsize.md), and a scroller style of [`NSScroller.Style.legacy`](./style/legacy.md).

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use [`scrollerWidth(for:scrollerStyle:)`](./scrollerwidth%28for,scrollerstyle%29.md) instead.

## Declaration

```objc
+ (CGFloat) scrollerWidth;
```

## Discussion

`NSScrollView` uses this value to lay out its components. Subclasses that use a different width should override this method.

## See Also

### Deprecated methods
- [+ scrollerWidthForControlSize:](./scrollerwidthforcontrolsize_.md)
  Returns the width of the scroller based on `controlSize` and assuming a scroller style of [`NSScroller.Style.legacy`](./style/legacy.md).
- [- setFloatValue:knobProportion:](./setfloatvalue_knobproportion_.md)
  Sets the position of the knob to `aFloat`, which is a value from 0.0 (indicating the top or left end) to 1.0 (the bottom or right end).
- [func drawArrow(NSScroller.Arrow, highlight: Bool)](./drawarrow%28_,highlight%29.md)
  Draws the scroll button indicated by `arrow`, which is either `NSScrollerIncrementArrow` (the down or right scroll button) or `NSScrollerDecrementArrow` (up or left).
- [- drawParts](./drawparts.md)
  Caches images for the scroll buttons and knob.
- [func highlight(Bool)](./highlight%28_%29.md)
  Highlights or unhighlights the scroll button the user clicked.
- [func trackScrollButtons(with: NSEvent)](./trackscrollbuttons%28with%29.md)
  Tracks the scroll buttons and sends action messages to the receiver’s target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/scrollerwidth)*