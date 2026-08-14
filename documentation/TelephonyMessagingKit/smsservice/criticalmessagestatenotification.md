# SMSService.CriticalMessageStateNotification

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains information about a critical SMS message.

**Availability**:
- iOS 26.0+

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

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var criticalMessageStateNotifications: some AsyncSequence<SMSService.CriticalMessageStateNotification, Never>](smsservice/criticalmessagestatenotifications.md)
  An asynchronous sequence of critical message state notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/criticalmessagestatenotification)*