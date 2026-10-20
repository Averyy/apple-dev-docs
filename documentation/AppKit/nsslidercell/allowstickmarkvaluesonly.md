# allowsTickMarkValuesOnly

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the receiver fixes its values to those values represented by its tick marks.

**Availability**:
- macOS

## Declaration

```swift
var allowsTickMarkValuesOnly: Bool { get set }
```

```objc
@property BOOL allowsTickMarkValuesOnly;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the slider’s values are limited to those values represented by tick marks; otherwise, [`false`](../../Swift/false.md). For example, if you specify [`true`](../../Swift/true.md) for a slider that has a minimum value of 0, a maximum value of 100, and five markers, the allowable values are 0, 25, 50, 75, and 100. When users move the slider’s knob, it jumps to the tick mark nearest the pointer when the mouse button is released. Setting this property has no effect if the slider has no tick marks.

## See Also

### Managing Tick Marks
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
- [func tickMarkValue(at: Int) -> Double](./tickmarkvalue%28at%29.md)
  Returns the receiver’s value represented by the tick mark at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/allowstickmarkvaluesonly)*