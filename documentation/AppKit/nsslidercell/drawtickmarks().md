# drawTickMarks()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the slider’s tick marks.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func drawTickMarks()
```

```objc
- (void) drawTickMarks;
```

#### Discussion

You should not call this method explicitly. It’s included so you can override it in a subclass and draw custom tick marks.

## See Also

### Displaying the Cell
- [func barRect(flipped: Bool) -> NSRect](./barrect%28flipped%29.md)
  Returns the rectangle in which the bar is drawn.
- [func knobRect(flipped: Bool) -> NSRect](./knobrect%28flipped%29.md)
  Returns the rectangle in which the slider knob is drawn.
- [func drawBar(inside: NSRect, flipped: Bool)](./drawbar%28inside,flipped%29.md)
  Draws the slider’s bar—but not its bezel or knob—inside the specified rectangle.
- [func drawKnob()](./drawknob%28%29.md)
  Calculates the rectangle in which the knob should be drawn, then calls [`drawKnob(_:)`](./drawknob%28_%29.md) to actually draw the knob.
- [func drawKnob(NSRect)](./drawknob%28_%29.md)
  Draws the slider knob in the given rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/drawtickmarks())*