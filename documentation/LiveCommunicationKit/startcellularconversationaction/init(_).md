# init(_:)

**Framework**: LiveCommunicationKit  
**Kind**: init  
**Role**: Initializer

Creates an action that initiates a cellular conversation using information from a recent conversation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
init(_ recentConversation: ConversationHistoryManager.RecentConversation)
```

## Discussion

Starting a cellular conversation from a recent conversation uses the same information associated with the conversation, including all handles, the account, and other information.

## Parameters

- `recentConversation`: A recent conversation to use for the new dial request.

## See Also

### Request creation
- [init(Handle, cellularService: CellularService?)](./init%28_,cellularservice%29.md)
  Creates an action that initiates a cellular network conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/startcellularconversationaction/init(_:))*