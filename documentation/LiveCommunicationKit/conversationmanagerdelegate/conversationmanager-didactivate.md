# conversationManager(_:didActivate:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Required**: Yes

Called when the provider’s audio session is activated.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
func conversationManager(_ manager: ConversationManager, didActivate audioSession: AVAudioSession)
```

## Parameters

- `manager`: The   that has requested the   to be performed.
- `audioSession`: The audio session that was activated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanagerdelegate/conversationmanager(_:didactivate:))*