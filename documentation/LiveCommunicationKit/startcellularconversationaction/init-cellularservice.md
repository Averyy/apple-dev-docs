# init(_:cellularService:)

**Framework**: LiveCommunicationKit  
**Kind**: init

Creates an action that initiates a cellular network conversation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
init(_ handle: Handle, cellularService: CellularService? = nil)
```

#### Discussion

If you don’t provide an cellular service, the system chooses a service for the conversation or fails the action.

## Parameters

- `handle`: The handle of the conversation’s recipient.
- `cellularService`: The cellular service for the conversation.

## See Also

- [init(ConversationHistoryManager.RecentConversation)](startcellularconversationaction/init(_:).md)
  Creates an action that initiates a cellular conversation using information from a recent conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/startcellularconversationaction/init(_:cellularservice:))*