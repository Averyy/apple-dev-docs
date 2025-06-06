# step(byCount:)

**Framework**: AVFoundation  
**Kind**: method

Moves the player item’s current time forward or backward by a specified number of steps.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
nonisolated
func step(byCount stepCount: Int)
```

#### Discussion

The size of each step depends on the receiver’s enabled `AVPlayerItemTrack` objects (see [`tracks`](avplayeritem/tracks.md)).

## Parameters

- `stepCount`: A positive number steps forward, a negative number steps backward.

## See Also

- [var canStepForward: Bool](avplayeritem/canstepforward.md)
  A Boolean value that indicates whether the item supports stepping forward.
- [var canStepBackward: Bool](avplayeritem/canstepbackward.md)
  A Boolean value that indicates whether the item supports stepping backward.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/step(bycount:))*