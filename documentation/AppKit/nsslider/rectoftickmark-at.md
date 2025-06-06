# rectOfTickMark(at:)

**Framework**: AppKit  
**Kind**: method

Returns the bounding rectangle of the tick mark at the given index.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func rectOfTickMark(at index: Int) -> NSRect
```

#### Return Value

The bounding rectangle of the specified tick mark.

#### Discussion

If no tick mark is associated with `index`, the method raises `NSRangeException`. In its implementation of this method, the receiving `NSSlider` instance invokes the method of the same name of its [`NSSliderCell`](nsslidercell.md) instance.

## Parameters

- `index`: The index of the tick mark for which to retrieve the bounds.  The minimum-value tick mark is at index  .

## See Also

- [var allowsTickMarkValuesOnly: Bool](nsslider/allowstickmarkvaluesonly.md)
  A Boolean value that indicates whether the slider fixes its values to those values represented by its tick marks.
- [func closestTickMarkValue(toValue: Double) -> Double](nsslider/closesttickmarkvalue(tovalue:).md)
  Returns the value of the tick mark closest to the specified value.
- [func indexOfTickMark(at: NSPoint) -> Int](nsslider/indexoftickmark(at:).md)
  Returns the index of the tick mark closest to the location of the slider represented by the given point.
- [var numberOfTickMarks: Int](nsslider/numberoftickmarks.md)
  The number of tick marks associated with the slider.
- [var tickMarkPosition: NSSlider.TickMarkPosition](nsslider/tickmarkposition-swift.property.md)
  Determines where the slider’s tick marks are displayed.
- [NSSlider.TickMarkPosition](nsslider/tickmarkposition-swift.enum.md)
  The position where a linear slider’s tick marks appear (above, below, leading, or trailing).
- [func tickMarkValue(at: Int) -> Double](nsslider/tickmarkvalue(at:).md)
  Returns the slider’s value represented by the tick mark at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/rectoftickmark(at:))*