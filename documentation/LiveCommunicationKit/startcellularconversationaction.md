# StartCellularConversationAction

**Framework**: LiveCommunicationKit  
**Kind**: struct  
**Role**: Structure

The action that starts a cellular conversation using the default calling app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct StartCellularConversationAction
```

## Mentions

- [Preparing your app to be the default dialer app](./preparing-your-app-to-be-the-default-dialer-app.md)
- [Initiating VoIP conversations with LiveCommunicationKit](./initiating-voip-conversations-with-livecommunicationkit.md)

#### Overview

Use the `StartCellularConversationAction` to  initiate a conversation and let the system route the conversation to the default calling app. For more information, see [Preparing your app to be the default dialer app](./preparing-your-app-to-be-the-default-dialer-app.md).

## Topics

### Request creation
- [init(Handle, cellularService: CellularService?)](./startcellularconversationaction/init%28_,cellularservice%29.md)
  Creates an action that initiates a cellular network conversation.
- [init(ConversationHistoryManager.RecentConversation)](./startcellularconversationaction/init%28_%29.md)
  Creates an action that initiates a cellular conversation using information from a recent conversation.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Cellular network conversations
- [class TelephonyConversationManager](./telephonyconversationmanager.md)
  An interface for initiating cellular network conversations.
- [struct CellularService](./cellularservice.md)
  A structure that represents the cellular service account to use for starting or joining a conversation.
- [struct Handle](./handle.md)
  A way to reach a participant, such as a phone number or email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/startcellularconversationaction)*