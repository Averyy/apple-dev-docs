# numberOfMajorTickMarks

**Framework**: AppKit  
**Kind**: property

The number of major tick marks associated with the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var numberOfMajorTickMarks: Int { get set }
```

#### Discussion

The number of major tick marks must be less than or equal to the number of tick marks returned by [`numberOfTickMarks`](nslevelindicator/numberoftickmarks.md). For example, if the number of tick marks is 11 and you specify 3 major tick marks, the resulting level indicator will display 3 major tick marks alternating with 8 minor tick marks, as in the example shown in [`NSLevelIndicator`](nslevelindicator.md).

![Major and minor tick marks in a level indicator](https://docs-assets.developer.apple.com/published/6d8de4ad21c396ebc4ef77203661539b/media-1965752.gif)

## See Also

- [var tickMarkPosition: NSSlider.TickMarkPosition](nslevelindicator/tickmarkposition.md)
  Determines how the receiver’s tick marks are aligned with it.
- [var numberOfTickMarks: Int](nslevelindicator/numberoftickmarks.md)
  The number of tick marks associated with the receiver.
- [func tickMarkValue(at: Int) -> Double](nslevelindicator/tickmarkvalue(at:).md)
  Returns the receiver’s value represented by the tick mark at the specified index (the minimum-value tick mark has an index of 0).
- [func rectOfTickMark(at: Int) -> NSRect](nslevelindicator/rectoftickmark(at:).md)
  Returns the bounding rectangle of the tick mark identified by the specified index (the minimum-value tick mark is at index 0).
- [var levelIndicatorStyle: NSLevelIndicator.Style](nslevelindicator/levelindicatorstyle.md)
  The appearance of the indicator.
- [NSLevelIndicator.Style](nslevelindicator/style.md)
  Constants that specify a level indicator’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicator/numberofmajortickmarks)*