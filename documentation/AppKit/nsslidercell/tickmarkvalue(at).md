# tickMarkValue(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the receiver’s value represented by the tick mark at the specified index.

**Availability**:
- macOS

## Declaration

```swift
func tickMarkValue(at index: Int) -> Double
```

```objc
- (double) tickMarkValueAtIndex:(NSInteger) index;
```

## Return Value

The value represented by the specified tick mark.

## Parameters

- `index`: The index of the tick mark for which to retrieve the value.  The minimum-value tick mark has an index of 0.

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
- [func rectOfTickMark(at: Int) -> NSRect](./rectoftickmark%28at%29.md)
  Returns the bounding rectangle of the tick mark at the specified index.
- [var tickMarkPosition: NSSlider.TickMarkPosition](./tickmarkposition.md)
  The position of the tick marks relative to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/tickmarkvalue(at:))*