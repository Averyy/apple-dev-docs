# tickMarkPosition

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The position of the tick marks relative to the receiver.

**Availability**:
- macOS

## Declaration

```swift
var tickMarkPosition: NSSlider.TickMarkPosition { get set }
```

```objc
@property NSTickMarkPosition tickMarkPosition;
```

## Discussion

The value of this property is a constant indicating the position of the tick marks. Possible values  are described in [`NSSlider.TickMarkPosition`](../nsslider/tickmarkposition-swift.enum.md). The default alignments are `NSTickMarkBelow` and `NSTickMarkLeft`. Setting this property has no effect if no tick marks have been assigned (that is, if [`numberOfTickMarks`](./numberoftickmarks.md) is 0).

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
- [func tickMarkValue(at: Int) -> Double](./tickmarkvalue%28at%29.md)
  Returns the receiver’s value represented by the tick mark at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/tickmarkposition)*