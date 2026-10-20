# conversationManagerDidBegin(_:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that your app has started a conversation manager.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
func conversationManagerDidBegin(_ manager: ConversationManager)
```

## Parameters

- `manager`: The conversation manager that your app started.

## See Also

### Observing the conversation manager
- [func conversationManagerDidReset(ConversationManager)](./conversationmanagerdidreset%28_%29.md)
  Tells the delegate that the app has reset the conversation manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanagerdelegate/conversationmanagerdidbegin(_:))*