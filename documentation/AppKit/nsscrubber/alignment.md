# NSScrubber.Alignment

**Framework**: AppKit  
**Kind**: enum

The specified preferred alignment of items within the scrubber, when they come to rest following a user’s scrolling or paging interaction.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
enum Alignment
```

#### Overview

For details on how to choose the right alignment option for your app, see [`Choose a scrubber touch-interaction model`](nsscrubber#Choose-a-scrubber-touch-interaction-model.md).

## Topics

### Constants
- [NSScrubber.Alignment.center](nsscrubber/alignment/center.md)
  Center alignment of items within the scrubber.
- [NSScrubber.Alignment.leading](nsscrubber/alignment/leading.md)
  Leading alignment of items within the scrubber.
- [NSScrubber.Alignment.none](nsscrubber/alignment/none.md)
  No preference for item alignment.
- [NSScrubber.Alignment.trailing](nsscrubber/alignment/trailing.md)
  Trailing alignment of items within the scrubber.
### Initializers
- [init?(rawValue: Int)](nsscrubber/alignment/init(rawvalue:).md)

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
- [NSScrubber.Mode](nsscrubber/mode-swift.enum.md)
  The scrolling behavior for a scrubber.
- [var itemAlignment: NSScrubber.Alignment](nsscrubber/itemalignment.md)
  A setting that specifies the snapping behavior of items in the scrubber.
- [var isContinuous: Bool](nsscrubber/iscontinuous.md)
  A Boolean value that, together with the [`mode`](nsscrubber/mode-swift.property.md) property, determines scrubber interaction style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/alignment)*