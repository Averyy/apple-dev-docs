# levelIndicatorStyle

**Framework**: AppKit  
**Kind**: property

The appearance of the indicator.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var levelIndicatorStyle: NSLevelIndicator.Style { get set }
```

#### Discussion

See [`NSLevelIndicator.Style`](nslevelindicator/style.md) for possible styles.

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
- [NSLevelIndicator.Style](nslevelindicator/style.md)
  Constants that specify a level indicator’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicator/levelindicatorstyle)*