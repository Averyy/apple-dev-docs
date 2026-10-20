# AVPlayer.RateDidChangeReason

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A structure that represents a rate change reason.

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
struct RateDidChangeReason
```

```c
typedef NSString * AVPlayerRateDidChangeReason;
```

## Topics

### Initializers
- [init(rawValue: String)](./ratedidchangereason/init%28rawvalue%29.md)
  Creates a reason with a string value.
### Rate change reasons
- [static let appBackgrounded: AVPlayer.RateDidChangeReason](./ratedidchangereason/appbackgrounded.md)
  An app transitions to the background.
- [static let audioSessionInterrupted: AVPlayer.RateDidChangeReason](./ratedidchangereason/audiosessioninterrupted.md)
  The system interrupts the app’s audio session.
- [static let setRateCalled: AVPlayer.RateDidChangeReason](./ratedidchangereason/setratecalled.md)
  An app makes a call to set the player’s rate.
- [static let setRateFailed: AVPlayer.RateDidChangeReason](./ratedidchangereason/setratefailed.md)
  An attempt to change the player’s rate fails.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### User information keys
- [class let rateDidChangeOriginatingParticipantKey: String](./ratedidchangeoriginatingparticipantkey.md)
  A key to retrieve the identifier of the participant that originates the rate change.
- [class let rateDidChangeReasonKey: String](./ratedidchangereasonkey.md)
  A key to retrieve the reason for the rate change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/ratedidchangereason)*