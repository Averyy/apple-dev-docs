# conversationManager(_:timedOutPerforming:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Required**: Yes

Called when a `ConversationAction` is not performed before it expires.

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

- `manager`: The   that has requested the   to be performed.
- `action`: The   that timed out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanagerdelegate/conversationmanager(_:timedoutperforming:))*