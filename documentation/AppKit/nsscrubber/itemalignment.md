# itemAlignment

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A setting that specifies the snapping behavior of items in the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var itemAlignment: NSScrubber.Alignment { get set }
```

```objc
@property NSScrubberAlignment itemAlignment;
```

## Discussion

Set the value to something other than [`NSScrubber.Alignment.none`](./alignment/none.md) to ensure that an item is aligned with the specified position when the scrubber comes to rest.

The default value is [`NSScrubber.Alignment.none`](./alignment/none.md).

## See Also

### Changing the layout
- [var scrubberLayout: NSScrubberLayout](./scrubberlayout.md)
  An object used to describe the layout of items within the scrubber.
- [var mode: NSScrubber.Mode](./mode-swift.property.md)
  A setting that determines whether interaction with the scrubber is fixed or free.
- [NSScrubber.Mode](./mode-swift.enum.md)
  The scrolling behavior for a scrubber.
- [NSScrubber.Alignment](./alignment.md)
  The specified preferred alignment of items within the scrubber, when they come to rest following a user’s scrolling or paging interaction.
- [var isContinuous: Bool](./iscontinuous.md)
  A Boolean value that, together with the [`mode`](./mode-swift.property.md) property, determines scrubber interaction style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/itemalignment)*