# NSSlider.TickMarkPosition

**Framework**: AppKit  
**Kind**: enum

The position where a linear slider’s tick marks appear (above, below, leading, or trailing).

**Availability**:
- macOS ?+

## Declaration

```swift
enum TickMarkPosition
```

#### Overview

Use these constants for setting [`tickMarkPosition`](nsslidercell/tickmarkposition.md).

## Topics

### Configuring Horizontal Sliders
- [NSSlider.TickMarkPosition.below](nsslider/tickmarkposition-swift.enum/below.md)
  A constant indicating that tick marks are displayed below the slider.
- [NSSlider.TickMarkPosition.above](nsslider/tickmarkposition-swift.enum/above.md)
  A constant indicating that tick marks are displayed above the slider.
### Configuring Vertical Sliders
- [static var leading: NSSlider.TickMarkPosition](nsslider/tickmarkposition-swift.enum/leading.md)
  A constant indicating that tick marks are displayed on the leading side of the slider.
- [static var trailing: NSSlider.TickMarkPosition](nsslider/tickmarkposition-swift.enum/trailing.md)
  A constant indicating that tick marks are displayed on the trailing side of the slider.
### Initializers
- [init?(rawValue: UInt)](nsslider/tickmarkposition-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var allowsTickMarkValuesOnly: Bool](nsslider/allowstickmarkvaluesonly.md)
  A Boolean value that indicates whether the slider fixes its values to those values represented by its tick marks.
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
- [func tickMarkValue(at: Int) -> Double](nsslider/tickmarkvalue(at:).md)
  Returns the slider’s value represented by the tick mark at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/tickmarkposition-swift.enum)*