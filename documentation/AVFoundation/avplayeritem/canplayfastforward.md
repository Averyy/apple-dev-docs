# canPlayFastForward

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the item can be fast forwarded.

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

An item can be fast forwarded if its rate can be greater than `1.0`.

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