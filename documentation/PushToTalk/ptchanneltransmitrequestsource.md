# PTChannelTransmitRequestSource

**Framework**: Push to Talk  
**Kind**: enum

Identifies the type that indicates the transmission request source.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum PTChannelTransmitRequestSource
```

## Topics

### Transmission sources
- [PTChannelTransmitRequestSource.userRequest](ptchanneltransmitrequestsource/userrequest.md)
  A transmission request that indicates the user pressed the transmit button in the system user interface.
- [PTChannelTransmitRequestSource.developerRequest](ptchanneltransmitrequestsource/developerrequest.md)
  A transmission request that indicates the app calls the begin transmission method.
- [PTChannelTransmitRequestSource.handsfreeButton](ptchanneltransmitrequestsource/handsfreebutton.md)
  A transmission request that indicates a user pressed a button on a hands-free device.
- [PTChannelTransmitRequestSource.unknown](ptchanneltransmitrequestsource/unknown.md)
  A transmission request that indicates an unknown reason.
### Initializers
- [init?(rawValue: Int)](ptchanneltransmitrequestsource/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol PTChannelManagerDelegate](ptchannelmanagerdelegate.md)
  A type that represents your life cycle of a channel manager.
- [enum PTTransmissionMode](pttransmissionmode.md)
  Identifies the type of audio transmission modes.
- [enum PTServiceStatus](ptservicestatus.md)
  Identifies the type that indicates the status of the service.
- [enum PTChannelJoinReason](ptchanneljoinreason.md)
  Identifies the type that indicates the join reason.
- [enum PTChannelLeaveReason](ptchannelleavereason.md)
  Identifies the type that indicates the leave reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchanneltransmitrequestsource)*