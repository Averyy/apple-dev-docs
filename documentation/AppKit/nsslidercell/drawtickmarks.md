# drawTickMarks()

**Framework**: AppKit  
**Kind**: method

Draws the slider’s tick marks.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
func drawTickMarks()
```

#### Discussion

You should not call this method explicitly. It’s included so you can override it in a subclass and draw custom tick marks.

## See Also

- [func barRect(flipped: Bool) -> NSRect](nsslidercell/barrect(flipped:).md)
  Returns the rectangle in which the bar is drawn.
- [func knobRect(flipped: Bool) -> NSRect](nsslidercell/knobrect(flipped:).md)
  Returns the rectangle in which the slider knob is drawn.
- [func drawBar(inside: NSRect, flipped: Bool)](nsslidercell/drawbar(inside:flipped:).md)
  Draws the slider’s bar—but not its bezel or knob—inside the specified rectangle.
- [func drawKnob()](nsslidercell/drawknob.md)
  Calculates the rectangle in which the knob should be drawn, then calls [`drawKnob(_:)`](nsslidercell/drawknob(_:).md) to actually draw the knob.
- [func drawKnob(NSRect)](nsslidercell/drawknob(_:).md)
  Draws the slider knob in the given rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/drawtickmarks())*