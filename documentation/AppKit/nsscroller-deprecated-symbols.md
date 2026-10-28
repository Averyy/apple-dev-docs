# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

## Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [func drawArrow(NSScroller.Arrow, highlight: Bool)](./nsscroller/drawarrow%28_,highlight%29.md)
  Draws the scroll button indicated by `arrow`, which is either `NSScrollerIncrementArrow` (the down or right scroll button) or `NSScrollerDecrementArrow` (up or left).
- [func highlight(Bool)](./nsscroller/highlight%28_%29.md)
  Highlights or unhighlights the scroll button the user clicked.
- [func trackScrollButtons(with: NSEvent)](./nsscroller/trackscrollbuttons%28with%29.md)
  Tracks the scroll buttons and sends action messages to the receiver’s target.
- [+ scrollerWidth](./nsscroller/scrollerwidth.md)
  Returns the width for scrollers of the receiving class, assuming a control size [`NSRegularControlSize`](./nsregularcontrolsize.md), and a scroller style of [`NSScrollerStyleLegacy`](./nsscroller/style/legacy.md).
- [+ scrollerWidthForControlSize:](./nsscroller/scrollerwidthforcontrolsize_.md)
  Returns the width of the scroller based on `controlSize` and assuming a scroller style of [`NSScrollerStyleLegacy`](./nsscroller/style/legacy.md).
- [- setFloatValue:knobProportion:](./nsscroller/setfloatvalue_knobproportion_.md)
  Sets the position of the knob to `aFloat`, which is a value from 0.0 (indicating the top or left end) to 1.0 (the bottom or right end).
- [- drawParts](./nsscroller/drawparts.md)
  Caches images for the scroll buttons and knob.
### Deprecated properties
- [var arrowsPosition: NSScroller.ArrowPosition](./nsscroller/arrowsposition.md)
  The location of the scroll buttons within the scroller, as described in [`NSScroller.ArrowPosition`](./nsscroller/arrowposition.md).
- [var controlTint: NSControlTint](./nsscroller/controltint.md)
  The scroller’s control tint.
### Deprecated enumerations
- [NSScroller.Arrow](./nsscroller/arrow.md)
  These constants describe the two scroller buttons and are used by [`drawArrow(_:highlight:)`](./nsscroller/drawarrow%28_,highlight%29.md).
- [NSScroller.ArrowPosition](./nsscroller/arrowposition.md)
  These constants specify where the scroller’s buttons appear and are used by the [`arrowsPosition`](./nsscroller/arrowsposition.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller-deprecated-symbols)*