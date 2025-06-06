# startVoiceChat(withParticipantID:)

**Framework**: GameKit  
**Kind**: method

Sends a request to another participant to join the voice chat.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func startVoiceChat(withParticipantID participantID: String!) throws
```

#### Discussion

The voice chat service calls the client’s [`voiceChatService(_:send:toParticipantID:)`](gkvoicechatclient/voicechatservice(_:send:toparticipantid:).md) method to send the connection request to the remote participant.

## Parameters

- `participantID`: A string that uniquely identifies the participant to connect to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/startvoicechat(withparticipantid:))*