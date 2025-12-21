# init(_:)

**Framework**: LiveCommunicationKit  
**Kind**: init

Creates an action that initiates a cellular conversation using information from a recent conversation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
init(_ recentConversation: ConversationHistoryManager.RecentConversation)
```

#### Discussion

Starting a cellular conversation from a recent conversation uses the same information associated with the conversation, including all handles, the account, and other information.

## Parameters

- `recentConversation`: A recent conversation to use for the new dial request.

## See Also

- [init(Handle, cellularService: CellularService?)](startcellularconversationaction/init(_:cellularservice:).md)
  Creates an action that initiates a cellular network conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/startcellularconversationaction/init(_:))*