# rectOfTickMark(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the bounding rectangle of the tick mark at the given index.

**Availability**:
- macOS

## Declaration

```swift
func rectOfTickMark(at index: Int) -> NSRect
```

```objc
- (NSRect) rectOfTickMarkAtIndex:(NSInteger) index;
```

## Return Value

The bounding rectangle of the specified tick mark.

## Discussion

If no tick mark is associated with `index`, the method raises `NSRangeException`. In its implementation of this method, the receiving `NSSlider` instance invokes the method of the same name of its [`NSSliderCell`](../nsslidercell.md) instance.

## Parameters

- `index`: The index of the tick mark for which to retrieve the bounds.  The minimum-value tick mark is at index `0`.

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
- [var tickMarkPosition: NSSlider.TickMarkPosition](./tickmarkposition-swift.property.md)
  Determines where the slider’s tick marks are displayed.
- [NSSlider.TickMarkPosition](./tickmarkposition-swift.enum.md)
  The position where a linear slider’s tick marks appear (above, below, leading, or trailing).
- [func tickMarkValue(at: Int) -> Double](./tickmarkvalue%28at%29.md)
  Returns the slider’s value represented by the tick mark at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/rectoftickmark(at:))*