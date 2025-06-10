# NSScrubber.Mode

**Framework**: AppKit  
**Kind**: enum

The scrolling behavior for a scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
enum Mode
```

#### Overview

Scrolling is either  or . For details on how to choose the correct scrolling mode for your app, see [`Choose a scrubber touch-interaction model`](nsscrubber#Choose-a-scrubber-touch-interaction-model.md).

## Topics

### Constants
- [NSScrubber.Mode.fixed](nsscrubber/mode-swift.enum/fixed.md)
  A scrolling mode in which scrubber items remain fixed in place, and the item under the user’s finger is highlighted.
- [NSScrubber.Mode.free](nsscrubber/mode-swift.enum/free.md)
  A scrolling mode in which the scrubber scrolls as the user swipes horizontally across the scrubber.
### Initializers
- [init?(rawValue: Int)](nsscrubber/mode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var scrubberLayout: NSScrubberLayout](nsscrubber/scrubberlayout.md)
  An object used to describe the layout of items within the scrubber.
- [var mode: NSScrubber.Mode](nsscrubber/mode-swift.property.md)
  A setting that determines whether interaction with the scrubber is fixed or free.
- [var itemAlignment: NSScrubber.Alignment](nsscrubber/itemalignment.md)
  A setting that specifies the snapping behavior of items in the scrubber.
- [NSScrubber.Alignment](nsscrubber/alignment.md)
  The specified preferred alignment of items within the scrubber, when they come to rest following a user’s scrolling or paging interaction.
- [var isContinuous: Bool](nsscrubber/iscontinuous.md)
  A Boolean value that, together with the [`mode`](nsscrubber/mode-swift.property.md) property, determines scrubber interaction style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/mode-swift.enum)*