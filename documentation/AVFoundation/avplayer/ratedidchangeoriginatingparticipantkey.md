# rateDidChangeOriginatingParticipantKey

**Framework**: AVFoundation  
**Kind**: property

A key to retrieve the identifier of the participant that originates the rate change.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class let rateDidChangeOriginatingParticipantKey: String
```

#### Discussion

The associated value is a UUID of a participant in the playback coordinator’s [`otherParticipants`](avplaybackcoordinator/otherparticipants.md) array.

## See Also

- [class let rateDidChangeReasonKey: String](avplayer/ratedidchangereasonkey.md)
  A key to retrieve the reason for the rate change.
- [AVPlayer.RateDidChangeReason](avplayer/ratedidchangereason.md)
  A structure that represents a rate change reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/ratedidchangeoriginatingparticipantkey)*