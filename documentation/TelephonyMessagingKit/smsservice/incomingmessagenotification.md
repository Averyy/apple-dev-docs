# SMSService.IncomingMessageNotification

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that contains information about an incoming SMS message.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct IncomingMessageNotification
```

## Topics

### Inspecting notification properties
- [let message: SMSMessage](./incomingmessagenotification/message.md)
  The incoming message.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Receiving messages
- [var incomingMessageNotifications: some AsyncSequence<SMSService.IncomingMessageNotification, Never>](./incomingmessagenotifications.md)
  An asynchronous sequence of incoming message notifications produced by this service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsservice/incomingmessagenotification)*