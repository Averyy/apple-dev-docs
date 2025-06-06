# voiceChatService(_:didReceiveInvitationFromParticipantID:callID:)

**Framework**: GameKit  
**Kind**: method

Asks the client to accept or reject an invitation from a remote participant.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didReceiveInvitationFromParticipantID participantID: String, callID: Int)
```

#### Discussion

If this method is not implemented by the client, the voice chat service automatically accept requests from other participants.

This method should call the service’s [`acceptCallID(_:)`](gkvoicechatservice/acceptcallid(_:).md) method if it wants to accept the request or the [`denyCallID(_:)`](gkvoicechatservice/denycallid(_:).md) to reject it.

## Parameters

- `voiceChatService`: The service that received the request.
- `participantID`: A string that uniquely identifies the other user.
- `callID`: An integer that uniquely identifies the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/voicechatservice(_:didreceiveinvitationfromparticipantid:callid:))*