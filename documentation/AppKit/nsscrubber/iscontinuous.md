# isContinuous

**Framework**: AppKit  
**Kind**: property

A Boolean value that, together with the [`mode`](nsscrubber/mode-swift.property.md) property, determines scrubber interaction style.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var isContinuous: Bool { get set }
```

#### Discussion

For details on how to choose the right [`isContinuous`](nsscrubber/iscontinuous.md) value for your app, see [`Choose a scrubber touch-interaction model`](nsscrubber#Choose-a-scrubber-touch-interaction-model.md).

## See Also

- [var scrubberLayout: NSScrubberLayout](nsscrubber/scrubberlayout.md)
  An object used to describe the layout of items within the scrubber.
- [var mode: NSScrubber.Mode](nsscrubber/mode-swift.property.md)
  A setting that determines whether interaction with the scrubber is fixed or free.
- [NSScrubber.Mode](nsscrubber/mode-swift.enum.md)
  The scrolling behavior for a scrubber.
- [var itemAlignment: NSScrubber.Alignment](nsscrubber/itemalignment.md)
  A setting that specifies the snapping behavior of items in the scrubber.
- [NSScrubber.Alignment](nsscrubber/alignment.md)
  The specified preferred alignment of items within the scrubber, when they come to rest following a user’s scrolling or paging interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/iscontinuous)*