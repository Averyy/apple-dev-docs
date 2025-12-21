# ConversationManagerDelegate

**Framework**: LiveCommunicationKit  
**Kind**: protocol

Methods for managing conversations and receiving VoIP conversation updates.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
protocol ConversationManagerDelegate : AnyObject
```

## Mentions

- [Initiating VoIP conversations with LiveCommunicationKit](initiating-voip-conversations-with-livecommunicationkit.md)

## Topics

### Observing the conversation manager
- [func conversationManagerDidBegin(ConversationManager)](conversationmanagerdelegate/conversationmanagerdidbegin(_:).md)
  Tells the delegate that your app has started a conversation manager.
- [func conversationManagerDidReset(ConversationManager)](conversationmanagerdelegate/conversationmanagerdidreset(_:).md)
  Tells the delegate that the app has reset the conversation manager.
### Receiving status updates
- [func conversationManager(ConversationManager, conversationChanged: Conversation)](conversationmanagerdelegate/conversationmanager(_:conversationchanged:).md)
  Tells the delegate that a conversation changed.
- [func conversationManager(ConversationManager, didActivate: AVAudioSession)](conversationmanagerdelegate/conversationmanager(_:didactivate:).md)
  Tells the delegate that the app activated the conversation’s audio session.
- [func conversationManager(ConversationManager, didDeactivate: AVAudioSession)](conversationmanagerdelegate/conversationmanager(_:diddeactivate:).md)
  Tells the delegate that the app deactivated a conversation’s audio session..
### Performing actions
- [func conversationManager(ConversationManager, perform: ConversationAction)](conversationmanagerdelegate/conversationmanager(_:perform:).md)
  Tells the delegate that the system requires a conversation action.
- [func conversationManager(ConversationManager, timedOutPerforming: ConversationAction)](conversationmanagerdelegate/conversationmanager(_:timedoutperforming:).md)
  Tells the delegate that a conversation action wasn’t completed and timed out.

## See Also

- [class ConversationManager](conversationmanager.md)
  An interface for managing and observing VoIP conversations.
- [class ConversationHistoryManager](conversationhistorymanager.md)
  An interface for managing and providing conversation history.
- [class Conversation](conversation.md)
  A type that describes a video or audio conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanagerdelegate)*