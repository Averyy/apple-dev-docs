# anticipatedPlaybackRate

**Framework**: AVFoundation  
**Kind**: property

The rate at which the coordinator expects the current item to play.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var anticipatedPlaybackRate: Float { get }
```

#### Discussion

Consider this command complete after the player is ready to start playback at the indicated rate.

## See Also

- [var shouldBufferInAnticipationOfPlayback: Bool](avdelegatingplaybackcoordinatorpausecommand/shouldbufferinanticipationofplayback.md)
  A Boolean value that indicates whether the player starts buffering in preparation for a request to begin playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorpausecommand/anticipatedplaybackrate)*