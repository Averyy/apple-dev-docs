# SMSService.IncomingMessageNotification

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains information about an incoming SMS message.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct IncomingMessageNotification
```

## Topics

### Inspecting notification properties
- [let message: SMSMessage](smsservice/incomingmessagenotification/message.md)
  The incoming message.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var incomingMessageNotifications: some AsyncSequence<SMSService.IncomingMessageNotification, Never>](smsservice/incomingmessagenotifications.md)
  An asynchronous sequence of incoming message notifications produced by this service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/incomingmessagenotification)*