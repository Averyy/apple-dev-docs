# voiceChatService(_:didNotStartWithParticipantID:error:)

**Framework**: GameKit  
**Kind**: method

Received by the client when an attempt to establish a voice chat with another participant failed.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didNotStartWithParticipantID participantID: String, error: (any Error)?)
```

#### Discussion

Your application can implement this method to notify the user that an error occurred when establishing a connection.

## Parameters

- `voiceChatService`: The voice chat service that was establishing the connection.
- `participantID`: A string that uniquely identifies the other user.
- `error`: The error that prevented the voice chat from being established.

## See Also

- [func voiceChatService(GKVoiceChatService, didStartWithParticipantID: String)](gkvoicechatclient/voicechatservice(_:didstartwithparticipantid:).md)
  Received by the client when a voice chat with another participant is established.
- [func voiceChatService(GKVoiceChatService, didStopWithParticipantID: String, error: (any Error)?)](gkvoicechatclient/voicechatservice(_:didstopwithparticipantid:error:).md)
  Received by the client when a previously established voice chat has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/voicechatservice(_:didnotstartwithparticipantid:error:))*