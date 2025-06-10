# NSScroller.ArrowPosition

**Framework**: AppKit  
**Kind**: enum

These constants specify where the scroller’s buttons appear and are used by the [`arrowsPosition`](nsscroller/arrowsposition.md) property.

**Availability**:
- macOS 10.0+

## Declaration

```swift
enum ArrowPosition
```

## Topics

### Constants
- [NSScroller.ArrowPosition.scrollerArrowsMaxEnd](nsscroller/arrowposition/scrollerarrowsmaxend.md)
  Buttons at bottom or right. This constant has been deprecated.
- [NSScroller.ArrowPosition.scrollerArrowsMinEnd](nsscroller/arrowposition/scrollerarrowsminend.md)
  Buttons at top or left. This has been deprecated.
- [static var scrollerArrowsDefaultSetting: NSScroller.ArrowPosition](nsscroller/arrowposition/scrollerarrowsdefaultsetting.md)
  Buttons are displayed according to the system-wide appearance preferences.
- [NSScroller.ArrowPosition.scrollerArrowsNone](nsscroller/arrowposition/scrollerarrowsnone.md)
  No buttons.
### Initializers
- [init?(rawValue: UInt)](nsscroller/arrowposition/init(rawvalue:).md)

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
- [NSScroller.UsableParts](nsscroller/usableparts-swift.enum.md)
  These constants specify which parts of the scroller are visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/arrowposition)*