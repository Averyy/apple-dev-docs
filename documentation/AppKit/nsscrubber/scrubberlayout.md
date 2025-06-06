# scrubberLayout

**Framework**: AppKit  
**Kind**: property

An object used to describe the layout of items within the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var scrubberLayout: NSScrubberLayout { get set }
```

## See Also

- [var mode: NSScrubber.Mode](nsscrubber/mode-swift.property.md)
  A setting that determines whether interaction with the scrubber is fixed or free.
- [NSScrubber.Mode](nsscrubber/mode-swift.enum.md)
  The scrolling behavior for a scrubber.
- [var itemAlignment: NSScrubber.Alignment](nsscrubber/itemalignment.md)
  A setting that specifies the snapping behavior of items in the scrubber.
- [NSScrubber.Alignment](nsscrubber/alignment.md)
  The specified preferred alignment of items within the scrubber, when they come to rest following a user’s scrolling or paging interaction.
- [var isContinuous: Bool](nsscrubber/iscontinuous.md)
  A Boolean value that, together with the [`mode`](nsscrubber/mode-swift.property.md) property, determines scrubber interaction style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/scrubberlayout)*