# tickMarkValue(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the receiver’s value represented by the tick mark at index (the minimum-value tick mark has an index of 0).

**Availability**:
- macOS

## Declaration

```swift
func tickMarkValue(at index: Int) -> Double
```

```objc
- (double) tickMarkValueAtIndex:(NSInteger) index;
```

## See Also

### Managing Tick Marks
- [var tickMarkPosition: NSSlider.TickMarkPosition](./tickmarkposition.md)
  The placement of tick marks on the level indicator control.
- [var numberOfTickMarks: Int](./numberoftickmarks.md)
  The number of tick marks displayed by the control.
- [var numberOfMajorTickMarks: Int](./numberofmajortickmarks.md)
  The number of major tick marks displayed by the control.
- [func rectOfTickMark(at: Int) -> NSRect](./rectoftickmark%28at%29.md)
  Returns the bounding rectangle of the tick mark identified by `index` (the minimum-value tick mark is at index 0).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/tickmarkvalue(at:))*