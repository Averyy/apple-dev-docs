# levelIndicatorStyle

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The appearance of the indicator.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var levelIndicatorStyle: NSLevelIndicator.Style { get set }
```

```objc
@property NSLevelIndicatorStyle levelIndicatorStyle;
```

## Discussion

See [`NSLevelIndicator.Style`](./style.md) for possible styles.

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
- [NSLevelIndicator.Style](./style.md)
  Constants that specify a level indicator’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicator/levelindicatorstyle)*