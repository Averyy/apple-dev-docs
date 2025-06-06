# suspensionReasons

**Framework**: AVFoundation  
**Kind**: property

The reasons a participant isn’t currently participating in coordinated playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var suspensionReasons: [AVCoordinatedPlaybackSuspension.Reason] { get }
```

#### Discussion

This value is empty if the participant’s playback isn’t in a suspended state.

## See Also

- [var identifier: UUID](avcoordinatedplaybackparticipant/identifier.md)
  A unique identifier for the participant.
- [var isReadyToPlay: Bool](avcoordinatedplaybackparticipant/isreadytoplay.md)
  A Boolean value that indicates whether the participant is ready to start coordinated playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybackparticipant/suspensionreasons)*