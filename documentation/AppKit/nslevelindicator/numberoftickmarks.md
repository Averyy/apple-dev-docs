# numberOfTickMarks

**Framework**: AppKit  
**Kind**: property

The number of tick marks associated with the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var numberOfTickMarks: Int { get set }
```

#### Discussion

By default, this value is 0, and no tick marks appear. The number of tick marks assigned to a slider, along with the slider’s minimum and maximum values, determines the values associated with the tick marks.

## See Also

- [var tickMarkPosition: NSSlider.TickMarkPosition](nslevelindicator/tickmarkposition.md)
  Determines how the receiver’s tick marks are aligned with it.
- [var numberOfMajorTickMarks: Int](nslevelindicator/numberofmajortickmarks.md)
  The number of major tick marks associated with the receiver.
- [func tickMarkValue(at: Int) -> Double](nslevelindicator/tickmarkvalue(at:).md)
  Returns the receiver’s value represented by the tick mark at the specified index (the minimum-value tick mark has an index of 0).
- [func rectOfTickMark(at: Int) -> NSRect](nslevelindicator/rectoftickmark(at:).md)
  Returns the bounding rectangle of the tick mark identified by the specified index (the minimum-value tick mark is at index 0).
- [var levelIndicatorStyle: NSLevelIndicator.Style](nslevelindicator/levelindicatorstyle.md)
  The appearance of the indicator.
- [NSLevelIndicator.Style](nslevelindicator/style.md)
  Constants that specify a level indicator’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicator/numberoftickmarks)*