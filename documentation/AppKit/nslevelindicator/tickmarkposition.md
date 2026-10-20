# tickMarkPosition

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Determines how the receiver’s tick marks are aligned with it.

**Availability**:
- macOS

## Declaration

```swift
var tickMarkPosition: NSSlider.TickMarkPosition { get set }
```

```objc
@property NSTickMarkPosition tickMarkPosition;
```

#### Discussion

The default alignments are `NSTickMarkBelow` and `NSTickMarkLeft`. This property has no effect if no tick marks have been assigned (that is, [`numberOfTickMarks`](./numberoftickmarks.md) returns 0).

## See Also

### Managing Tick Marks and Style
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
- [NSLevelIndicator.Style](./style.md)
  Constants that specify a level indicator’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicator/tickmarkposition)*