# drawKnob()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Calculates the rectangle in which the knob should be drawn, then calls [`drawKnob(_:)`](./drawknob%28_%29.md) to actually draw the knob.

**Availability**:
- macOS

## Declaration

```swift
func drawKnob()
```

```objc
- (void) drawKnob;
```

#### Discussion

Before this message is sent, a `lockFocus` method must be sent to the cell’s control view.

You might call this method if you override one of the display methods belonging to `NSControl` or `NSCell`.

##### Special Considerations

If you create a subclass of `NSSliderCell`, don’t override this method. Override [`drawKnob(_:)`](./drawknob%28_%29.md) instead.

## See Also

### Displaying the Cell
- [func barRect(flipped: Bool) -> NSRect](./barrect%28flipped%29.md)
  Returns the rectangle in which the bar is drawn.
- [func drawTickMarks()](./drawtickmarks%28%29.md)
  Draws the slider’s tick marks.
- [func knobRect(flipped: Bool) -> NSRect](./knobrect%28flipped%29.md)
  Returns the rectangle in which the slider knob is drawn.
- [func drawBar(inside: NSRect, flipped: Bool)](./drawbar%28inside,flipped%29.md)
  Draws the slider’s bar—but not its bezel or knob—inside the specified rectangle.
- [func drawKnob(NSRect)](./drawknob%28_%29.md)
  Draws the slider knob in the given rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/drawknob())*