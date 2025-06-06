# rectOfTickMark(at:)

**Framework**: AppKit  
**Kind**: method

Returns the bounding rectangle of the tick mark identified by the specified index (the minimum-value tick mark is at index 0).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func rectOfTickMark(at index: Int) -> NSRect
```

#### Discussion

If no tick mark is associated with `index`, the method raises an `NSRangeException`.

## See Also

- [var tickMarkPosition: NSSlider.TickMarkPosition](nslevelindicator/tickmarkposition.md)
  Determines how the receiver’s tick marks are aligned with it.
- [var numberOfTickMarks: Int](nslevelindicator/numberoftickmarks.md)
  The number of tick marks associated with the receiver.
- [var numberOfMajorTickMarks: Int](nslevelindicator/numberofmajortickmarks.md)
  The number of major tick marks associated with the receiver.
- [func tickMarkValue(at: Int) -> Double](nslevelindicator/tickmarkvalue(at:).md)
  Returns the receiver’s value represented by the tick mark at the specified index (the minimum-value tick mark has an index of 0).
- [var levelIndicatorStyle: NSLevelIndicator.Style](nslevelindicator/levelindicatorstyle.md)
  The appearance of the indicator.
- [NSLevelIndicator.Style](nslevelindicator/style.md)
  Constants that specify a level indicator’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicator/rectoftickmark(at:))*