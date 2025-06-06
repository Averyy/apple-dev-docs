# drawKnob(_:)

**Framework**: AppKit  
**Kind**: method

Draws the slider knob in the given rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func drawKnob(_ knobRect: NSRect)
```

#### Discussion

Before this message is sent, a [`lockFocus()`](nsview/lockfocus().md) message must be sent to the cell’s control view.

You should not call this method explicitly. It’s included so you can override it in a subclass.

## Parameters

- `knobRect`: The rectangle in which to draw the slider knob.

## See Also

- [func barRect(flipped: Bool) -> NSRect](nsslidercell/barrect(flipped:).md)
  Returns the rectangle in which the bar is drawn.
- [func drawTickMarks()](nsslidercell/drawtickmarks.md)
  Draws the slider’s tick marks.
- [func knobRect(flipped: Bool) -> NSRect](nsslidercell/knobrect(flipped:).md)
  Returns the rectangle in which the slider knob is drawn.
- [func drawBar(inside: NSRect, flipped: Bool)](nsslidercell/drawbar(inside:flipped:).md)
  Draws the slider’s bar—but not its bezel or knob—inside the specified rectangle.
- [func drawKnob()](nsslidercell/drawknob.md)
  Calculates the rectangle in which the knob should be drawn, then calls [`drawKnob(_:)`](nsslidercell/drawknob(_:).md) to actually draw the knob.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/drawknob(_:))*