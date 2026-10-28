# rectOfTickMark(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the bounding rectangle of the tick mark identified by the specified index (the minimum-value tick mark is at index 0).

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

If no tick mark is associated with `index`, the method raises an `NSRangeException`.

## See Also

### Managing Tick Marks and Style
- [var tickMarkPosition: NSSlider.TickMarkPosition](./tickmarkposition.md)
  Determines how the receiver’s tick marks are aligned with it.
- [var numberOfTickMarks: Int](./numberoftickmarks.md)
  The number of tick marks associated with the receiver.
- [var numberOfMajorTickMarks: Int](./numberofmajortickmarks.md)
  The number of major tick marks associated with the receiver.
- [func tickMarkValue(at: Int) -> Double](./tickmarkvalue%28at%29.md)
  Returns the receiver’s value represented by the tick mark at the specified index (the minimum-value tick mark has an index of 0).
- [var levelIndicatorStyle: NSLevelIndicator.Style](./levelindicatorstyle.md)
  The appearance of the indicator.
- [NSLevelIndicator.Style](./style.md)
  Constants that specify a level indicator’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicator/rectoftickmark(at:))*