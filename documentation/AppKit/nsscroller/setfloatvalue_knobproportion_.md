# setFloatValue:knobProportion:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the position of the knob to `aFloat`, which is a value from 0.0 (indicating the top or left end) to 1.0 (the bottom or right end).

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Use the [`knobProportion`](./knobproportion.md) property and the [`doubleValue`](../nscontrol/doublevalue.md) method instead.

## Declaration

```objc
- (void) setFloatValue:(float) value knobProportion:(CGFloat) proportion;
```

#### Discussion

Also sets the proportion of the knob slot filled by the knob to `knobProp`, also a value from 0.0 (minimal size) to 1.0 (fills the slot).

## See Also

### Related Documentation
- [var knobProportion: CGFloat](./knobproportion.md)
  The proportion of the knob slot that the knob should fill.
- [var floatValue: Float](../nscontrol/floatvalue.md)
  The value of the receiver’s cell as a single-precision floating-point number.
### Deprecated methods
- [+ scrollerWidth](./scrollerwidth.md)
  Returns the width for scrollers of the receiving class, assuming a control size [`NSRegularControlSize`](../nsregularcontrolsize.md), and a scroller style of [`NSScroller.Style.legacy`](./style/legacy.md).
- [+ scrollerWidthForControlSize:](./scrollerwidthforcontrolsize_.md)
  Returns the width of the scroller based on `controlSize` and assuming a scroller style of [`NSScroller.Style.legacy`](./style/legacy.md).
- [func drawArrow(NSScroller.Arrow, highlight: Bool)](./drawarrow%28_,highlight%29.md)
  Draws the scroll button indicated by `arrow`, which is either `NSScrollerIncrementArrow` (the down or right scroll button) or `NSScrollerDecrementArrow` (up or left).
- [- drawParts](./drawparts.md)
  Caches images for the scroll buttons and knob.
- [func highlight(Bool)](./highlight%28_%29.md)
  Highlights or unhighlights the scroll button the user clicked.
- [func trackScrollButtons(with: NSEvent)](./trackscrollbuttons%28with%29.md)
  Tracks the scroll buttons and sends action messages to the receiver’s target.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/setfloatvalue:knobproportion:)*