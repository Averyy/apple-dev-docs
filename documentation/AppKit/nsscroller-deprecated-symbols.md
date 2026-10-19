# Deprecated symbols

**Framework**: AppKit

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [func drawArrow(NSScroller.Arrow, highlight: Bool)](nsscroller/drawarrow(_:highlight:).md)
  Draws the scroll button indicated by `arrow`, which is either `NSScrollerIncrementArrow` (the down or right scroll button) or `NSScrollerDecrementArrow` (up or left).
- [func highlight(Bool)](nsscroller/highlight(_:).md)
  Highlights or unhighlights the scroll button the user clicked.
- [func trackScrollButtons(with: NSEvent)](nsscroller/trackscrollbuttons(with:).md)
  Tracks the scroll buttons and sends action messages to the receiver’s target.
### Deprecated properties
- [var arrowsPosition: NSScroller.ArrowPosition](nsscroller/arrowsposition.md)
  The location of the scroll buttons within the scroller, as described in [`NSScroller.ArrowPosition`](nsscroller/arrowposition.md).
- [var controlTint: NSControlTint](nsscroller/controltint.md)
  The scroller’s control tint.
### Deprecated enumerations
- [NSScroller.Arrow](nsscroller/arrow.md)
  These constants describe the two scroller buttons and are used by [`drawArrow(_:highlight:)`](nsscroller/drawarrow(_:highlight:).md).
- [NSScroller.ArrowPosition](nsscroller/arrowposition.md)
  These constants specify where the scroller’s buttons appear and are used by the [`arrowsPosition`](nsscroller/arrowsposition.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller-deprecated-symbols)*