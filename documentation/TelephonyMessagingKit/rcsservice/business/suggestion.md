# RCSService.Business.Suggestion

**Framework**: TelephonyMessagingKit  
**Kind**: enum

Enumeration representing a suggestion from a business.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
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
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/business/suggestion/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](rcsservice/business/suggestion/encode(to:).md)
  Encodes this value into the given encoder.
### Comparing suggestions
- [static func == (RCSService.Business.Suggestion, RCSService.Business.Suggestion) -> Bool](rcsservice/business/suggestion/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](rcsservice/business/suggestion/equatable-implementations.md)

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