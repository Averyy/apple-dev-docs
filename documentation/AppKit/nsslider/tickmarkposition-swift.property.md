# tickMarkPosition

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Determines where the slider’s tick marks are displayed.

**Availability**:
- macOS

## Declaration

```swift
var tickMarkPosition: NSSlider.TickMarkPosition { get set }
```

```objc
@property NSTickMarkPosition tickMarkPosition;
```

## Discussion

For horizontal sliders, use [`NSSlider.TickMarkPosition.below`](./tickmarkposition-swift.enum/below.md) and [`NSSlider.TickMarkPosition.above`](./tickmarkposition-swift.enum/above.md). For vertical sliders, use [`leading`](./tickmarkposition-swift.enum/leading.md), and [`trailing`](./tickmarkposition-swift.enum/trailing.md). The default positions are `below` for horizontal and `leading` for vertical. This property has no effect if [`numberOfTickMarks`](./numberoftickmarks.md) is `0`, or if the slider is circular. In its implementation of this property, the receiving `NSSlider` instance invokes the method of the same name of its `NSSliderCell` instance.

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
- [NSSlider.TickMarkPosition](./tickmarkposition-swift.enum.md)
  The position where a linear slider’s tick marks appear (above, below, leading, or trailing).
- [func tickMarkValue(at: Int) -> Double](./tickmarkvalue%28at%29.md)
  Returns the slider’s value represented by the tick mark at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/tickmarkposition-swift.property)*