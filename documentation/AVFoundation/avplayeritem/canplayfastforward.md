# canPlayFastForward

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the item can play at fast-forward rates.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
var canPlayFastForward: Bool { get }
```

#### Discussion

This property is `true` when an item can play at rates greater than `2.0`. Every item with a status of [`AVPlayerItem.Status.readyToPlay`](avplayeritem/status-swift.enum/readytoplay.md) plays at rates between `1.0` and `2.0`, inclusive, even when this property is `false`.

## See Also

- [var canPlayReverse: Bool](avplayeritem/canplayreverse.md)
  A Boolean value that indicates whether the item can play in reverse.
- [var canPlayFastReverse: Bool](avplayeritem/canplayfastreverse.md)
  A Boolean value that indicates whether the item can be quickly reversed.
- [var canPlaySlowForward: Bool](avplayeritem/canplayslowforward.md)
  A Boolean value that indicates whether the item can play slower than normal.
- [var canPlaySlowReverse: Bool](avplayeritem/canplayslowreverse.md)
  A Boolean value that indicates whether the item can play slowly backward.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/canplayfastforward)*