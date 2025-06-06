# reportNewIncomingConversation(uuid:update:)

**Framework**: LiveCommunicationKit  
**Kind**: method

Informs the system that there’s a new incoming Conversation, and the device should begin to ring and present the incoming Conversation UI.

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

- `uuid`: The   used to identify the created Conversation.
- `update`: Optional fields used to configure the Conversation to an initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanager/reportnewincomingconversation(uuid:update:))*