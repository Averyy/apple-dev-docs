# PTServiceStatus

**Framework**: Push to Talk  
**Kind**: enum  
**Role**: Enumeration

Identifies the type that indicates the status of the service.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum PTServiceStatus
```

```c
enum PTServiceStatus : NSInteger;
```

## Topics

### Statuses
- [PTServiceStatus.ready](./ptservicestatus/ready.md)
  A type that indicates the service is available for use.
- [PTServiceStatus.connecting](./ptservicestatus/connecting.md)
  A type that indicates the service is attempting to establish a connection.
- [PTServiceStatus.unavailable](./ptservicestatus/unavailable.md)
  A type that indicates the service is unavailable and needs to be re-established.
### Initializers
- [init?(rawValue: Int)](./ptservicestatus/init%28rawvalue%29.md)

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
- [enum PTTransmissionMode](./pttransmissionmode.md)
  Identifies the type of audio transmission modes.
- [enum PTChannelJoinReason](./ptchanneljoinreason.md)
  Identifies the type that indicates the join reason.
- [enum PTChannelLeaveReason](./ptchannelleavereason.md)
  Identifies the type that indicates the leave reason.
- [enum PTChannelTransmitRequestSource](./ptchanneltransmitrequestsource.md)
  Identifies the type that indicates the transmission request source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptservicestatus)*