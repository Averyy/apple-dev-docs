# Conversation.Event.conversationStartedConnecting(_:)

**Framework**: LiveCommunicationKit  
**Kind**: case

Informs the system that a conversation has started to connect participants at a point in time.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
case conversationStartedConnecting(Date)
```

## See Also

- [Conversation.Event.conversationConnected(_:)](conversation/event/conversationconnected(_:).md)
  Informs that system that conversation successfully connected at a point in time.
- [case conversationEnded(Date, Conversation.EndedReason)](conversation/event/conversationended(_:_:).md)
  Informs that system that a conversation ended at a point in time with a reason.
- [case conversationUpdated(Conversation.Update)](conversation/event/conversationupdated(_:).md)
  Updates a conversation’s attributes and capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversation/event/conversationstartedconnecting(_:))*