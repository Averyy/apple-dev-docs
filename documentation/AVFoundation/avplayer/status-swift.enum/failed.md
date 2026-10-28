# AVPlayer.Status.failed

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

A value that indicates the player can no longer play media due to an error.

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
case failed
```

```c
AVPlayerStatusFailed
```

## Discussion

Inspect the value of the player’s [`error`](../error.md) property to determine the details of the failure.

## See Also

### Status values
- [AVPlayer.Status.unknown](./unknown.md)
  A value that indicates a player hasn’t attempted to load media for playback.
- [AVPlayer.Status.readyToPlay](./readytoplay.md)
  A value that indicates the player is ready to media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/status-swift.enum/failed)*