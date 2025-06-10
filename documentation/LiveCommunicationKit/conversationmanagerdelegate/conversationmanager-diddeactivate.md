# conversationManager(_:didDeactivate:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Required**: Yes

Tells the delegate that the app deactivated a conversation’s audio session..

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
func conversationManager(_ manager: ConversationManager, didDeactivate audioSession: AVAudioSession)
```

## Parameters

- `manager`: A conversation manager informing the delegate that the app deactivated the audio session.
- `audioSession`: The audio session that the app deactivated.

## See Also

- [func conversationManager(ConversationManager, conversationChanged: Conversation)](conversationmanagerdelegate/conversationmanager(_:conversationchanged:).md)
  Tells the delegate that a conversation changed.
- [func conversationManager(ConversationManager, didActivate: AVAudioSession)](conversationmanagerdelegate/conversationmanager(_:didactivate:).md)
  Tells the delegate that the app activated the conversation’s audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanagerdelegate/conversationmanager(_:diddeactivate:))*