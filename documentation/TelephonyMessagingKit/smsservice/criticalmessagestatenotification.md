# SMSService.CriticalMessageStateNotification

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains information about a critical SMS message.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct CriticalMessageStateNotification
```

## Topics

### Accessing message properties
- [let cellularServiceID: CellularServiceID](smsservice/criticalmessagestatenotification/cellularserviceid.md)
  The cellular service identifier associated with the notification.
- [let messageID: SMSMessageID](smsservice/criticalmessagestatenotification/messageid.md)
  The identifier of the critical message.
- [let state: SMSService.CriticalMessageStateNotification.State](smsservice/criticalmessagestatenotification/state-swift.property.md)
  The state of the critical message.
- [SMSService.CriticalMessageStateNotification.State](smsservice/criticalmessagestatenotification/state-swift.enum.md)
  An enumeration of possible states of a critical message.
### Comparing notifications
- [static func == (SMSService.CriticalMessageStateNotification, SMSService.CriticalMessageStateNotification) -> Bool](smsservice/criticalmessagestatenotification/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](smsservice/criticalmessagestatenotification/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var criticalMessageStateNotifications: some AsyncSequence<SMSService.CriticalMessageStateNotification, Never>](smsservice/criticalmessagestatenotifications.md)
  An asynchronous sequence of critical message state notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/criticalmessagestatenotification)*