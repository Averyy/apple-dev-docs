# drawKnobSlot(in:highlight:)

**Framework**: AppKit  
**Kind**: method

Draws the portion of the scroller’s track, possibly including the line increment and decrement arrow buttons, that falls in the given rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawKnobSlot(in slotRect: NSRect, highlight flag: Bool)
```

#### Discussion

Only one arrow button will be shown highlighted at a time, so you can expect this method to sometimes be invoked with a `slotRect` that encompasses only one arrow.

## Parameters

- `slotRect`: The rectangle in which to draw the knob slot.
- `flag`: If   is  , any scroll arrow button that falls within   is drawn highlighted; otherwise it’s drawn normally.

## See Also

- [func drawArrow(NSScroller.Arrow, highlight: Bool)](nsscroller/drawarrow(_:highlight:).md)
  Draws the scroll button indicated by `arrow`, which is either `NSScrollerIncrementArrow` (the down or right scroll button) or `NSScrollerDecrementArrow` (up or left).
- [func drawKnob()](nsscroller/drawknob.md)
  Draws the knob.
- [func highlight(Bool)](nsscroller/highlight(_:).md)
  Highlights or unhighlights the scroll button the user clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/drawknobslot(in:highlight:))*