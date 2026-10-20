# audioSessionInterrupted

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The system interrupts a participant’s audio session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
static let audioSessionInterrupted: AVCoordinatedPlaybackSuspension.Reason
```

```c
extern AVCoordinatedPlaybackSuspensionReason const AVCoordinatedPlaybackSuspensionReasonAudioSessionInterrupted;
```

## See Also

### Suspension reasons
- [static let coordinatedPlaybackNotPossible: AVCoordinatedPlaybackSuspension.Reason](./coordinatedplaybacknotpossible.md)
  It’s not possible for a participant to start or resume coordinated playback.
- [static let playingInterstitial: AVCoordinatedPlaybackSuspension.Reason](./playinginterstitial.md)
  A participant is playing content other than the primary content.
- [static let stallRecovery: AVCoordinatedPlaybackSuspension.Reason](./stallrecovery.md)
  The player object is buffering media data after a stall.
- [static let userActionRequired: AVCoordinatedPlaybackSuspension.Reason](./useractionrequired.md)
  A playback object requires user intervention to resume playback.
- [static let userIsChangingCurrentTime: AVCoordinatedPlaybackSuspension.Reason](./userischangingcurrenttime.md)
  A participant is actively changing the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybacksuspension/reason-swift.struct/audiosessioninterrupted)*