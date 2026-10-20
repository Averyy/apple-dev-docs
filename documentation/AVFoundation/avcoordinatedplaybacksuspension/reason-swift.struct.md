# AVCoordinatedPlaybackSuspension.Reason

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

Constants that identify playback suspension reasons.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Reason
```

```c
typedef NSString * AVCoordinatedPlaybackSuspensionReason;
```

## Topics

### Suspension reasons
- [static let audioSessionInterrupted: AVCoordinatedPlaybackSuspension.Reason](./reason-swift.struct/audiosessioninterrupted.md)
  The system interrupts a participant’s audio session.
- [static let coordinatedPlaybackNotPossible: AVCoordinatedPlaybackSuspension.Reason](./reason-swift.struct/coordinatedplaybacknotpossible.md)
  It’s not possible for a participant to start or resume coordinated playback.
- [static let playingInterstitial: AVCoordinatedPlaybackSuspension.Reason](./reason-swift.struct/playinginterstitial.md)
  A participant is playing content other than the primary content.
- [static let stallRecovery: AVCoordinatedPlaybackSuspension.Reason](./reason-swift.struct/stallrecovery.md)
  The player object is buffering media data after a stall.
- [static let userActionRequired: AVCoordinatedPlaybackSuspension.Reason](./reason-swift.struct/useractionrequired.md)
  A playback object requires user intervention to resume playback.
- [static let userIsChangingCurrentTime: AVCoordinatedPlaybackSuspension.Reason](./reason-swift.struct/userischangingcurrenttime.md)
  A participant is actively changing the current time.
### Initializers
- [init(String)](./reason-swift.struct/init%28_%29.md)
  Creates a suspension with a string.
- [init(rawValue: String)](./reason-swift.struct/init%28rawvalue%29.md)
  Creates a suspension with a raw string value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting a suspension
- [var beginDate: Date](./begindate.md)
  The time the suspension begins.
- [var reason: AVCoordinatedPlaybackSuspension.Reason](./reason-swift.property.md)
  The reason for the suspension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybacksuspension/reason-swift.struct)*