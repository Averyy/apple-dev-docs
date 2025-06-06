# ConversationManager

**Framework**: LiveCommunicationKit  
**Kind**: class

A programmatic interface for interacting with and observing conversations.

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

## Topics

### Structures
- [ConversationManager.Configuration](conversationmanager/configuration-swift.struct.md)
  An encapsulation of the configuration of a `ConversationManager`.
### Initializers
- [convenience init(configuration: ConversationManager.Configuration)](conversationmanager/init(configuration:).md)
  Creates a new `ConversationManager` with the given `ConversationManager.Configuration`.
### Instance Properties
- [let configuration: ConversationManager.Configuration](conversationmanager/configuration-swift.property.md)
  The configuration of the manager.
- [var conversations: [Conversation]](conversationmanager/conversations.md)
- [var delegate: (any ConversationManagerDelegate)?](conversationmanager/delegate.md)
- [var pendingActions: [ConversationAction]](conversationmanager/pendingactions.md)
  `ConversationAction`s that have not yet been fulfilled.
### Instance Methods
- [func invalidate()](conversationmanager/invalidate.md)
  Invalidates the manager, ends all `Conversation`s, and fails all pending `ConversationAction`s.
- [func pendingConversationActions(of: ConversationAction.Type, for: Conversation) -> [ConversationAction]](conversationmanager/pendingconversationactions(of:for:).md)
  Returns all pending `ConversationAction`s of the specified class for the specified call identifier that are incomplete.
- [func perform([ConversationAction]) async throws](conversationmanager/perform(_:).md)
  Instructs the `ConversationManager` to asynchronously perform the given actions.
- [func reportConversationEvent(Conversation.Event, for: Conversation)](conversationmanager/reportconversationevent(_:for:).md)
  Informs the system that some event has occurred and to update the given `Conversation` as needed.
- [func reportNewIncomingConversation(uuid: UUID, update: Conversation.Update) async throws](conversationmanager/reportnewincomingconversation(uuid:update:).md)
  Informs the system that there’s a new incoming Conversation, and the device should begin to ring and present the incoming Conversation UI.
### Type Methods
- [class func reportNewIncomingVoIPPushPayload([AnyHashable : Any]) async throws](conversationmanager/reportnewincomingvoippushpayload(_:).md)
  Reports a new incoming call after your notification service extension decrypts a VoIP call request.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Observable](../Observation/Observable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanager)*