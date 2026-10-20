# NSScroller.Arrow

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

These constants describe the two scroller buttons and are used by [`drawArrow(_:highlight:)`](./drawarrow%28_,highlight%29.md).

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Scroller arrows are not used anymore.

## Declaration

```swift
enum Arrow
```

```c
enum NSScrollerArrow : NSUInteger;
```

## Topics

### Constants
- [NSScroller.Arrow.incrementArrow](./arrow/incrementarrow.md)
  The down or right scroll button.
- [NSScroller.Arrow.decrementArrow](./arrow/decrementarrow.md)
  The up or left scroll button.
### Initializers
- [init?(rawValue: UInt)](./arrow/init%28rawvalue%29.md)

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
- [NSScroller.ArrowPosition](./arrowposition.md)
  These constants specify where the scroller’s buttons appear and are used by the [`arrowsPosition`](./arrowsposition.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscroller/arrow)*