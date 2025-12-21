# allowsTickMarkValuesOnly

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the slider fixes its values to those values represented by its tick marks.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var allowsTickMarkValuesOnly: Bool { get set }
```

#### Discussion

This value is [`true`](https://developer.apple.com/documentation/Swift/true) if the slider fixes its values to the values represented by its tick marks; otherwise it’s [`false`](https://developer.apple.com/documentation/Swift/false). For example, if a slider has a minimum value of `0`, a maximum value of `100`, and five markers, the allowable values are `0`, `25`, `50`, `75`, and `100`. When users move the slider’s knob, it jumps to the tick mark nearest the cursor when the mouse button is released. This method has no effect if the slider has no tick marks. In its implementation of this method, the receiving `NSSlider` instance invokes the method of the same name of its `NSSliderCell` instance.

## See Also

- [func closestTickMarkValue(toValue: Double) -> Double](nsslider/closesttickmarkvalue(tovalue:).md)
  Returns the value of the tick mark closest to the specified value.
- [func indexOfTickMark(at: NSPoint) -> Int](nsslider/indexoftickmark(at:).md)
  Returns the index of the tick mark closest to the location of the slider represented by the given point.
- [var numberOfTickMarks: Int](nsslider/numberoftickmarks.md)
  The number of tick marks associated with the slider.
- [func rectOfTickMark(at: Int) -> NSRect](nsslider/rectoftickmark(at:).md)
  Returns the bounding rectangle of the tick mark at the given index.
- [var tickMarkPosition: NSSlider.TickMarkPosition](nsslider/tickmarkposition-swift.property.md)
  Determines where the slider’s tick marks are displayed.
- [NSSlider.TickMarkPosition](nsslider/tickmarkposition-swift.enum.md)
  The position where a linear slider’s tick marks appear (above, below, leading, or trailing).
- [func tickMarkValue(at: Int) -> Double](nsslider/tickmarkvalue(at:).md)
  Returns the slider’s value represented by the tick mark at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/allowstickmarkvaluesonly)*