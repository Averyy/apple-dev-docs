# RCSService.IncomingMessageNotification

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that contains information about an incoming RCS message.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct IncomingMessageNotification
```

## Topics

### Inspecting notification properties
- [let message: RCSMessage](./incomingmessagenotification/message.md)
  The message contained in this notification.
- [let groupContext: RCSGroupContext?](./incomingmessagenotification/groupcontext.md)
  The group context associated with this message.
- [struct RCSGroupContext](../rcsgroupcontext.md)
  Structure containing information about a message’s group.
- [let suggestions: [RCSService.Business.Suggestion]](./incomingmessagenotification/suggestions.md)
  An array of suggestions associated with the message.
- [RCSService.Business.Suggestion](./business/suggestion.md)
  Enumeration representing a suggestion from a business.
### Instance Properties
- [let requestedDispositions: [RCSMessage.Disposition]](./incomingmessagenotification/requesteddispositions.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Receiving messages
- [var incomingMessageNotifications: some AsyncSequence<RCSService.IncomingMessageNotification, Never>](./incomingmessagenotifications.md)
  An asynchronous sequence of incoming message notifications produced by this service.
- [struct RCSMessage](../rcsmessage.md)
  A structure that contains an RCS message’s content and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/incomingmessagenotification)*