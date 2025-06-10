# init(recentConversation:)

**Framework**: LiveCommunicationKit  
**Kind**: init

Creates a request to initiate a conversation using information from a recent conversation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
init(recentConversation: ConversationHistoryManager.RecentConversation)
```

#### Discussion

Dialing using a recent conversation uses the same information associated with the conversation, including all handles, the account, and other information.

## Parameters

- `recentConversation`: A recent conversation to use for the new dial request.

## See Also

- [init(handle: Handle, account: Account?)](dialrequest/init(handle:account:).md)
  Creates a request to initiate a conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/dialrequest/init(recentconversation:))*