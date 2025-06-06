# stallRecovery

**Framework**: AVFoundation  
**Kind**: property

The player object is buffering media data after a stall.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static let stallRecovery: AVCoordinatedPlaybackSuspension.Reason
```

## See Also

- [static let audioSessionInterrupted: AVCoordinatedPlaybackSuspension.Reason](avcoordinatedplaybacksuspension/reason-swift.struct/audiosessioninterrupted.md)
  The system interrupts a participant’s audio session.
- [static let coordinatedPlaybackNotPossible: AVCoordinatedPlaybackSuspension.Reason](avcoordinatedplaybacksuspension/reason-swift.struct/coordinatedplaybacknotpossible.md)
  It’s not possible for a participant to start or resume coordinated playback.
- [static let playingInterstitial: AVCoordinatedPlaybackSuspension.Reason](avcoordinatedplaybacksuspension/reason-swift.struct/playinginterstitial.md)
  A participant is playing content other than the primary content.
- [static let userActionRequired: AVCoordinatedPlaybackSuspension.Reason](avcoordinatedplaybacksuspension/reason-swift.struct/useractionrequired.md)
  A playback object requires user intervention to resume playback.
- [static let userIsChangingCurrentTime: AVCoordinatedPlaybackSuspension.Reason](avcoordinatedplaybacksuspension/reason-swift.struct/userischangingcurrenttime.md)
  A participant is actively changing the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybacksuspension/reason-swift.struct/stallrecovery)*