# RCSService.IncomingMessageNotification

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains information about an incoming RCS message.

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
- [let message: RCSMessage](rcsservice/incomingmessagenotification/message.md)
  The message contained in this notification.
- [let groupContext: RCSGroupContext?](rcsservice/incomingmessagenotification/groupcontext.md)
  The group context associated with this message.
- [struct RCSGroupContext](rcsgroupcontext.md)
  Structure containing information about a message’s group.
- [let suggestions: [RCSService.Business.Suggestion]](rcsservice/incomingmessagenotification/suggestions.md)
  An array of suggestions associated with the message.
- [RCSService.Business.Suggestion](rcsservice/business/suggestion.md)
  Enumeration representing a suggestion from a business.
### Comparing notifications
- [static func == (RCSService.IncomingMessageNotification, RCSService.IncomingMessageNotification) -> Bool](rcsservice/incomingmessagenotification/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](rcsservice/incomingmessagenotification/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var incomingMessageNotifications: some AsyncSequence<RCSService.IncomingMessageNotification, Never>](rcsservice/incomingmessagenotifications.md)
  An asynchronous sequence of incoming message notifications produced by this service.
- [struct RCSMessage](rcsmessage.md)
  A structure that contains an RCS message’s content and metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/incomingmessagenotification)*