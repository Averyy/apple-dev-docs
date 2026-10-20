# NSScrubber.Mode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The scrolling behavior for a scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
enum Mode
```

```c
enum NSScrubberMode : NSInteger;
```

#### Overview

Scrolling is either *fixed* or *free*. For details on how to choose the correct scrolling mode for your app, see [Choose a scrubber touch-interaction model](../nsscrubber.md#Choose-a-scrubber-touch-interaction-model).

## Topics

### Constants
- [NSScrubber.Mode.fixed](./mode-swift.enum/fixed.md)
  A scrolling mode in which scrubber items remain fixed in place, and the item under the user’s finger is highlighted.
- [NSScrubber.Mode.free](./mode-swift.enum/free.md)
  A scrolling mode in which the scrubber scrolls as the user swipes horizontally across the scrubber.
### Initializers
- [init?(rawValue: Int)](./mode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Changing the layout
- [var scrubberLayout: NSScrubberLayout](./scrubberlayout.md)
  An object used to describe the layout of items within the scrubber.
- [var mode: NSScrubber.Mode](./mode-swift.property.md)
  A setting that determines whether interaction with the scrubber is fixed or free.
- [var itemAlignment: NSScrubber.Alignment](./itemalignment.md)
  A setting that specifies the snapping behavior of items in the scrubber.
- [NSScrubber.Alignment](./alignment.md)
  The specified preferred alignment of items within the scrubber, when they come to rest following a user’s scrolling or paging interaction.
- [var isContinuous: Bool](./iscontinuous.md)
  A Boolean value that, together with the [`mode`](./mode-swift.property.md) property, determines scrubber interaction style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/mode-swift.enum)*