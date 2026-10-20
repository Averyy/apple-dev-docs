# PTTransmissionMode

**Framework**: Push to Talk  
**Kind**: enum  
**Role**: Enumeration

Identifies the type of audio transmission modes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum PTTransmissionMode
```

```c
enum PTTransmissionMode : NSInteger;
```

## Topics

### Modes
- [PTTransmissionMode.fullDuplex](./pttransmissionmode/fullduplex.md)
  A type that indicates a participant can simultaneously receive and transmit audio.
- [PTTransmissionMode.halfDuplex](./pttransmissionmode/halfduplex.md)
  A type that indicates a participant can’t simultaneously receive and transmit audio.
- [PTTransmissionMode.listenOnly](./pttransmissionmode/listenonly.md)
  A type that indicates a participant can only receive audio.
### Initializers
- [init?(rawValue: Int)](./pttransmissionmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Channel management
- [protocol PTChannelManagerDelegate](./ptchannelmanagerdelegate.md)
  A type that represents your life cycle of a channel manager.
- [enum PTServiceStatus](./ptservicestatus.md)
  Identifies the type that indicates the status of the service.
- [enum PTChannelJoinReason](./ptchanneljoinreason.md)
  Identifies the type that indicates the join reason.
- [enum PTChannelLeaveReason](./ptchannelleavereason.md)
  Identifies the type that indicates the leave reason.
- [enum PTChannelTransmitRequestSource](./ptchanneltransmitrequestsource.md)
  Identifies the type that indicates the transmission request source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/pttransmissionmode)*