# numberOfTickMarks

**Framework**: AppKit  
**Kind**: property

The number of tick marks associated with the slider, including the tick marks assigned to the minimum and maximum values.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var numberOfTickMarks: Int { get set }
```

#### Discussion

By default, this value is 0, and no tick marks appear. The number of tick marks assigned to a slider, along with the slider’s minimum and maximum values, determines the values associated with the tick marks.

## See Also

- [var allowsTickMarkValuesOnly: Bool](nsslidercell/allowstickmarkvaluesonly.md)
  A Boolean value indicating whether the receiver fixes its values to those values represented by its tick marks.
- [func closestTickMarkValue(toValue: Double) -> Double](nsslidercell/closesttickmarkvalue(tovalue:).md)
  Returns the value of the tick mark closest to the specified value.
- [func indexOfTickMark(at: NSPoint) -> Int](nsslidercell/indexoftickmark(at:).md)
  Returns the index of the tick mark closest to the location of the slider represented by the specified point.
- [func rectOfTickMark(at: Int) -> NSRect](nsslidercell/rectoftickmark(at:).md)
  Returns the bounding rectangle of the tick mark at the specified index.
- [var tickMarkPosition: NSSlider.TickMarkPosition](nsslidercell/tickmarkposition.md)
  The position of the tick marks relative to the receiver.
- [func tickMarkValue(at: Int) -> Double](nsslidercell/tickmarkvalue(at:).md)
  Returns the receiver’s value represented by the tick mark at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/numberoftickmarks)*