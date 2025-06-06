# stopVoiceChat(withParticipantID:)

**Framework**: GameKit  
**Kind**: method

Ends a previously established voice chat.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func stopVoiceChat(withParticipantID participantID: String!)
```

#### Discussion

When this method is called, the client’s [`voiceChatService(_:didStopWithParticipantID:error:)`](gkvoicechatclient/voicechatservice(_:didstopwithparticipantid:error:).md) method is called.

## Parameters

- `participantID`: A string that uniquely identifies the participant in the chat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/stopvoicechat(withparticipantid:))*