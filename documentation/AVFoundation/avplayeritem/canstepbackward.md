# canStepBackward

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) BOOL canStepBackward;
```

## Discussion

Once the item becomes ready to play, the value of this property does not change. This behavior applies even when boundary conditions, such as when the item’s current time is [`zero`](../../CoreMedia/cmtime/zero.md), have been reached.

## See Also

### Stepping through media
- [var canStepForward: Bool](./canstepforward.md)
  A Boolean value that indicates whether the item supports stepping forward.
- [func step(byCount: Int)](./step%28bycount%29.md)
  Moves the player item’s current time forward or backward by a specified number of steps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/canstepbackward)*