# rectOfTickMark(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the bounding rectangle of the tick mark identified by `index` (the minimum-value tick mark is at index 0).

**Availability**:
- macOS

## Declaration

```swift
func rectOfTickMark(at index: Int) -> NSRect
```

```objc
- (NSRect) rectOfTickMarkAtIndex:(NSInteger) index;
```

## Discussion

If no tick mark is associated with `index`, the method raises a `NSRangeException`.

## See Also

### Managing Tick Marks
- [var tickMarkPosition: NSSlider.TickMarkPosition](./tickmarkposition.md)
  The placement of tick marks on the level indicator control.
- [var numberOfTickMarks: Int](./numberoftickmarks.md)
  The number of tick marks displayed by the control.
- [var numberOfMajorTickMarks: Int](./numberofmajortickmarks.md)
  The number of major tick marks displayed by the control.
- [func tickMarkValue(at: Int) -> Double](./tickmarkvalue%28at%29.md)
  Returns the receiver’s value represented by the tick mark at index (the minimum-value tick mark has an index of 0).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/rectoftickmark(at:))*