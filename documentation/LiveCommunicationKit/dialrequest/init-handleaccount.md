# init(handle:account:)

**Framework**: LiveCommunicationKit  
**Kind**: init

Creates a request to initiate a conversation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
init(handle: Handle, account: Account? = nil)
```

#### Discussion

If you don’t provide an account, the system chooses an account to dial with or fails the request.

## Parameters

- `handle`: The handle of the request’s recipient.
- `account`: The account for initiating the conversation.

## See Also

- [init(recentConversation: ConversationHistoryManager.RecentConversation)](dialrequest/init(recentconversation:).md)
  Creates a request to initiate a conversation using information from a recent conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/dialrequest/init(handle:account:))*