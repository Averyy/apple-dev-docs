# itemAlignment

**Framework**: AppKit  
**Kind**: property

A setting that specifies the snapping behavior of items in the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
var itemAlignment: NSScrubber.Alignment { get set }
```

#### Discussion

Set the value to something other than [`NSScrubber.Alignment.none`](nsscrubber/alignment/none.md) to ensure that an item is aligned with the specified position when the scrubber comes to rest.

The default value is [`NSScrubber.Alignment.none`](nsscrubber/alignment/none.md).

## See Also

- [var scrubberLayout: NSScrubberLayout](nsscrubber/scrubberlayout.md)
  An object used to describe the layout of items within the scrubber.
- [var mode: NSScrubber.Mode](nsscrubber/mode-swift.property.md)
  A setting that determines whether interaction with the scrubber is fixed or free.
- [NSScrubber.Mode](nsscrubber/mode-swift.enum.md)
  The scrolling behavior for a scrubber.
- [NSScrubber.Alignment](nsscrubber/alignment.md)
  The specified preferred alignment of items within the scrubber, when they come to rest following a user’s scrolling or paging interaction.
- [var isContinuous: Bool](nsscrubber/iscontinuous.md)
  A Boolean value that, together with the [`mode`](nsscrubber/mode-swift.property.md) property, determines scrubber interaction style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/itemalignment)*