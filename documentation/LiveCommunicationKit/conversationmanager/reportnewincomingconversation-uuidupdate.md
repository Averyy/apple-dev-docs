# reportNewIncomingConversation(uuid:update:)

**Framework**: LiveCommunicationKit  
**Kind**: method

Informs the system that there’s a new incoming conversation, and the device should begin to ring and present the incoming Conversation UI.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final func reportNewIncomingConversation(uuid: UUID, update: Conversation.Update) async throws
```

## Parameters

- `uuid`: The   used to identify the created conversation.
- `update`: Optional fields to configure the initial state of the conversation.

## See Also

- [func pendingConversationActions(of: ConversationAction.Type, for: Conversation) -> [ConversationAction]](conversationmanager/pendingconversationactions(of:for:).md)
  Queries a conversation for pending actions of a specified type.
- [func reportConversationEvent(Conversation.Event, for: Conversation)](conversationmanager/reportconversationevent(_:for:).md)
  Informs the system that an event has occurred and that it needs to update the conversation if necessary.
- [class func reportNewIncomingVoIPPushPayload([AnyHashable : Any]) async throws](conversationmanager/reportnewincomingvoippushpayload(_:).md)
  Reports a new incoming conversation after your notification service extension decrypts a VoIP request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanager/reportnewincomingconversation(uuid:update:))*