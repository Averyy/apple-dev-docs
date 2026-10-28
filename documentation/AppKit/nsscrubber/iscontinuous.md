# isContinuous

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that, together with the [`mode`](./mode-swift.property.md) property, determines scrubber interaction style.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var isContinuous: Bool { get set }
```

```objc
@property (getter=isContinuous) BOOL continuous;
```

## Discussion

For details on how to choose the right [`isContinuous`](./iscontinuous.md) value for your app, see [Choose a scrubber touch-interaction model](../nsscrubber.md#Choose-a-scrubber-touch-interaction-model).

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
- [NSScrubber.Alignment](./alignment.md)
  The specified preferred alignment of items within the scrubber, when they come to rest following a user’s scrolling or paging interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/iscontinuous)*