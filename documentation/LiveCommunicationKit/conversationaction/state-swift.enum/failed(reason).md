# ConversationAction.State.failed(reason:)

**Framework**: LiveCommunicationKit  
**Kind**: case  
**Role**: Case

Indicates that the action failed.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
case failed(reason: String)
```

## Parameters

- `reason`: A string that describes why the action failed.

## See Also

### Constants
- [ConversationAction.State.complete](./complete.md)
  The action finished successfully.
- [ConversationAction.State.idle](./idle.md)
  The action has been created but hasn’t started.
- [ConversationAction.State.running](./running.md)
  The action is currently processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationaction/state-swift.enum/failed(reason:))*