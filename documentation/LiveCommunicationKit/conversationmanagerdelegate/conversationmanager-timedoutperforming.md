# conversationManager(_:timedOutPerforming:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Required**: Yes

Tells the delegate that a conversation action wasn’t completed and timed out.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
func conversationManager(_ manager: ConversationManager, timedOutPerforming action: ConversationAction)
```

## Parameters

- `manager`: A conversation manager informing the delegate that the requested action wasn’t completed and timed out.
- `action`: The action that wasn’t completed and timed out.

## See Also

- [func conversationManager(ConversationManager, perform: ConversationAction)](conversationmanagerdelegate/conversationmanager(_:perform:).md)
  Tells the delegate that the system requires a conversation action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanagerdelegate/conversationmanager(_:timedoutperforming:))*