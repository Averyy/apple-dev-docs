# Conversation.Event.conversationEnded(_:_:)

**Framework**: LiveCommunicationKit  
**Kind**: case

Informs that system that a conversation ended at a point in time with a reason.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
case conversationEnded(Date, Conversation.EndedReason)
```

## See Also

- [Conversation.Event.conversationConnected(_:)](conversation/event/conversationconnected(_:).md)
  Informs that system that conversation successfully connected at a point in time.
- [Conversation.Event.conversationStartedConnecting(_:)](conversation/event/conversationstartedconnecting(_:).md)
  Informs the system that a conversation has started to connect participants at a point in time.
- [case conversationUpdated(Conversation.Update)](conversation/event/conversationupdated(_:).md)
  Updates a conversation’s attributes and capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/event/conversationended(_:_:))*