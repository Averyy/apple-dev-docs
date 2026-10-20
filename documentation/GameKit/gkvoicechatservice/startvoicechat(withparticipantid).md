# startVoiceChat(withParticipantID:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Sends a request to another participant to join the voice chat.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use SharePlay instead

## Declaration

```swift
func startVoiceChat(withParticipantID participantID: String!) throws
```

```objc
- (BOOL) startVoiceChatWithParticipantID:(NSString *) participantID error:(NSError **) error;
```

#### Discussion

The voice chat service calls the client’s [`voiceChatService(_:send:toParticipantID:)`](../gkvoicechatclient/voicechatservice%28_,send,toparticipantid%29.md) method to send the connection request to the remote participant.

## Parameters

- `participantID`: A string that uniquely identifies the participant to connect to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/startvoicechat(withparticipantid:))*