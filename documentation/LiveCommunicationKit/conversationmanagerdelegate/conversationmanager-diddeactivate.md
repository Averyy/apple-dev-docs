# conversationManager(_:didDeactivate:)

**Framework**: LiveCommunicationKit  
**Kind**: method  
**Required**: Yes

Called when the provider’s audio session is deactivated.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
func conversationManager(_ manager: ConversationManager, didDeactivate audioSession: AVAudioSession)
```

## Parameters

- `manager`: The   that has requested the   to be performed.
- `audioSession`: The audio session that was deactivated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/conversationmanagerdelegate/conversationmanager(_:diddeactivate:))*