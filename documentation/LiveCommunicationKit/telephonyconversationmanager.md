# TelephonyConversationManager

**Framework**: LiveCommunicationKit  
**Kind**: class

An interface for initiating cellular network conversations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
final class TelephonyConversationManager
```

## Mentions

- [Preparing your app to be the default dialer app](preparing-your-app-to-be-the-default-dialer-app.md)
- [Initiating VoIP conversations with LiveCommunicationKit](initiating-voip-conversations-with-livecommunicationkit.md)

#### Overview

Use `TelephonyConversationManager` to initiate a cellular conversation and let the system route the conversation to the default calling app. For more information, see [`Preparing your app to be the default dialer app`](preparing-your-app-to-be-the-default-dialer-app.md).

## Topics

### Starting a conversation
- [func startCellularConversation(StartCellularConversationAction) async throws](telephonyconversationmanager/startcellularconversation(_:).md)
  Starts a cellular conversation using the provided action.
- [static let sharedInstance: TelephonyConversationManager](telephonyconversationmanager/sharedinstance.md)
  The shared object that manages cellular conversations.
### Cellular services
- [var cellularServices: [CellularService]](telephonyconversationmanager/cellularservices.md)
  A read-only list of cellular service accounts that you can use to initiate a cellular conversation.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct StartCellularConversationAction](startcellularconversationaction.md)
  The action that starts a cellular conversation using the default calling app.
- [struct CellularService](cellularservice.md)
  A structure that represents the cellular service account to use for starting or joining a conversation.
- [struct Handle](handle.md)
  A way to reach a participant, such as a phone number or email address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/telephonyconversationmanager)*