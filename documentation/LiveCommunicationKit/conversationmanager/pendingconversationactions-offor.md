# pendingConversationActions(of:for:)

**Framework**: LiveCommunicationKit  
**Kind**: method

Returns all pending `ConversationAction`s of the specified class for the specified call identifier that are incomplete.

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

An array of call actions of the specified class for the specified `Conversation`.

## Parameters

- `conversationActionClass`: The desired   subclass of actions to return.
- `conversation`: The desired   for returned actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanager/pendingconversationactions(of:for:))*