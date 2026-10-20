# drawKnob()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the knob.

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

You should never need to invoke this method directly, but may wish to override it to customize the appearance of the knob.

## See Also

### Related Documentation
- [func rect(for: NSScroller.Part) -> NSRect](./rect%28for%29.md)
  Returns the rectangle occupied by `aPart`, which for this method is interpreted literally rather than as an indicator of scrolling direction.
### Drawing Scroller Parts
- [func drawKnobSlot(in: NSRect, highlight: Bool)](./drawknobslot%28in,highlight%29.md)
  Draws the portion of the scroller’s track, possibly including the line increment and decrement arrow buttons, that falls in the given rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/drawknob())*