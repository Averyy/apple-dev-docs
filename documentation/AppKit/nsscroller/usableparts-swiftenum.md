# NSScroller.UsableParts

**Framework**: AppKit  
**Kind**: enum

These constants specify which parts of the scroller are visible.

**Availability**:
- macOS ?+

## Declaration

```swift
enum UsableParts
```

## Topics

### Constants
- [NSScroller.UsableParts.noScrollerParts](nsscroller/usableparts-swift.enum/noscrollerparts.md)
  Specifies that the scroller has neither a knob nor scroll buttons, only the knob slot.
- [NSScroller.UsableParts.onlyScrollerArrows](nsscroller/usableparts-swift.enum/onlyscrollerarrows.md)
  Specifies that the scroller has only scroll buttons, no knob.
- [NSScroller.UsableParts.allScrollerParts](nsscroller/usableparts-swift.enum/allscrollerparts.md)
  Specifies that the scroller has at least a knob, possibly also scroll buttons.
### Initializers
- [init?(rawValue: UInt)](nsscroller/usableparts-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSScroller.Style](nsscroller/style.md)
  Constants to specify the scroller style.
- [NSScroller.KnobStyle](nsscroller/knobstyle-swift.enum.md)
  Specify different knob styles.
- [NSScroller.Part](nsscroller/part.md)
  These constants specify the different parts of the scroller:
- [NSScroller.Arrow](nsscroller/arrow.md)
  These constants describe the two scroller buttons and are used by [`drawArrow(_:highlight:)`](nsscroller/drawarrow(_:highlight:).md).
- [NSScroller.ArrowPosition](nsscroller/arrowposition.md)
  These constants specify where the scroller’s buttons appear and are used by the [`arrowsPosition`](nsscroller/arrowsposition.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/usableparts-swift.enum)*