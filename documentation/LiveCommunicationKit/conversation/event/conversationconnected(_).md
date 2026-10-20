# Conversation.Event.conversationConnected(_:)

**Framework**: LiveCommunicationKit  
**Kind**: case  
**Role**: Case

Informs that system that conversation successfully connected at a point in time.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
case conversationConnected(Date)
```

## See Also

- [case conversationEnded(Date, Conversation.EndedReason)](./conversationended%28_,_%29.md)
  Informs that system that a conversation ended at a point in time with a reason.
- [Conversation.Event.conversationStartedConnecting(_:)](./conversationstartedconnecting%28_%29.md)
  Informs the system that a conversation has started to connect participants at a point in time.
- [case conversationUpdated(Conversation.Update)](./conversationupdated%28_%29.md)
  Updates a conversation’s attributes and capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/event/conversationconnected(_:))*