# indexOfTickMark(at:)

**Framework**: AppKit  
**Kind**: method

Returns the index of the tick mark closest to the location of the slider represented by the specified point.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func indexOfTickMark(at point: NSPoint) -> Int
```

#### Return Value

The index of the tick mark closest to the specified location.

#### Discussion

If `point` is not within the bounding rectangle (plus an extra pixel of space) of any tick mark, the method returns `NSNotFound`. This method calls [`rectOfTickMark(at:)`](nsslidercell/rectoftickmark(at:).md) for each tick mark on the slider until it finds a tick mark containing `point`.

## Parameters

- `point`: The point representing the slider location.

## See Also

- [var allowsTickMarkValuesOnly: Bool](nsslidercell/allowstickmarkvaluesonly.md)
  A Boolean value indicating whether the receiver fixes its values to those values represented by its tick marks.
- [func closestTickMarkValue(toValue: Double) -> Double](nsslidercell/closesttickmarkvalue(tovalue:).md)
  Returns the value of the tick mark closest to the specified value.
- [var numberOfTickMarks: Int](nsslidercell/numberoftickmarks.md)
  The number of tick marks associated with the slider, including the tick marks assigned to the minimum and maximum values.
- [func rectOfTickMark(at: Int) -> NSRect](nsslidercell/rectoftickmark(at:).md)
  Returns the bounding rectangle of the tick mark at the specified index.
- [var tickMarkPosition: NSSlider.TickMarkPosition](nsslidercell/tickmarkposition.md)
  The position of the tick marks relative to the receiver.
- [func tickMarkValue(at: Int) -> Double](nsslidercell/tickmarkvalue(at:).md)
  Returns the receiver’s value represented by the tick mark at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/indexoftickmark(at:))*