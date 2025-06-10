# MMSService.IncomingMessageNotification

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains information about an incoming MMS message.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct IncomingMessageNotification
```

## Topics

### Inspecting notification properties
- [let cellularServiceID: CellularServiceID](mmsservice/incomingmessagenotification/cellularserviceid.md)
  The cellular service identifier associated with the notification.
- [let messageID: MMSMessageID](mmsservice/incomingmessagenotification/messageid.md)
  The identifier of the incoming message.
### Comparing notifications
- [static func == (MMSService.IncomingMessageNotification, MMSService.IncomingMessageNotification) -> Bool](mmsservice/incomingmessagenotification/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](mmsservice/incomingmessagenotification/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func receiveMessage(using: CellularServiceID, messageID: MMSMessageID) async throws -> MMSMessage](mmsservice/receivemessage(using:messageid:).md)
  Retrieves an MMS message that matches the given identifiers.
- [struct CellularServiceID](cellularserviceid.md)
  An opaque identifier that represents the cellular service for which to provide operations.
- [struct MMSMessageID](mmsmessageid.md)
  A structure that represents an MMS message identifier.
- [var incomingMessageNotifications: some AsyncSequence<MMSService.IncomingMessageNotification, Never>](mmsservice/incomingmessagenotifications.md)
  An asynchronous sequence of incoming message notifications produced by the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/mmsservice/incomingmessagenotification)*