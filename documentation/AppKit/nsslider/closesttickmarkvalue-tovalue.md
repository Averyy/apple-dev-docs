# closestTickMarkValue(toValue:)

**Framework**: AppKit  
**Kind**: method

Returns the value of the tick mark closest to the specified value.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func closestTickMarkValue(toValue value: Double) -> Double
```

#### Return Value

The value of the tick mark closest to `aValue`.

#### Discussion

In its implementation of this method, the slider invokes the method of the same name of its `NSSliderCell` instance.

## Parameters

- `value`: The value for which to return the closest tick mark.

## See Also

- [var allowsTickMarkValuesOnly: Bool](nsslider/allowstickmarkvaluesonly.md)
  A Boolean value that indicates whether the slider fixes its values to those values represented by its tick marks.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/closesttickmarkvalue(tovalue:))*