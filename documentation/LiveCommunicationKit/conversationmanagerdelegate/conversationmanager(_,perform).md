# conversationManager(_:perform:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that the system requires a conversation action.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
func conversationManager(_ manager: ConversationManager, perform action: ConversationAction)
```

## Parameters

- `manager`: A conversation manager informing the delegate that the system requires a conversation action.
- `action`: The action to perform and fulfill.

## See Also

### Performing actions
- [func conversationManager(ConversationManager, timedOutPerforming: ConversationAction)](./conversationmanager%28_,timedoutperforming%29.md)
  Tells the delegate that a conversation action wasn’t completed and timed out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanagerdelegate/conversationmanager(_:perform:))*