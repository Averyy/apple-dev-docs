# rectOfTickMark(at:)

**Framework**: AppKit  
**Kind**: method

Returns the bounding rectangle of the tick mark identified by `index` (the minimum-value tick mark is at index 0).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func rectOfTickMark(at index: Int) -> NSRect
```

#### Discussion

If no tick mark is associated with `index`, the method raises a `NSRangeException`.

## See Also

- [var tickMarkPosition: NSSlider.TickMarkPosition](nslevelindicatorcell/tickmarkposition.md)
  The placement of tick marks on the level indicator control.
- [var numberOfTickMarks: Int](nslevelindicatorcell/numberoftickmarks.md)
  The number of tick marks displayed by the control.
- [var numberOfMajorTickMarks: Int](nslevelindicatorcell/numberofmajortickmarks.md)
  The number of major tick marks displayed by the control.
- [func tickMarkValue(at: Int) -> Double](nslevelindicatorcell/tickmarkvalue(at:).md)
  Returns the receiver’s value represented by the tick mark at index (the minimum-value tick mark has an index of 0).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/rectoftickmark(at:))*