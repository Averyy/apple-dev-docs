# NSScrubber.Alignment

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The specified preferred alignment of items within the scrubber, when they come to rest following a user’s scrolling or paging interaction.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
enum Alignment
```

```c
enum NSScrubberAlignment : NSInteger;
```

#### Overview

For details on how to choose the right alignment option for your app, see [Choose a scrubber touch-interaction model](../nsscrubber.md#Choose-a-scrubber-touch-interaction-model).

## Topics

### Constants
- [NSScrubber.Alignment.center](./alignment/center.md)
  Center alignment of items within the scrubber.
- [NSScrubber.Alignment.leading](./alignment/leading.md)
  Leading alignment of items within the scrubber.
- [NSScrubber.Alignment.none](./alignment/none.md)
  No preference for item alignment.
- [NSScrubber.Alignment.trailing](./alignment/trailing.md)
  Trailing alignment of items within the scrubber.
### Initializers
- [init?(rawValue: Int)](./alignment/init%28rawvalue%29.md)

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
- [NSScrubber.Mode](./mode-swift.enum.md)
  The scrolling behavior for a scrubber.
- [var itemAlignment: NSScrubber.Alignment](./itemalignment.md)
  A setting that specifies the snapping behavior of items in the scrubber.
- [var isContinuous: Bool](./iscontinuous.md)
  A Boolean value that, together with the [`mode`](./mode-swift.property.md) property, determines scrubber interaction style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/alignment)*