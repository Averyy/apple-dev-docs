# NSScroller.ArrowPosition

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

These constants specify where the scroller’s buttons appear and are used by the [`arrowsPosition`](./arrowsposition.md) property.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Scroller arrows are not used anymore.

## Declaration

```swift
enum ArrowPosition
```

```c
enum NSScrollArrowPosition : NSUInteger;
```

## Topics

### Constants
- [NSScroller.ArrowPosition.scrollerArrowsMaxEnd](./arrowposition/scrollerarrowsmaxend.md)
  Buttons at bottom or right. This constant has been deprecated.
- [NSScroller.ArrowPosition.scrollerArrowsMinEnd](./arrowposition/scrollerarrowsminend.md)
  Buttons at top or left. This has been deprecated.
- [static var scrollerArrowsDefaultSetting: NSScroller.ArrowPosition](./arrowposition/scrollerarrowsdefaultsetting.md)
  Buttons are displayed according to the system-wide appearance preferences.
- [NSScroller.ArrowPosition.scrollerArrowsNone](./arrowposition/scrollerarrowsnone.md)
  No buttons.
### Initializers
- [init?(rawValue: UInt)](./arrowposition/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Deprecated enumerations
- [NSScroller.Arrow](./arrow.md)
  These constants describe the two scroller buttons and are used by [`drawArrow(_:highlight:)`](./drawarrow%28_,highlight%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/arrowposition)*