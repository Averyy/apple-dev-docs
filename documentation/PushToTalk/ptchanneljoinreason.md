# PTChannelJoinReason

**Framework**: Push to Talk  
**Kind**: enum  
**Role**: Enumeration

Identifies the type that indicates the join reason.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum PTChannelJoinReason
```

```c
enum PTChannelJoinReason : NSInteger;
```

## Topics

### Join reasons
- [PTChannelJoinReason.developerRequest](./ptchanneljoinreason/developerrequest.md)
  A join reason that indicates the app calls the join channel method while in the foreground.
- [PTChannelJoinReason.channelRestoration](./ptchanneljoinreason/channelrestoration.md)
  A join reason that indicates the app rejoined a channel through channel restoration.
### Initializers
- [init?(rawValue: Int)](./ptchanneljoinreason/init%28rawvalue%29.md)

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
- [enum PTServiceStatus](./ptservicestatus.md)
  Identifies the type that indicates the status of the service.
- [enum PTChannelLeaveReason](./ptchannelleavereason.md)
  Identifies the type that indicates the leave reason.
- [enum PTChannelTransmitRequestSource](./ptchanneltransmitrequestsource.md)
  Identifies the type that indicates the transmission request source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchanneljoinreason)*