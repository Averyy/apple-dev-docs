# RCSService.Business.Suggestion

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Enumeration representing a suggestion from a business.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
enum Suggestion
```

## Topics

### Determining suggestion type
- [case action(RCSService.Business.SuggestedAction)](rcsservice/business/suggestion/action(_:).md)
  Suggested action.
- [RCSService.Business.SuggestedAction](rcsservice/business/suggestedaction.md)
  Suggested action sent by a business.
- [case reply(RCSService.Business.SuggestedReply)](rcsservice/business/suggestion/reply(_:).md)
  Suggested reply.
- [RCSService.Business.SuggestedReply](rcsservice/business/suggestedreply.md)
  Suggested reply in response to a business message.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let message: RCSMessage](rcsservice/incomingmessagenotification/message.md)
  The message contained in this notification.
- [let groupContext: RCSGroupContext?](rcsservice/incomingmessagenotification/groupcontext.md)
  The group context associated with this message.
- [struct RCSGroupContext](rcsgroupcontext.md)
  Structure containing information about a message’s group.
- [let suggestions: [RCSService.Business.Suggestion]](rcsservice/incomingmessagenotification/suggestions.md)
  An array of suggestions associated with the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/suggestion)*