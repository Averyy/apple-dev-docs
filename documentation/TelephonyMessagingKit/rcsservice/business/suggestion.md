# RCSService.Business.Suggestion

**Framework**: TelephonyMessagingKit  
**Kind**: enum  
**Role**: Enumeration

Enumeration representing a suggestion from a business.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum Suggestion
```

## Topics

### Determining suggestion type
- [case action(RCSService.Business.SuggestedAction)](./suggestion/action%28_%29.md)
  Suggested action.
- [RCSService.Business.SuggestedAction](./suggestedaction.md)
  Suggested action sent by a business.
- [case reply(RCSService.Business.SuggestedReply)](./suggestion/reply%28_%29.md)
  Suggested reply.
- [RCSService.Business.SuggestedReply](./suggestedreply.md)
  Suggested reply in response to a business message.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Inspecting notification properties
- [let message: RCSMessage](../incomingmessagenotification/message.md)
  The message contained in this notification.
- [let groupContext: RCSGroupContext?](../incomingmessagenotification/groupcontext.md)
  The group context associated with this message.
- [struct RCSGroupContext](../../rcsgroupcontext.md)
  Structure containing information about a message’s group.
- [let suggestions: [RCSService.Business.Suggestion]](../incomingmessagenotification/suggestions.md)
  An array of suggestions associated with the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/suggestion)*