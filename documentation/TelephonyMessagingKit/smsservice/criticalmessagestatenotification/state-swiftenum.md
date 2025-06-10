# SMSService.CriticalMessageStateNotification.State

**Framework**: TelephonyMessagingKit  
**Kind**: enum

An enumeration of possible states of a critical message.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
enum State
```

## Topics

### Inspecting message states
- [SMSService.CriticalMessageStateNotification.State.sent](smsservice/criticalmessagestatenotification/state-swift.enum/sent.md)
  The service sent the message successfully.
### Hashing
- [func hash(into: inout Hasher)](smsservice/criticalmessagestatenotification/state-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](smsservice/criticalmessagestatenotification/state-swift.enum/hashvalue.md)
  The hash value.
### Comparing states
- [static func == (SMSService.CriticalMessageStateNotification.State, SMSService.CriticalMessageStateNotification.State) -> Bool](smsservice/criticalmessagestatenotification/state-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](smsservice/criticalmessagestatenotification/state-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let cellularServiceID: CellularServiceID](smsservice/criticalmessagestatenotification/cellularserviceid.md)
  The cellular service identifier associated with the notification.
- [let messageID: SMSMessageID](smsservice/criticalmessagestatenotification/messageid.md)
  The identifier of the critical message.
- [let state: SMSService.CriticalMessageStateNotification.State](smsservice/criticalmessagestatenotification/state-swift.property.md)
  The state of the critical message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/criticalmessagestatenotification/state-swift.enum)*