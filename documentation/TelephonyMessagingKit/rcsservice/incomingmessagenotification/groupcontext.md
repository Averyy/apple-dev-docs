# groupContext

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

The group context associated with this message.

**Availability**:
- iOS 26.0+

## Declaration

```swift
let groupContext: RCSGroupContext?
```

## Discussion

This property is non-`nil` when the message is part of a group conversation.

## See Also

### Inspecting notification properties
- [let message: RCSMessage](./message.md)
  The message contained in this notification.
- [struct RCSGroupContext](../../rcsgroupcontext.md)
  Structure containing information about a message’s group.
- [let suggestions: [RCSService.Business.Suggestion]](./suggestions.md)
  An array of suggestions associated with the message.
- [RCSService.Business.Suggestion](../business/suggestion.md)
  Enumeration representing a suggestion from a business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/incomingmessagenotification/groupcontext)*