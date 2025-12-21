# rateDidChangeNotification

**Framework**: AVFoundation  
**Kind**: property

A notification that a player posts when its rate changes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class let rateDidChangeNotification: NSNotification.Name
```

## Mentions

- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md)

#### Discussion

Observing this notification is similar to key-value observing the rate property, except the notification provides additional information about the rate change in the user information dictionary.

## Topics

### User information keys
- [class let rateDidChangeOriginatingParticipantKey: String](avplayer/ratedidchangeoriginatingparticipantkey.md)
  A key to retrieve the identifier of the participant that originates the rate change.
- [class let rateDidChangeReasonKey: String](avplayer/ratedidchangereasonkey.md)
  A key to retrieve the reason for the rate change.
- [AVPlayer.RateDidChangeReason](avplayer/ratedidchangereason.md)
  A structure that represents a rate change reason.

## See Also

- [var defaultRate: Float](avplayer/defaultrate.md)
  A default rate at which to begin playback.
- [func play()](avplayer/play.md)
  Begins playback of the current item.
- [func pause()](avplayer/pause.md)
  Pauses playback of the current item.
- [var rate: Float](avplayer/rate.md)
  The current playback rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/ratedidchangenotification)*