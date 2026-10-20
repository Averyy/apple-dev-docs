# SMSService.CriticalMessageStateNotification

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that contains information about a critical SMS message.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct CriticalMessageStateNotification
```

## Topics

### Accessing message properties
- [let cellularServiceID: CellularServiceID](./criticalmessagestatenotification/cellularserviceid.md)
  The cellular service identifier associated with the notification.
- [let messageID: SMSMessageID](./criticalmessagestatenotification/messageid.md)
  The identifier of the critical message.
- [let state: SMSService.CriticalMessageStateNotification.State](./criticalmessagestatenotification/state-swift.property.md)
  The state of the critical message.
- [SMSService.CriticalMessageStateNotification.State](./criticalmessagestatenotification/state-swift.enum.md)
  An enumeration of possible states of a critical message.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling critical state changes
- [var criticalMessageStateNotifications: some AsyncSequence<SMSService.CriticalMessageStateNotification, Never>](./criticalmessagestatenotifications.md)
  An asynchronous sequence of critical message state notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/criticalmessagestatenotification)*