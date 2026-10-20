# step(byCount:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Moves the player item’s current time forward or backward by a specified number of steps.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
nonisolated
func step(byCount stepCount: Int)
```

```objc
- (void) stepByCount:(NSInteger) stepCount;
```

#### Discussion

The size of each step depends on the receiver’s enabled `AVPlayerItemTrack` objects (see [`tracks`](./tracks.md)).

## Parameters

- `stepCount`: The number of steps by which to move.

  A positive number steps forward, a negative number steps backward.

## See Also

### Stepping through media
- [var canStepForward: Bool](./canstepforward.md)
  A Boolean value that indicates whether the item supports stepping forward.
- [var canStepBackward: Bool](./canstepbackward.md)
  A Boolean value that indicates whether the item supports stepping backward.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/step(bycount:))*