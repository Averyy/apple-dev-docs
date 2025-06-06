# ConversationAction

**Framework**: LiveCommunicationKit  
**Kind**: class

A programmatic interface for objects that represent a VoIP action associated with a `Conversation`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
class ConversationAction
```

## Topics

### Initializers
- [convenience init(conversationUUID: UUID, timeoutDate: Date)](conversationaction/init(conversationuuid:timeoutdate:).md)
  Initializes a new conversation action.
### Instance Properties
- [var conversationUUID: UUID](conversationaction/conversationuuid.md)
  The unique identifier for the `Conversation` associated with the action.
- [var state: ConversationAction.State](conversationaction/state-swift.property.md)
  The action’s current state.
- [var timeoutDate: Date](conversationaction/timeoutdate.md)
  The `Date` after which the action cannot be completed.
- [var uuid: UUID](conversationaction/uuid.md)
  The unique identifier for the action.
### Instance Methods
- [func fail()](conversationaction/fail.md)
  Reports the failed execution of the action.
- [func fulfill()](conversationaction/fulfill.md)
  Reports the successful execution of the action.
### Enumerations
- [ConversationAction.State](conversationaction/state-swift.enum.md)
  Represents the current state of a `ConversationAction`.

## Relationships

### Inherited By
- [EndConversationAction](endconversationaction.md)
- [JoinConversationAction](joinconversationaction.md)
- [MergeConversationAction](mergeconversationaction.md)
- [MuteConversationAction](muteconversationaction.md)
- [PauseConversationAction](pauseconversationaction.md)
- [PlayToneAction](playtoneaction.md)
- [StartConversationAction](startconversationaction.md)
- [UnmergeConversationAction](unmergeconversationaction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationaction)*