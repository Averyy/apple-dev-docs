# conversationManager(_:didActivate:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Required**: Yes

Tells the delegate that the app activated the conversation’s audio session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
func conversationManager(_ manager: ConversationManager, didActivate audioSession: AVAudioSession)
```

## Mentions

- [Initiating VoIP conversations with LiveCommunicationKit](initiating-voip-conversations-with-livecommunicationkit.md)

## Parameters

- `manager`: A conversation manager informing the delegate that the app activated the audio session.
- `audioSession`: The audio session that the app activated.

## See Also

- [func conversationManager(ConversationManager, conversationChanged: Conversation)](conversationmanagerdelegate/conversationmanager(_:conversationchanged:).md)
  Tells the delegate that a conversation changed.
- [func conversationManager(ConversationManager, didDeactivate: AVAudioSession)](conversationmanagerdelegate/conversationmanager(_:diddeactivate:).md)
  Tells the delegate that the app deactivated a conversation’s audio session..


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanagerdelegate/conversationmanager(_:didactivate:))*