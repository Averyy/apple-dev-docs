# drawArrow(_:highlight:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the scroll button indicated by `arrow`, which is either `NSScrollerIncrementArrow` (the down or right scroll button) or `NSScrollerDecrementArrow` (up or left).

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Scrollers don't have arrows as of 10.7

## Declaration

```swift
func drawArrow(_ whichArrow: NSScroller.Arrow, highlight flag: Bool)
```

```objc
- (void) drawArrow:(NSScrollerArrow) whichArrow highlight:(BOOL) flag;
```

## Discussion

If `flag` is [`true`](../../Swift/true.md), the button is drawn highlighted; otherwise it’s drawn normally. You should never need to invoke this method directly, but may wish to override it to customize the appearance of scroll buttons.

> **Note**:  The [`drawArrow(_:highlight:)`](./drawarrow%28_,highlight%29.md) method is not invoked in macOS 10.7 and later.

## See Also

### Related Documentation
- [func rect(for: NSScroller.Part) -> NSRect](./rect%28for%29.md)
  Returns the rectangle occupied by `aPart`, which for this method is interpreted literally rather than as an indicator of scrolling direction.
### Deprecated methods
- [func highlight(Bool)](./highlight%28_%29.md)
  Highlights or unhighlights the scroll button the user clicked.
- [func trackScrollButtons(with: NSEvent)](./trackscrollbuttons%28with%29.md)
  Tracks the scroll buttons and sends action messages to the receiver’s target.
- [+ scrollerWidth](./scrollerwidth.md)
  Returns the width for scrollers of the receiving class, assuming a control size [`NSRegularControlSize`](../nsregularcontrolsize.md), and a scroller style of [`NSScrollerStyleLegacy`](./style/legacy.md).
- [+ scrollerWidthForControlSize:](./scrollerwidthforcontrolsize_.md)
  Returns the width of the scroller based on `controlSize` and assuming a scroller style of [`NSScrollerStyleLegacy`](./style/legacy.md).
- [- setFloatValue:knobProportion:](./setfloatvalue_knobproportion_.md)
  Sets the position of the knob to `aFloat`, which is a value from 0.0 (indicating the top or left end) to 1.0 (the bottom or right end).
- [- drawParts](./drawparts.md)
  Caches images for the scroll buttons and knob.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/drawarrow(_:highlight:))*