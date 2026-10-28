# knobRect(flipped:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle in which the slider knob is drawn.

**Availability**:
- macOS

## Declaration

```swift
func knobRect(flipped: Bool) -> NSRect
```

```objc
- (NSRect) knobRectFlipped:(BOOL) flipped;
```

## Return Value

The rectangle in which the knob is drawn, specified in the coordinate system of the `NSSlider` or `NSMatrix` with which the receiver is associated.

## Discussion

The knob rectangle depends on where in the slider the knob belongs—that is, it depends on the receiver’s minimum and maximum values and on the value the position of the knob will represent.

## Parameters

- `flipped`: [`true`](../../Swift/true.md) if the coordinate system of the associated `NSSlider` or `NSMatrix` is flipped; otherwise [`false`](../../Swift/false.md). You can determine whether this is the case by sending the `NSView` message [`isFlipped`](../nsview/isflipped.md) message to the `NSMatrix` or `NSSlider`.

## See Also

### Displaying the Cell
- [func barRect(flipped: Bool) -> NSRect](./barrect%28flipped%29.md)
  Returns the rectangle in which the bar is drawn.
- [func drawTickMarks()](./drawtickmarks%28%29.md)
  Draws the slider’s tick marks.
- [func drawBar(inside: NSRect, flipped: Bool)](./drawbar%28inside,flipped%29.md)
  Draws the slider’s bar—but not its bezel or knob—inside the specified rectangle.
- [func drawKnob()](./drawknob%28%29.md)
  Calculates the rectangle in which the knob should be drawn, then calls [`drawKnob(_:)`](./drawknob%28_%29.md) to actually draw the knob.
- [func drawKnob(NSRect)](./drawknob%28_%29.md)
  Draws the slider knob in the given rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/knobrect(flipped:))*