# drawBar(inside:flipped:)

**Framework**: AppKit  
**Kind**: method

Draws the slider’s bar—but not its bezel or knob—inside the specified rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawBar(inside rect: NSRect, flipped: Bool)
```

#### Discussion

You should not call this method explicitly. It’s included so you can override it in a subclass.

## Parameters

- `rect`: The bounds of the slider’s bar, not of its interior rectangle.
- `flipped`: A Boolean value that indicates whether the cell’s control view—that is, the   or   associated with the  —has a flipped coordinate system.

## See Also

- [func barRect(flipped: Bool) -> NSRect](nsslidercell/barrect(flipped:).md)
  Returns the rectangle in which the bar is drawn.
- [func drawTickMarks()](nsslidercell/drawtickmarks.md)
  Draws the slider’s tick marks.
- [func knobRect(flipped: Bool) -> NSRect](nsslidercell/knobrect(flipped:).md)
  Returns the rectangle in which the slider knob is drawn.
- [func drawKnob()](nsslidercell/drawknob.md)
  Calculates the rectangle in which the knob should be drawn, then calls [`drawKnob(_:)`](nsslidercell/drawknob(_:).md) to actually draw the knob.
- [func drawKnob(NSRect)](nsslidercell/drawknob(_:).md)
  Draws the slider knob in the given rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/drawbar(inside:flipped:))*