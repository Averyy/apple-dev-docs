# reportConversationEvent(_:for:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Role**: Instance Method

Informs the system that an event has occurred and that it needs to update the conversation if necessary.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final func reportConversationEvent(_ event: Conversation.Event, for conversation: Conversation)
```

## Parameters

- `event`: A conversation event that the system needs to process.
- `conversation`: The conversation that the event applies to.

## See Also

### Observing conversations
- [func pendingConversationActions(of: ConversationAction.Type, for: Conversation) -> [ConversationAction]](./pendingconversationactions%28of,for%29.md)
  Queries a conversation for pending actions of a specified type.
- [func reportNewIncomingConversation(uuid: UUID, update: Conversation.Update) async throws](./reportnewincomingconversation%28uuid,update%29.md)
  Informs the system that there’s a new incoming conversation, and the device should begin to ring and present the incoming Conversation UI.
- [class func reportNewIncomingVoIPPushPayload([AnyHashable : Any]) async throws](./reportnewincomingvoippushpayload%28_%29.md)
  Reports a new incoming conversation after your notification service extension decrypts a VoIP request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanager/reportconversationevent(_:for:))*