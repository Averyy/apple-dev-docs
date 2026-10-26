# NSLevelIndicator.Style

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify a level indicator’s appearance.

**Availability**:
- macOS

## Declaration

```swift
enum Style
```

```c
enum NSLevelIndicatorStyle : NSUInteger;
```

## Topics

### Level Indicator Styles
- [NSLevelIndicator.Style.relevancy](./style/relevancy.md)
  A style that indicates the relevancy of an item, such as a search result.
- [NSLevelIndicator.Style.continuousCapacity](./style/continuouscapacity.md)
  A style that indicates the capacity of something, such as how much data is on a hard disk.
- [NSLevelIndicator.Style.discreteCapacity](./style/discretecapacity.md)
  A style that displays discrete segments that indicate the capacity of something, such as an audio level.
- [NSLevelIndicator.Style.rating](./style/rating.md)
  A style that indicates a rank, such as a star ranking display.
### Initializers
- [init?(rawValue: UInt)](./style/init%28rawvalue%29.md)
### Deprecated
- [NSRelevancyLevelIndicatorStyle](../nsrelevancylevelindicatorstyle.md)
  A style that indicates the relevancy of an item, such as a search result.
- [NSRatingLevelIndicatorStyle](../nsratinglevelindicatorstyle.md)
  A style that indicates a rank, such as a star ranking display.
- [NSDiscreteCapacityLevelIndicatorStyle](../nsdiscretecapacitylevelindicatorstyle.md)
  A style that displays discrete segments that indicate the capacity of something, such as an audio level.
- [NSContinuousCapacityLevelIndicatorStyle](../nscontinuouscapacitylevelindicatorstyle.md)
  A style that indicates the capacity of something, such as how much data is on a hard disk.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing Tick Marks and Style
- [var tickMarkPosition: NSSlider.TickMarkPosition](./tickmarkposition.md)
  Determines how the receiver’s tick marks are aligned with it.
- [var numberOfTickMarks: Int](./numberoftickmarks.md)
  The number of tick marks associated with the receiver.
- [var numberOfMajorTickMarks: Int](./numberofmajortickmarks.md)
  The number of major tick marks associated with the receiver.
- [func tickMarkValue(at: Int) -> Double](./tickmarkvalue%28at%29.md)
  Returns the receiver’s value represented by the tick mark at the specified index (the minimum-value tick mark has an index of 0).
- [func rectOfTickMark(at: Int) -> NSRect](./rectoftickmark%28at%29.md)
  Returns the bounding rectangle of the tick mark identified by the specified index (the minimum-value tick mark is at index 0).
- [var levelIndicatorStyle: NSLevelIndicator.Style](./levelindicatorstyle.md)
  The appearance of the indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicator/style)*