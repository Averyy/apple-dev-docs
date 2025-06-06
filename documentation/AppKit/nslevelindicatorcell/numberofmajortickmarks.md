# numberOfMajorTickMarks

**Framework**: AppKit  
**Kind**: property

The number of major tick marks displayed by the control.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var numberOfMajorTickMarks: Int { get set }
```

#### Discussion

The value in this property must be less than or equal to the value in the [`numberOfTickMarks`](nslevelindicatorcell/numberoftickmarks.md) property.

## See Also

- [var tickMarkPosition: NSSlider.TickMarkPosition](nslevelindicatorcell/tickmarkposition.md)
  The placement of tick marks on the level indicator control.
- [var numberOfTickMarks: Int](nslevelindicatorcell/numberoftickmarks.md)
  The number of tick marks displayed by the control.
- [func tickMarkValue(at: Int) -> Double](nslevelindicatorcell/tickmarkvalue(at:).md)
  Returns the receiver’s value represented by the tick mark at index (the minimum-value tick mark has an index of 0).
- [func rectOfTickMark(at: Int) -> NSRect](nslevelindicatorcell/rectoftickmark(at:).md)
  Returns the bounding rectangle of the tick mark identified by `index` (the minimum-value tick mark is at index 0).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/numberofmajortickmarks)*