# numberOfTickMarks

**Framework**: AppKit  
**Kind**: property

The number of tick marks associated with the slider.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var numberOfTickMarks: Int { get set }
```

#### Discussion

This property includes tick marks assigned to the minimum and maximum values. In its implementation of this property, the receiving `NSSlider` instance invokes the method of the same name of its `NSSliderCell` instance. By default, this value is 0, and no tick marks appear. The number of tick marks assigned to a slider, along with the slider’s minimum and maximum values, determines the values associated with the tick marks.

## See Also

- [var allowsTickMarkValuesOnly: Bool](nsslider/allowstickmarkvaluesonly.md)
  A Boolean value that indicates whether the slider fixes its values to those values represented by its tick marks.
- [func closestTickMarkValue(toValue: Double) -> Double](nsslider/closesttickmarkvalue(tovalue:).md)
  Returns the value of the tick mark closest to the specified value.
- [func indexOfTickMark(at: NSPoint) -> Int](nsslider/indexoftickmark(at:).md)
  Returns the index of the tick mark closest to the location of the slider represented by the given point.
- [func rectOfTickMark(at: Int) -> NSRect](nsslider/rectoftickmark(at:).md)
  Returns the bounding rectangle of the tick mark at the given index.
- [var tickMarkPosition: NSSlider.TickMarkPosition](nsslider/tickmarkposition-swift.property.md)
  Determines where the slider’s tick marks are displayed.
- [NSSlider.TickMarkPosition](nsslider/tickmarkposition-swift.enum.md)
  The position where a linear slider’s tick marks appear (above, below, leading, or trailing).
- [func tickMarkValue(at: Int) -> Double](nsslider/tickmarkvalue(at:).md)
  Returns the slider’s value represented by the tick mark at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/numberoftickmarks)*