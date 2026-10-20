# conversationManager(_:conversationChanged:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Role**: Instance Method  
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

### Receiving status updates
- [func conversationManager(ConversationManager, didActivate: AVAudioSession)](./conversationmanager%28_,didactivate%29.md)
  Tells the delegate that the app activated the conversation’s audio session.
- [func conversationManager(ConversationManager, didDeactivate: AVAudioSession)](./conversationmanager%28_,diddeactivate%29.md)
  Tells the delegate that the app deactivated a conversation’s audio session..


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanagerdelegate/conversationmanager(_:conversationchanged:))*