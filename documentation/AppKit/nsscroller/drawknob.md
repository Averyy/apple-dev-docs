# drawKnob()

**Framework**: AppKit  
**Kind**: method

Draws the knob.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawKnob()
```

#### Discussion

You should never need to invoke this method directly, but may wish to override it to customize the appearance of the knob.

## See Also

- [func rect(for: NSScroller.Part) -> NSRect](nsscroller/rect(for:).md)
  Returns the rectangle occupied by `aPart`, which for this method is interpreted literally rather than as an indicator of scrolling direction.
- [func drawArrow(NSScroller.Arrow, highlight: Bool)](nsscroller/drawarrow(_:highlight:).md)
  Draws the scroll button indicated by `arrow`, which is either `NSScrollerIncrementArrow` (the down or right scroll button) or `NSScrollerDecrementArrow` (up or left).
- [func drawKnobSlot(in: NSRect, highlight: Bool)](nsscroller/drawknobslot(in:highlight:).md)
  Draws the portion of the scroller’s track, possibly including the line increment and decrement arrow buttons, that falls in the given rectangle.
- [func highlight(Bool)](nsscroller/highlight(_:).md)
  Highlights or unhighlights the scroll button the user clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/drawknob())*