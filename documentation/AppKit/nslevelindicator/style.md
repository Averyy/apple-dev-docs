# NSLevelIndicator.Style

**Framework**: AppKit  
**Kind**: enum

Constants that specify a level indicator’s appearance.

**Availability**:
- macOS ?+

## Declaration

```swift
enum Style
```

## Topics

### Level Indicator Styles
- [NSLevelIndicator.Style.relevancy](nslevelindicator/style/relevancy.md)
  A style that indicates the relevancy of an item, such as a search result.
- [NSLevelIndicator.Style.continuousCapacity](nslevelindicator/style/continuouscapacity.md)
  A style that indicates the capacity of something, such as how much data is on a hard disk.
- [NSLevelIndicator.Style.discreteCapacity](nslevelindicator/style/discretecapacity.md)
  A style that displays discrete segments that indicate the capacity of something, such as an audio level.
- [NSLevelIndicator.Style.rating](nslevelindicator/style/rating.md)
  A style that indicates a rank, such as a star ranking display.
### Initializers
- [init?(rawValue: UInt)](nslevelindicator/style/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var tickMarkPosition: NSSlider.TickMarkPosition](nslevelindicator/tickmarkposition.md)
  Determines how the receiver’s tick marks are aligned with it.
- [var numberOfTickMarks: Int](nslevelindicator/numberoftickmarks.md)
  The number of tick marks associated with the receiver.
- [var numberOfMajorTickMarks: Int](nslevelindicator/numberofmajortickmarks.md)
  The number of major tick marks associated with the receiver.
- [func tickMarkValue(at: Int) -> Double](nslevelindicator/tickmarkvalue(at:).md)
  Returns the receiver’s value represented by the tick mark at the specified index (the minimum-value tick mark has an index of 0).
- [func rectOfTickMark(at: Int) -> NSRect](nslevelindicator/rectoftickmark(at:).md)
  Returns the bounding rectangle of the tick mark identified by the specified index (the minimum-value tick mark is at index 0).
- [var levelIndicatorStyle: NSLevelIndicator.Style](nslevelindicator/levelindicatorstyle.md)
  The appearance of the indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicator/style)*