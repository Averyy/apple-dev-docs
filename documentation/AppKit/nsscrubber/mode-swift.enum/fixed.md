# NSScrubber.Mode.fixed

**Framework**: AppKit  
**Kind**: case

A scrolling mode in which scrubber items remain fixed in place, and the item under the user’s finger is highlighted.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
case fixed
```

#### Discussion

When a user swipes horizontally across the scrubber, the scrubber items remain fixed in place and the item under the user’s finger highlights. At the conclusion of the touch interaction, the last-highlighted item is selected.

For details on how to choose the correct mode for your app, see [`Choose a scrubber touch-interaction model`](nsscrubber#Choose-a-scrubber-touch-interaction-model.md).

## See Also

- [NSScrubber.Mode.free](nsscrubber/mode-swift.enum/free.md)
  A scrolling mode in which the scrubber scrolls as the user swipes horizontally across the scrubber.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscrubber/mode-swift.enum/fixed)*