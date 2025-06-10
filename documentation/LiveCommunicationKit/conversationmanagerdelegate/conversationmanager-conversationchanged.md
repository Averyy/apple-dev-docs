# conversationManager(_:conversationChanged:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Required**: Yes

Tells the delegate that a conversation changed.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
func conversationManager(_ manager: ConversationManager, conversationChanged conversation: Conversation)
```

## Parameters

- `manager`: A conversation manager informing the delegate that a conversation changed.
- `conversation`: The conversation that changed.

## See Also

- [func conversationManager(ConversationManager, didActivate: AVAudioSession)](conversationmanagerdelegate/conversationmanager(_:didactivate:).md)
  Tells the delegate that the app activated the conversation’s audio session.
- [func conversationManager(ConversationManager, didDeactivate: AVAudioSession)](conversationmanagerdelegate/conversationmanager(_:diddeactivate:).md)
  Tells the delegate that the app deactivated a conversation’s audio session..


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanagerdelegate/conversationmanager(_:conversationchanged:))*