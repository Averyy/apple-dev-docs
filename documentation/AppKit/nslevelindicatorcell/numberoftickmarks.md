# numberOfTickMarks

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of tick marks displayed by the control.

**Availability**:
- macOS

## Declaration

```swift
var numberOfTickMarks: Int { get set }
```

```objc
@property NSInteger numberOfTickMarks;
```

## Discussion

The value in this property represents all of the tick marks displayed by the control, including those positioned at the minimum and maximum values. The default value of this property is `0`, which results in no tick marks being displayed.

## See Also

### Managing Tick Marks
- [var tickMarkPosition: NSSlider.TickMarkPosition](./tickmarkposition.md)
  The placement of tick marks on the level indicator control.
- [var numberOfMajorTickMarks: Int](./numberofmajortickmarks.md)
  The number of major tick marks displayed by the control.
- [func tickMarkValue(at: Int) -> Double](./tickmarkvalue%28at%29.md)
  Returns the receiver’s value represented by the tick mark at index (the minimum-value tick mark has an index of 0).
- [func rectOfTickMark(at: Int) -> NSRect](./rectoftickmark%28at%29.md)
  Returns the bounding rectangle of the tick mark identified by `index` (the minimum-value tick mark is at index 0).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/numberoftickmarks)*