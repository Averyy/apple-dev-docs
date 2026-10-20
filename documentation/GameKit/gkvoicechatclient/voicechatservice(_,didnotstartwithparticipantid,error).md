# voiceChatService(_:didNotStartWithParticipantID:error:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Received by the client when an attempt to establish a voice chat with another participant failed.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

## Declaration

```swift
optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didNotStartWithParticipantID participantID: String, error: (any Error)?)
```

```objc
- (void) voiceChatService:(GKVoiceChatService *) voiceChatService didNotStartWithParticipantID:(NSString *) participantID error:(NSError *) error;
```

#### Discussion

Your application can implement this method to notify the user that an error occurred when establishing a connection.

## Parameters

- `voiceChatService`: The voice chat service that was establishing the connection.
- `participantID`: A string that uniquely identifies the other user.
- `error`: The error that prevented the voice chat from being established.

## See Also

### Responding to Changes in Other Participants
- [func voiceChatService(GKVoiceChatService, didStartWithParticipantID: String)](./voicechatservice%28_,didstartwithparticipantid%29.md)
  Received by the client when a voice chat with another participant is established.
- [func voiceChatService(GKVoiceChatService, didStopWithParticipantID: String, error: (any Error)?)](./voicechatservice%28_,didstopwithparticipantid,error%29.md)
  Received by the client when a previously established voice chat has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/voicechatservice(_:didnotstartwithparticipantid:error:))*