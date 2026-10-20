# closestTickMarkValue(toValue:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the value of the tick mark closest to the specified value.

**Availability**:
- macOS

## Declaration

```swift
func closestTickMarkValue(toValue value: Double) -> Double
```

```objc
- (double) closestTickMarkValueToValue:(double) value;
```

#### Return Value

The value of the closest tick mark.

## Parameters

- `value`: The value for which to obtain the closest tick mark.

## See Also

### Managing Tick Marks
- [var allowsTickMarkValuesOnly: Bool](./allowstickmarkvaluesonly.md)
  A Boolean value indicating whether the receiver fixes its values to those values represented by its tick marks.
- [func indexOfTickMark(at: NSPoint) -> Int](./indexoftickmark%28at%29.md)
  Returns the index of the tick mark closest to the location of the slider represented by the specified point.
- [var numberOfTickMarks: Int](./numberoftickmarks.md)
  The number of tick marks associated with the slider, including the tick marks assigned to the minimum and maximum values.
- [func rectOfTickMark(at: Int) -> NSRect](./rectoftickmark%28at%29.md)
  Returns the bounding rectangle of the tick mark at the specified index.
- [var tickMarkPosition: NSSlider.TickMarkPosition](./tickmarkposition.md)
  The position of the tick marks relative to the receiver.
- [func tickMarkValue(at: Int) -> Double](./tickmarkvalue%28at%29.md)
  Returns the receiver’s value represented by the tick mark at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/closesttickmarkvalue(tovalue:))*