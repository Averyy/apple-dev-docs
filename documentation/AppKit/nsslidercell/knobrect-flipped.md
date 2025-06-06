# knobRect(flipped:)

**Framework**: AppKit  
**Kind**: method

Returns the rectangle in which the slider knob is drawn.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func knobRect(flipped: Bool) -> NSRect
```

#### Return Value

The rectangle in which the knob is drawn, specified in the coordinate system of the `NSSlider` or `NSMatrix` with which the receiver is associated.

#### Discussion

The knob rectangle depends on where in the slider the knob belongs—that is, it depends on the receiver’s minimum and maximum values and on the value the position of the knob will represent.

## Parameters

- `flipped`:   if the coordinate system of the associated   or   is flipped; otherwise  . You can determine whether this is the case by sending the   message   message to the   or  .

## See Also

- [func barRect(flipped: Bool) -> NSRect](nsslidercell/barrect(flipped:).md)
  Returns the rectangle in which the bar is drawn.
- [func drawTickMarks()](nsslidercell/drawtickmarks.md)
  Draws the slider’s tick marks.
- [func drawBar(inside: NSRect, flipped: Bool)](nsslidercell/drawbar(inside:flipped:).md)
  Draws the slider’s bar—but not its bezel or knob—inside the specified rectangle.
- [func drawKnob()](nsslidercell/drawknob.md)
  Calculates the rectangle in which the knob should be drawn, then calls [`drawKnob(_:)`](nsslidercell/drawknob(_:).md) to actually draw the knob.
- [func drawKnob(NSRect)](nsslidercell/drawknob(_:).md)
  Draws the slider knob in the given rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/knobrect(flipped:))*