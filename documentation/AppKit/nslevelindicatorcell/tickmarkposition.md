# tickMarkPosition

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The placement of tick marks on the level indicator control.

**Availability**:
- macOS

## Declaration

```swift
var tickMarkPosition: NSSlider.TickMarkPosition { get set }
```

```objc
@property NSTickMarkPosition tickMarkPosition;
```

#### Discussion

Use this property to set the position where the control draws tick marks. Regardless of the value in this property, tick marks are not drawn if the value in the [`numberOfTickMarks`](./numberoftickmarks.md) property is `0`.

The default value of this property is [`NSTickMarkBelow`](../nstickmarkbelow.md), which also corresponds to the value [`NSTickMarkLeft`](../nstickmarkleft.md) for vertically oriented level indicators.

## See Also

### Managing Tick Marks
- [var numberOfTickMarks: Int](./numberoftickmarks.md)
  The number of tick marks displayed by the control.
- [var numberOfMajorTickMarks: Int](./numberofmajortickmarks.md)
  The number of major tick marks displayed by the control.
- [func tickMarkValue(at: Int) -> Double](./tickmarkvalue%28at%29.md)
  Returns the receiver’s value represented by the tick mark at index (the minimum-value tick mark has an index of 0).
- [func rectOfTickMark(at: Int) -> NSRect](./rectoftickmark%28at%29.md)
  Returns the bounding rectangle of the tick mark identified by `index` (the minimum-value tick mark is at index 0).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicatorcell/tickmarkposition)*