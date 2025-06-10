# Conversation.Event.conversationUpdated(_:)

**Framework**: LiveCommunicationKit  
**Kind**: case

Updates a conversation’s attributes and capabilities.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
case conversationUpdated(Conversation.Update)
```

## See Also

- [Conversation.Event.conversationConnected(_:)](conversation/event/conversationconnected(_:).md)
  Informs that system that conversation successfully connected at a point in time.
- [case conversationEnded(Date, Conversation.EndedReason)](conversation/event/conversationended(_:_:).md)
  Informs that system that a conversation ended at a point in time with a reason.
- [Conversation.Event.conversationStartedConnecting(_:)](conversation/event/conversationstartedconnecting(_:).md)
  Informs the system that a conversation has started to connect participants at a point in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/event/conversationupdated(_:))*