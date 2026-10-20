# voiceChatService(_:didReceiveInvitationFromParticipantID:callID:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Asks the client to accept or reject an invitation from a remote participant.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

## Declaration

```swift
optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didReceiveInvitationFromParticipantID participantID: String, callID: Int)
```

```objc
- (void) voiceChatService:(GKVoiceChatService *) voiceChatService didReceiveInvitationFromParticipantID:(NSString *) participantID callID:(NSInteger) callID;
```

#### Discussion

If this method is not implemented by the client, the voice chat service automatically accept requests from other participants.

This method should call the service’s [`acceptCallID(_:)`](../gkvoicechatservice/acceptcallid%28_%29.md) method if it wants to accept the request or the [`denyCallID(_:)`](../gkvoicechatservice/denycallid%28_%29.md) to reject it.

## Parameters

- `voiceChatService`: The service that received the request.
- `participantID`: A string that uniquely identifies the other user.
- `callID`: An integer that uniquely identifies the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/voicechatservice(_:didreceiveinvitationfromparticipantid:callid:))*