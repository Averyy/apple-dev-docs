# voiceChatService(_:didStartWithParticipantID:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Received by the client when a voice chat with another participant is established.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

## Declaration

```swift
optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didStartWithParticipantID participantID: String)
```

```objc
- (void) voiceChatService:(GKVoiceChatService *) voiceChatService didStartWithParticipantID:(NSString *) participantID;
```

#### Discussion

Your client can use this method to update the user interface to show that a connection has been established.

## Parameters

- `voiceChatService`: The voice chat service that initiated the connection.
- `participantID`: A string that uniquely identifies the other user.

## See Also

### Responding to Changes in Other Participants
- [func voiceChatService(GKVoiceChatService, didNotStartWithParticipantID: String, error: (any Error)?)](./voicechatservice%28_,didnotstartwithparticipantid,error%29.md)
  Received by the client when an attempt to establish a voice chat with another participant failed.
- [func voiceChatService(GKVoiceChatService, didStopWithParticipantID: String, error: (any Error)?)](./voicechatservice%28_,didstopwithparticipantid,error%29.md)
  Received by the client when a previously established voice chat has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/voicechatservice(_:didstartwithparticipantid:))*