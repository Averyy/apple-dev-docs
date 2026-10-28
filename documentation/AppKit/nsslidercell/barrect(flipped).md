# barRect(flipped:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle in which the bar is drawn.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func barRect(flipped: Bool) -> NSRect
```

```objc
- (NSRect) barRectFlipped:(BOOL) flipped;
```

## Return Value

The rectangle in which the bar is drawn, specified in the coordinate system of the `NSSlider` or `NSMatrix` with which the receiver is associated. The bar doesn’t include the slider’s bezel or knob.

## Discussion

You can override this method if custom bar artwork requires specific dimensions.

## Parameters

- `flipped`: [`true`](../../Swift/true.md) if the coordinate system of the associated `NSSlider` or `NSMatrix` is flipped; otherwise [`false`](../../Swift/false.md). You can determine whether this is the case by sending the `NSView` message [`isFlipped`](../nsview/isflipped.md) message to the `NSMatrix` or `NSSlider`.

## See Also

### Displaying the Cell
- [func drawTickMarks()](./drawtickmarks%28%29.md)
  Draws the slider’s tick marks.
- [func knobRect(flipped: Bool) -> NSRect](./knobrect%28flipped%29.md)
  Returns the rectangle in which the slider knob is drawn.
- [func drawBar(inside: NSRect, flipped: Bool)](./drawbar%28inside,flipped%29.md)
  Draws the slider’s bar—but not its bezel or knob—inside the specified rectangle.
- [func drawKnob()](./drawknob%28%29.md)
  Calculates the rectangle in which the knob should be drawn, then calls [`drawKnob(_:)`](./drawknob%28_%29.md) to actually draw the knob.
- [func drawKnob(NSRect)](./drawknob%28_%29.md)
  Draws the slider knob in the given rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/barrect(flipped:))*