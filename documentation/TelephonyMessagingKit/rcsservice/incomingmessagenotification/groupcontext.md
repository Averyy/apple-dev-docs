# groupContext

**Framework**: TelephonyMessagingKit  
**Kind**: property

The group context associated with this message.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
let groupContext: RCSGroupContext?
```

#### Discussion

This property is non-`nil` when the message is part of a group conversation.

## See Also

- [let message: RCSMessage](rcsservice/incomingmessagenotification/message.md)
  The message contained in this notification.
- [struct RCSGroupContext](rcsgroupcontext.md)
  Structure containing information about a message’s group.
- [let suggestions: [RCSService.Business.Suggestion]](rcsservice/incomingmessagenotification/suggestions.md)
  An array of suggestions associated with the message.
- [RCSService.Business.Suggestion](rcsservice/business/suggestion.md)
  Enumeration representing a suggestion from a business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/incomingmessagenotification/groupcontext)*