# NSScroller.Style

**Framework**: AppKit  
**Kind**: enum

Constants to specify the scroller style.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum Style
```

## Topics

### Constants
- [NSScroller.Style.legacy](nsscroller/style/legacy.md)
  Specifies legacy-style scrollers as prior to macOS 10.7.
- [NSScroller.Style.overlay](nsscroller/style/overlay.md)
  Specifies overlay-style scrollers in macOS 10.7 and later.
### Initializers
- [init?(rawValue: Int)](nsscroller/style/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSScroller.KnobStyle](nsscroller/knobstyle-swift.enum.md)
  Specify different knob styles.
- [NSScroller.Part](nsscroller/part.md)
  These constants specify the different parts of the scroller:
- [NSScroller.Arrow](nsscroller/arrow.md)
  These constants describe the two scroller buttons and are used by [`drawArrow(_:highlight:)`](nsscroller/drawarrow(_:highlight:).md).
- [NSScroller.ArrowPosition](nsscroller/arrowposition.md)
  These constants specify where the scroller’s buttons appear and are used by the [`arrowsPosition`](nsscroller/arrowsposition.md) property.
- [NSScroller.UsableParts](nsscroller/usableparts-swift.enum.md)
  These constants specify which parts of the scroller are visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/style)*