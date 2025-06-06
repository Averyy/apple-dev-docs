# numberOfTickMarks

**Framework**: AppKit  
**Kind**: property

The number of tick marks displayed by the control.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var numberOfTickMarks: Int { get set }
```

#### Discussion

The value in this property represents all of the tick marks displayed by the control, including those positioned at the minimum and maximum values. The default value of this property is `0`, which results in no tick marks being displayed.

## See Also

- [var tickMarkPosition: NSSlider.TickMarkPosition](nslevelindicatorcell/tickmarkposition.md)
  The placement of tick marks on the level indicator control.
- [var numberOfMajorTickMarks: Int](nslevelindicatorcell/numberofmajortickmarks.md)
  The number of major tick marks displayed by the control.
- [func tickMarkValue(at: Int) -> Double](nslevelindicatorcell/tickmarkvalue(at:).md)
  Returns the receiver’s value represented by the tick mark at index (the minimum-value tick mark has an index of 0).
- [func rectOfTickMark(at: Int) -> NSRect](nslevelindicatorcell/rectoftickmark(at:).md)
  Returns the bounding rectangle of the tick mark identified by `index` (the minimum-value tick mark is at index 0).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/numberoftickmarks)*