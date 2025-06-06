# AVPlayer.RateDidChangeReason

**Framework**: AVFoundation  
**Kind**: struct

A structure that represents a rate change reason.

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
struct RateDidChangeReason
```

## Topics

### Initializers
- [init(rawValue: String)](avplayer/ratedidchangereason/init(rawvalue:).md)
  Creates a reason with a string value.
### Rate Change Reasons
- [static let appBackgrounded: AVPlayer.RateDidChangeReason](avplayer/ratedidchangereason/appbackgrounded.md)
  An app transitions to the background.
- [static let audioSessionInterrupted: AVPlayer.RateDidChangeReason](avplayer/ratedidchangereason/audiosessioninterrupted.md)
  The system interrupts the app’s audio session.
- [static let setRateCalled: AVPlayer.RateDidChangeReason](avplayer/ratedidchangereason/setratecalled.md)
  An app makes a call to set the player’s rate.
- [static let setRateFailed: AVPlayer.RateDidChangeReason](avplayer/ratedidchangereason/setratefailed.md)
  An attempt to change the player’s rate fails.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class let rateDidChangeOriginatingParticipantKey: String](avplayer/ratedidchangeoriginatingparticipantkey.md)
  A key to retrieve the identifier of the participant that originates the rate change.
- [class let rateDidChangeReasonKey: String](avplayer/ratedidchangereasonkey.md)
  A key to retrieve the reason for the rate change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/ratedidchangereason)*