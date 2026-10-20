# drawKnobSlot(in:highlight:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the portion of the scroller’s track, possibly including the line increment and decrement arrow buttons, that falls in the given rectangle.

**Availability**:
- macOS

## Declaration

```swift
func drawKnobSlot(in slotRect: NSRect, highlight flag: Bool)
```

```objc
- (void) drawKnobSlotInRect:(NSRect) slotRect highlight:(BOOL) flag;
```

#### Discussion

Only one arrow button will be shown highlighted at a time, so you can expect this method to sometimes be invoked with a `slotRect` that encompasses only one arrow.

## Parameters

- `slotRect`: The rectangle in which to draw the knob slot.
- `flag`: If `flag` is [`true`](../../Swift/true.md), any scroll arrow button that falls within `slotRect` is drawn highlighted; otherwise it’s drawn normally.

## See Also

### Drawing Scroller Parts
- [func drawKnob()](./drawknob%28%29.md)
  Draws the knob.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/drawknobslot(in:highlight:))*