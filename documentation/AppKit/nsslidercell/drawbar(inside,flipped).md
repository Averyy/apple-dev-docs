# drawBar(inside:flipped:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the slider’s bar—but not its bezel or knob—inside the specified rectangle.

**Availability**:
- macOS

## Declaration

```swift
func drawBar(inside rect: NSRect, flipped: Bool)
```

```objc
- (void) drawBarInside:(NSRect) rect flipped:(BOOL) flipped;
```

## Mentions

- [Updating views automatically with observation tracking in AppKit](../updating-views-automatically-with-observation-tracking-in-appkit.md)

## Discussion

You should not call this method explicitly. It’s included so you can override it in a subclass.

## Parameters

- `rect`: The bounds of the slider’s bar, not of its interior rectangle.
- `flipped`: A Boolean value that indicates whether the cell’s control view—that is, the `NSSlider` or `NSMatrix` associated with the `NSSliderCell`—has a flipped coordinate system.

## See Also

### Displaying the Cell
- [func barRect(flipped: Bool) -> NSRect](./barrect%28flipped%29.md)
  Returns the rectangle in which the bar is drawn.
- [func drawTickMarks()](./drawtickmarks%28%29.md)
  Draws the slider’s tick marks.
- [func knobRect(flipped: Bool) -> NSRect](./knobrect%28flipped%29.md)
  Returns the rectangle in which the slider knob is drawn.
- [func drawKnob()](./drawknob%28%29.md)
  Calculates the rectangle in which the knob should be drawn, then calls [`drawKnob(_:)`](./drawknob%28_%29.md) to actually draw the knob.
- [func drawKnob(NSRect)](./drawknob%28_%29.md)
  Draws the slider knob in the given rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/drawbar(inside:flipped:))*