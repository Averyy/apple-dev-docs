# DialRequest

**Framework**: LiveCommunicationKit  
**Kind**: struct

A request to start a conversation using the default calling app.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct DialRequest
```

## Mentions

- [Preparing your app to be the default dialer app](preparing-your-app-to-be-the-default-dialer-app.md)
- [Initiating VoIP conversations with LiveCommunicationKit](initiating-voip-conversations-with-livecommunicationkit.md)

#### Overview

Use `DialRequest` together with [`TelephonyManager`](telephonymanager.md) to initiate a conversation and let the system route the conversation to the default calling app. For more information, see [`Preparing your app to be the default dialer app`](preparing-your-app-to-be-the-default-dialer-app.md).

## Topics

### Request creation
- [init(handle: Handle, account: Account?)](dialrequest/init(handle:account:).md)
  Creates a request to initiate a conversation.
- [init(recentConversation: ConversationHistoryManager.RecentConversation)](dialrequest/init(recentconversation:).md)
  Creates a request to initiate a conversation using information from a recent conversation.

## See Also

- [class TelephonyManager](telephonymanager.md)
  An interface for initiating cellular network or VoIP conversations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/dialrequest)*