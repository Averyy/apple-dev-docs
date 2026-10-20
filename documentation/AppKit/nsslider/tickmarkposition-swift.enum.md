# NSSlider.TickMarkPosition

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The position where a linear slider’s tick marks appear (above, below, leading, or trailing).

**Availability**:
- macOS

## Declaration

```swift
enum TickMarkPosition
```

```c
enum NSTickMarkPosition : NSUInteger;
```

#### Overview

Use these constants for setting [`tickMarkPosition`](../nsslidercell/tickmarkposition.md).

## Topics

### Configuring Horizontal Sliders
- [NSSlider.TickMarkPosition.below](./tickmarkposition-swift.enum/below.md)
  A constant indicating that tick marks are displayed below the slider.
- [NSSlider.TickMarkPosition.above](./tickmarkposition-swift.enum/above.md)
  A constant indicating that tick marks are displayed above the slider.
### Configuring Vertical Sliders
- [static var leading: NSSlider.TickMarkPosition](./tickmarkposition-swift.enum/leading.md)
  A constant indicating that tick marks are displayed on the leading side of the slider.
- [static var trailing: NSSlider.TickMarkPosition](./tickmarkposition-swift.enum/trailing.md)
  A constant indicating that tick marks are displayed on the trailing side of the slider.
### Initializers
- [init?(rawValue: UInt)](./tickmarkposition-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [func tickMarkValue(at: Int) -> Double](./tickmarkvalue%28at%29.md)
  Returns the slider’s value represented by the tick mark at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/tickmarkposition-swift.enum)*