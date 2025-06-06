# highlight(_:)

**Framework**: AppKit  
**Kind**: method

Highlights or unhighlights the scroll button the user clicked.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func highlight(_ flag: Bool)
```

#### Discussion

The receiver invokes this method while tracking the mouse; you should not invoke it directly. If `flag` is [`true`](https://developer.apple.com/documentation/swift/true), the appropriate part is drawn highlighted; otherwise it’s drawn normally.

##### Special Considerations

This method has no effect in macOS 10.7 and later.

## See Also

- [func rect(for: NSScroller.Part) -> NSRect](nsscroller/rect(for:).md)
  Returns the rectangle occupied by `aPart`, which for this method is interpreted literally rather than as an indicator of scrolling direction.
- [func drawArrow(NSScroller.Arrow, highlight: Bool)](nsscroller/drawarrow(_:highlight:).md)
  Draws the scroll button indicated by `arrow`, which is either `NSScrollerIncrementArrow` (the down or right scroll button) or `NSScrollerDecrementArrow` (up or left).
- [func drawKnobSlot(in: NSRect, highlight: Bool)](nsscroller/drawknobslot(in:highlight:).md)
  Draws the portion of the scroller’s track, possibly including the line increment and decrement arrow buttons, that falls in the given rectangle.
- [func drawKnob()](nsscroller/drawknob.md)
  Draws the knob.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/highlight(_:))*