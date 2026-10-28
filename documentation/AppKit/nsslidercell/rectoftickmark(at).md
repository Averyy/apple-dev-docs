# rectOfTickMark(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the bounding rectangle of the tick mark at the specified index.

**Availability**:
- macOS

## Declaration

```swift
func rectOfTickMark(at index: Int) -> NSRect
```

```objc
- (NSRect) rectOfTickMarkAtIndex:(NSInteger) index;
```

## Return Value

The bounding rectangle of the specified tick mark.

## Discussion

If no tick mark is associated with `index`, the method raises `NSRangeException`.

## Parameters

- `index`: The index of the tick mark for which to return the bounding rectangle. The minimum-value tick mark is at index 0.

## See Also

### Managing Tick Marks
- [var allowsTickMarkValuesOnly: Bool](./allowstickmarkvaluesonly.md)
  A Boolean value indicating whether the receiver fixes its values to those values represented by its tick marks.
- [func closestTickMarkValue(toValue: Double) -> Double](./closesttickmarkvalue%28tovalue%29.md)
  Returns the value of the tick mark closest to the specified value.
- [func indexOfTickMark(at: NSPoint) -> Int](./indexoftickmark%28at%29.md)
  Returns the index of the tick mark closest to the location of the slider represented by the specified point.
- [var numberOfTickMarks: Int](./numberoftickmarks.md)
  The number of tick marks associated with the slider, including the tick marks assigned to the minimum and maximum values.
- [var tickMarkPosition: NSSlider.TickMarkPosition](./tickmarkposition.md)
  The position of the tick marks relative to the receiver.
- [func tickMarkValue(at: Int) -> Double](./tickmarkvalue%28at%29.md)
  Returns the receiver’s value represented by the tick mark at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/rectoftickmark(at:))*