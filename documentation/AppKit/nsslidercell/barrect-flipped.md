# barRect(flipped:)

**Framework**: AppKit  
**Kind**: method

Returns the rectangle in which the bar is drawn.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
func barRect(flipped: Bool) -> NSRect
```

#### Return Value

The rectangle in which the bar is drawn, specified in the coordinate system of the `NSSlider` or `NSMatrix` with which the receiver is associated. The bar doesn’t include the slider’s bezel or knob.

#### Discussion

You can override this method if custom bar artwork requires specific dimensions.

## Parameters

- `flipped`:   if the coordinate system of the associated   or   is flipped; otherwise  . You can determine whether this is the case by sending the   message   message to the   or  .

## See Also

- [func drawTickMarks()](nsslidercell/drawtickmarks.md)
  Draws the slider’s tick marks.
- [func knobRect(flipped: Bool) -> NSRect](nsslidercell/knobrect(flipped:).md)
  Returns the rectangle in which the slider knob is drawn.
- [func drawBar(inside: NSRect, flipped: Bool)](nsslidercell/drawbar(inside:flipped:).md)
  Draws the slider’s bar—but not its bezel or knob—inside the specified rectangle.
- [func drawKnob()](nsslidercell/drawknob.md)
  Calculates the rectangle in which the knob should be drawn, then calls [`drawKnob(_:)`](nsslidercell/drawknob(_:).md) to actually draw the knob.
- [func drawKnob(NSRect)](nsslidercell/drawknob(_:).md)
  Draws the slider knob in the given rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/barrect(flipped:))*