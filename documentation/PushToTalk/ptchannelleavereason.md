# PTChannelLeaveReason

**Framework**: Push to Talk  
**Kind**: enum

Identifies the type that indicates the leave reason.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum PTChannelLeaveReason
```

## Topics

### Leave reasons
- [PTChannelLeaveReason.userRequest](ptchannelleavereason/userrequest.md)
  A leave reason that indicates a user pressed the leave button in the user interface.
- [PTChannelLeaveReason.developerRequest](ptchannelleavereason/developerrequest.md)
  A leave reason that indicates the app calls the leave channel method.
- [PTChannelLeaveReason.systemPolicy](ptchannelleavereason/systempolicy.md)
  A leave reason that indicates a new device restriction is in effect.
- [PTChannelLeaveReason.unknown](ptchannelleavereason/unknown.md)
  A leave reason that indicates an unknown reason.
### Initializers
- [init?(rawValue: Int)](ptchannelleavereason/init(rawvalue:).md)

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
- [enum PTTransmissionMode](pttransmissionmode.md)
  Identifies the type of audio transmission modes.
- [enum PTServiceStatus](ptservicestatus.md)
  Identifies the type that indicates the status of the service.
- [enum PTChannelJoinReason](ptchanneljoinreason.md)
  Identifies the type that indicates the join reason.
- [enum PTChannelTransmitRequestSource](ptchanneltransmitrequestsource.md)
  Identifies the type that indicates the transmission request source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelleavereason)*