# tickMarkPosition

**Framework**: AppKit  
**Kind**: property

The position of the tick marks relative to the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var tickMarkPosition: NSSlider.TickMarkPosition { get set }
```

#### Discussion

The value of this property is a constant indicating the position of the tick marks. Possible values  are described in [`NSSlider.TickMarkPosition`](nsslider/tickmarkposition-swift.enum.md). The default alignments are `NSTickMarkBelow` and `NSTickMarkLeft`. Setting this property has no effect if no tick marks have been assigned (that is, if [`numberOfTickMarks`](nsslidercell/numberoftickmarks.md) is 0).

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
- [func tickMarkValue(at: Int) -> Double](nsslidercell/tickmarkvalue(at:).md)
  Returns the receiver’s value represented by the tick mark at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/tickmarkposition)*