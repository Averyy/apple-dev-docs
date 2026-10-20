# MMSService.IncomingMessageNotification

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that contains information about an incoming MMS message.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct IncomingMessageNotification
```

## Topics

### Inspecting notification properties
- [var message: MMSMessage](./incomingmessagenotification/message.md)
  The incoming message.
### Deprecated properties
- [var cellularServiceID: CellularServiceID](./incomingmessagenotification/cellularserviceid.md)
  The cellular service identifier associated with the notification.
- [var messageID: MMSMessageID](./incomingmessagenotification/messageid.md)
  The identifier of the incoming message.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Receiving messages
- [struct CellularServiceID](../cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [struct MMSMessageID](../mmsmessageid.md)
  A structure that represents an MMS message identifier.
- [var incomingMessageNotifications: some AsyncSequence<MMSService.IncomingMessageNotification, Never>](./incomingmessagenotifications.md)
  An asynchronous sequence of incoming message notifications produced by the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/incomingmessagenotification)*