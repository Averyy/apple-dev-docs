# drawKnob(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the slider knob in the given rectangle.

**Availability**:
- macOS

## Declaration

```swift
func drawKnob(_ knobRect: NSRect)
```

```objc
- (void) drawKnob:(NSRect) knobRect;
```

## Mentions

- [Updating views automatically with observation tracking in AppKit](../updating-views-automatically-with-observation-tracking-in-appkit.md)

#### Discussion

Before this message is sent, a [`lockFocus()`](../nsview/lockfocus%28%29.md) message must be sent to the cell’s control view.

You should not call this method explicitly. It’s included so you can override it in a subclass.

## Parameters

- `knobRect`: The rectangle in which to draw the slider knob.

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
- [func drawKnob()](./drawknob%28%29.md)
  Calculates the rectangle in which the knob should be drawn, then calls [`drawKnob(_:)`](./drawknob%28_%29.md) to actually draw the knob.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/drawknob(_:))*