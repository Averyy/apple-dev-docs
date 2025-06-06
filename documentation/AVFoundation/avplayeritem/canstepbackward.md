# canStepBackward

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the item supports stepping backward.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
var canStepBackward: Bool { get }
```

#### Discussion

Once the item becomes ready to play, the value of this property does not change. This behavior applies even when boundary conditions, such as when the item’s current time is [`zero`](https://developer.apple.com/documentation/CoreMedia/CMTime/zero), have been reached.

## See Also

- [var canStepForward: Bool](avplayeritem/canstepforward.md)
  A Boolean value that indicates whether the item supports stepping forward.
- [func step(byCount: Int)](avplayeritem/step(bycount:).md)
  Moves the player item’s current time forward or backward by a specified number of steps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/canstepbackward)*