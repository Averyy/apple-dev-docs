# reportNewIncomingVoIPPushPayload(_:)

**Framework**: LiveCommunicationKit  
**Kind**: method

Reports a new incoming conversation after your notification service extension decrypts a VoIP request.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final class func reportNewIncomingVoIPPushPayload(_ payload: [AnyHashable : Any]) async throws
```

#### Discussion

> **Note**: When the system disallows a conversation, an error is thrown that contains information about why it disallowed the conversation.

## Parameters

- `payload`: A dictionary containing additional data about the incoming conversation. All keys and values in the dictionary must implement the   protocol.

## See Also

- [func pendingConversationActions(of: ConversationAction.Type, for: Conversation) -> [ConversationAction]](conversationmanager/pendingconversationactions(of:for:).md)
  Queries a conversation for pending actions of a specified type.
- [func reportConversationEvent(Conversation.Event, for: Conversation)](conversationmanager/reportconversationevent(_:for:).md)
  Informs the system that an event has occurred and that it needs to update the conversation if necessary.
- [func reportNewIncomingConversation(uuid: UUID, update: Conversation.Update) async throws](conversationmanager/reportnewincomingconversation(uuid:update:).md)
  Informs the system that there’s a new incoming conversation, and the device should begin to ring and present the incoming Conversation UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanager/reportnewincomingvoippushpayload(_:))*