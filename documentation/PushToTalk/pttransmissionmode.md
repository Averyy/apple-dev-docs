# PTTransmissionMode

**Framework**: Push to Talk  
**Kind**: enum

Identifies the type of audio transmission modes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum PTTransmissionMode
```

## Topics

### Modes
- [PTTransmissionMode.fullDuplex](pttransmissionmode/fullduplex.md)
  A type that indicates a participant can simultaneously receive and transmit audio.
- [PTTransmissionMode.halfDuplex](pttransmissionmode/halfduplex.md)
  A type that indicates a participant can’t simultaneously receive and transmit audio.
- [PTTransmissionMode.listenOnly](pttransmissionmode/listenonly.md)
  A type that indicates a participant can only receive audio.
### Initializers
- [init?(rawValue: Int)](pttransmissionmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol PTChannelManagerDelegate](ptchannelmanagerdelegate.md)
  A type that represents your life cycle of a channel manager.
- [enum PTServiceStatus](ptservicestatus.md)
  Identifies the type that indicates the status of the service.
- [enum PTChannelJoinReason](ptchanneljoinreason.md)
  Identifies the type that indicates the join reason.
- [enum PTChannelLeaveReason](ptchannelleavereason.md)
  Identifies the type that indicates the leave reason.
- [enum PTChannelTransmitRequestSource](ptchanneltransmitrequestsource.md)
  Identifies the type that indicates the transmission request source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/pttransmissionmode)*