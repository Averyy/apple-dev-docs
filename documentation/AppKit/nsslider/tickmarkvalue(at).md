# tickMarkValue(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the slider’s value represented by the tick mark at the specified index.

**Availability**:
- macOS

## Declaration

```swift
func tickMarkValue(at index: Int) -> Double
```

```objc
- (double) tickMarkValueAtIndex:(NSInteger) index;
```

#### Return Value

The value of the specified tick mark.

#### Discussion

In its implementation of this method, the receiving `NSSlider` instance invokes the method of the same name of its `NSSliderCell` instance.

## Parameters

- `index`: The index of the tick mark for which to return the value. The minimum-value tick mark has an index of `0`.

## See Also

### Managing tick marks
- [var allowsTickMarkValuesOnly: Bool](./allowstickmarkvaluesonly.md)
  A Boolean value that indicates whether the slider fixes its values to those values represented by its tick marks.
- [func closestTickMarkValue(toValue: Double) -> Double](./closesttickmarkvalue%28tovalue%29.md)
  Returns the value of the tick mark closest to the specified value.
- [func indexOfTickMark(at: NSPoint) -> Int](./indexoftickmark%28at%29.md)
  Returns the index of the tick mark closest to the location of the slider represented by the given point.
- [var numberOfTickMarks: Int](./numberoftickmarks.md)
  The number of tick marks associated with the slider.
- [func rectOfTickMark(at: Int) -> NSRect](./rectoftickmark%28at%29.md)
  Returns the bounding rectangle of the tick mark at the given index.
- [var tickMarkPosition: NSSlider.TickMarkPosition](./tickmarkposition-swift.property.md)
  Determines where the slider’s tick marks are displayed.
- [NSSlider.TickMarkPosition](./tickmarkposition-swift.enum.md)
  The position where a linear slider’s tick marks appear (above, below, leading, or trailing).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/tickmarkvalue(at:))*