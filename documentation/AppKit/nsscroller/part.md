# NSScroller.Part

**Framework**: AppKit  
**Kind**: enum

These constants specify the different parts of the scroller:

**Availability**:
- macOS ?+

## Declaration

```swift
enum Part
```

## Topics

### Constants
- [NSScroller.Part.knob](nsscroller/part/knob.md)
  Directly to the scroller’s value, as given by [`floatValue`](nscontrol/floatvalue.md).
- [NSScroller.Part.knobSlot](nsscroller/part/knobslot.md)
  Directly to the scroller’s value, as given by [`floatValue`](nscontrol/floatvalue.md).
- [NSScroller.Part.decrementLine](nsscroller/part/decrementline.md)
  Up or left by a small amount.
- [NSScroller.Part.decrementPage](nsscroller/part/decrementpage.md)
  Up or left by a large amount.
- [NSScroller.Part.incrementLine](nsscroller/part/incrementline.md)
  Down or right by a small amount.
- [NSScroller.Part.incrementPage](nsscroller/part/incrementpage.md)
  Down or right by a large amount.
- [NSScroller.Part.noPart](nsscroller/part/nopart.md)
  Don’t scroll at all.
### Initializers
- [init?(rawValue: UInt)](nsscroller/part/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSScroller.Style](nsscroller/style.md)
  Constants to specify the scroller style.
- [NSScroller.KnobStyle](nsscroller/knobstyle-swift.enum.md)
  Specify different knob styles.
- [NSScroller.Arrow](nsscroller/arrow.md)
  These constants describe the two scroller buttons and are used by [`drawArrow(_:highlight:)`](nsscroller/drawarrow(_:highlight:).md).
- [NSScroller.ArrowPosition](nsscroller/arrowposition.md)
  These constants specify where the scroller’s buttons appear and are used by the [`arrowsPosition`](nsscroller/arrowsposition.md) property.
- [NSScroller.UsableParts](nsscroller/usableparts-swift.enum.md)
  These constants specify which parts of the scroller are visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/part)*