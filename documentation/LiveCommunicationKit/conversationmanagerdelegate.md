# ConversationManagerDelegate

**Framework**: LiveCommunicationKit  
**Kind**: protocol

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

## Topics

### Instance Methods
- [func conversationManager(ConversationManager, conversationChanged: Conversation)](conversationmanagerdelegate/conversationmanager(_:conversationchanged:).md)
  Invoked when a `Conversation` is changed.
- [func conversationManager(ConversationManager, didActivate: AVAudioSession)](conversationmanagerdelegate/conversationmanager(_:didactivate:).md)
  Called when the provider’s audio session is activated.
- [func conversationManager(ConversationManager, didDeactivate: AVAudioSession)](conversationmanagerdelegate/conversationmanager(_:diddeactivate:).md)
  Called when the provider’s audio session is deactivated.
- [func conversationManager(ConversationManager, perform: ConversationAction)](conversationmanagerdelegate/conversationmanager(_:perform:).md)
  Called when the system requires that some `ConversationAction` is performed.
- [func conversationManager(ConversationManager, timedOutPerforming: ConversationAction)](conversationmanagerdelegate/conversationmanager(_:timedoutperforming:).md)
  Called when a `ConversationAction` is not performed before it expires.
- [func conversationManagerDidBegin(ConversationManager)](conversationmanagerdelegate/conversationmanagerdidbegin(_:).md)
  Called when the provider begins.
- [func conversationManagerDidReset(ConversationManager)](conversationmanagerdelegate/conversationmanagerdidreset(_:).md)
  Called when the provider resets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanagerdelegate)*