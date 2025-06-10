# ConversationManager

**Framework**: LiveCommunicationKit  
**Kind**: class

An interface for managing and observing VoIP conversations.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
final class ConversationManager
```

## Mentions

- [Initiating VoIP conversations with LiveCommunicationKit](initiating-voip-conversations-with-livecommunicationkit.md)

#### Overview

Use `ConversationManager` to provide VoIP conversation functionality in your app. For more information, see [`Preparing your app to be the default dialer app`](preparing-your-app-to-be-the-default-dialer-app.md).

## Topics

### Creating the manager
- [convenience init(configuration: ConversationManager.Configuration)](conversationmanager/init(configuration:).md)
  Creates a new conversation manager with a given conversation.
- [let configuration: ConversationManager.Configuration](conversationmanager/configuration-swift.property.md)
  The configuration of a conversation manager.
- [ConversationManager.Configuration](conversationmanager/configuration-swift.struct.md)
  Configuration options for a conversation manager.
### Configuring the manager
- [var conversations: [Conversation]](conversationmanager/conversations.md)
  Currently active conversations.
- [var pendingActions: [ConversationAction]](conversationmanager/pendingactions.md)
  All unfinished conversation actions.
- [var delegate: (any ConversationManagerDelegate)?](conversationmanager/delegate.md)
  The object that acts as the delegate of the conversation manager.
### Managing conversations
- [func perform([ConversationAction]) async throws](conversationmanager/perform(_:).md)
  Tells the conversation manager to asynchronously perform actions for a conversation.
- [func invalidate()](conversationmanager/invalidate.md)
  Invalidates the conversation manager, ends all conversations, and fails all pending concersation actions.
### Observing conversations
- [func pendingConversationActions(of: ConversationAction.Type, for: Conversation) -> [ConversationAction]](conversationmanager/pendingconversationactions(of:for:).md)
  Queries a conversation for pending actions of a specified type.
- [func reportConversationEvent(Conversation.Event, for: Conversation)](conversationmanager/reportconversationevent(_:for:).md)
  Informs the system that an event has occurred and that it needs to update the conversation if necessary.
- [func reportNewIncomingConversation(uuid: UUID, update: Conversation.Update) async throws](conversationmanager/reportnewincomingconversation(uuid:update:).md)
  Informs the system that there’s a new incoming conversation, and the device should begin to ring and present the incoming Conversation UI.
- [class func reportNewIncomingVoIPPushPayload([AnyHashable : Any]) async throws](conversationmanager/reportnewincomingvoippushpayload(_:).md)
  Reports a new incoming conversation after your notification service extension decrypts a VoIP request.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Observable](../Observation/Observable.md)

## See Also

- [protocol ConversationManagerDelegate](conversationmanagerdelegate.md)
  Methods for managing conversations and receiving VoIP conversation updates.
- [class Conversation](conversation.md)
  A type that describes a video or audio conversation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanager)*