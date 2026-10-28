# mode

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A setting that determines whether interaction with the scrubber is fixed or free.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var mode: NSScrubber.Mode { get set }
```

```objc
@property NSScrubberMode mode;
```

## Discussion

When set to [`NSScrubber.Mode.fixed`](./mode-swift.enum/fixed.md), the scrubber’s content doesn’t scroll as the user pans. Instead, the element under the user’s finger is highlighted. The highlighted item becomes selected when the user completes the pan gesture. The default value is [`NSScrubber.Mode.fixed`](./mode-swift.enum/fixed.md).

When [`mode`](./mode-swift.property.md) is set to [`NSScrubber.Mode.free`](./mode-swift.enum/free.md), panning over the scrubber scrolls the scrubber’s content. A user selects items by tapping on them.

## See Also

### Changing the layout
- [var scrubberLayout: NSScrubberLayout](./scrubberlayout.md)
  An object used to describe the layout of items within the scrubber.
- [NSScrubber.Mode](./mode-swift.enum.md)
  The scrolling behavior for a scrubber.
- [var itemAlignment: NSScrubber.Alignment](./itemalignment.md)
  A setting that specifies the snapping behavior of items in the scrubber.
- [NSScrubber.Alignment](./alignment.md)
  The specified preferred alignment of items within the scrubber, when they come to rest following a user’s scrolling or paging interaction.
- [var isContinuous: Bool](./iscontinuous.md)
  A Boolean value that, together with the [`mode`](./mode-swift.property.md) property, determines scrubber interaction style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/mode-swift.property)*