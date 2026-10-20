# NSScrubber.Mode.free

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

A scrolling mode in which the scrubber scrolls as the user swipes horizontally across the scrubber.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
case free
```

```c
NSScrubberModeFree
```

#### Discussion

When a user swipes horizontally across the scrubber, the scrubber scrolls. To select an item, the user must tap or press it without moving their finger horizontally.

Free-mode interaction changes depending on the value the scrubber’s [`isContinuous`](../iscontinuous.md) property. For details on how to choose the correct mode for your app, see [Choose a scrubber touch-interaction model](../../nsscrubber.md#Choose-a-scrubber-touch-interaction-model).

## See Also

### Constants
- [NSScrubber.Mode.fixed](./fixed.md)
  A scrolling mode in which scrubber items remain fixed in place, and the item under the user’s finger is highlighted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/mode-swift.enum/free)*