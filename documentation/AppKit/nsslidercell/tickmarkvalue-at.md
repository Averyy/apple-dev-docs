# tickMarkValue(at:)

**Framework**: AppKit  
**Kind**: method

Returns the receiver’s value represented by the tick mark at the specified index.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func tickMarkValue(at index: Int) -> Double
```

#### Return Value

The value represented by the specified tick mark.

## Parameters

- `index`: The index of the tick mark for which to retrieve the value.  The minimum-value tick mark has an index of 0.

## See Also

- [var allowsTickMarkValuesOnly: Bool](nsslidercell/allowstickmarkvaluesonly.md)
  A Boolean value indicating whether the receiver fixes its values to those values represented by its tick marks.
- [func closestTickMarkValue(toValue: Double) -> Double](nsslidercell/closesttickmarkvalue(tovalue:).md)
  Returns the value of the tick mark closest to the specified value.
- [func indexOfTickMark(at: NSPoint) -> Int](nsslidercell/indexoftickmark(at:).md)
  Returns the index of the tick mark closest to the location of the slider represented by the specified point.
- [var numberOfTickMarks: Int](nsslidercell/numberoftickmarks.md)
  The number of tick marks associated with the slider, including the tick marks assigned to the minimum and maximum values.
- [func rectOfTickMark(at: Int) -> NSRect](nsslidercell/rectoftickmark(at:).md)
  Returns the bounding rectangle of the tick mark at the specified index.
- [var tickMarkPosition: NSSlider.TickMarkPosition](nsslidercell/tickmarkposition.md)
  The position of the tick marks relative to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/tickmarkvalue(at:))*