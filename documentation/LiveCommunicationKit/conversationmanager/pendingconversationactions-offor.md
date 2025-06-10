# pendingConversationActions(of:for:)

**Framework**: LiveCommunicationKit  
**Kind**: method

Queries a conversation for pending actions of a specified type.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final func pendingConversationActions(of conversationActionClass: ConversationAction.Type, for conversation: Conversation) -> [ConversationAction]
```

#### Return Value

An array of a conversation’s pending conversation actions of the specified type.

## Parameters

- `conversationActionClass`: The type of action to query.
- `conversation`: The conversation to query.

## See Also

- [func reportConversationEvent(Conversation.Event, for: Conversation)](conversationmanager/reportconversationevent(_:for:).md)
  Informs the system that an event has occurred and that it needs to update the conversation if necessary.
- [func reportNewIncomingConversation(uuid: UUID, update: Conversation.Update) async throws](conversationmanager/reportnewincomingconversation(uuid:update:).md)
  Informs the system that there’s a new incoming conversation, and the device should begin to ring and present the incoming Conversation UI.
- [class func reportNewIncomingVoIPPushPayload([AnyHashable : Any]) async throws](conversationmanager/reportnewincomingvoippushpayload(_:).md)
  Reports a new incoming conversation after your notification service extension decrypts a VoIP request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanager/pendingconversationactions(of:for:))*