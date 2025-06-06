# voiceChatService(_:didStartWithParticipantID:)

**Framework**: GameKit  
**Kind**: method

Received by the client when a voice chat with another participant is established.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didStartWithParticipantID participantID: String)
```

#### Discussion

Your client can use this method to update the user interface to show that a connection has been established.

## Parameters

- `voiceChatService`: The voice chat service that initiated the connection.
- `participantID`: A string that uniquely identifies the other user.

## See Also

- [func voiceChatService(GKVoiceChatService, didNotStartWithParticipantID: String, error: (any Error)?)](gkvoicechatclient/voicechatservice(_:didnotstartwithparticipantid:error:).md)
  Received by the client when an attempt to establish a voice chat with another participant failed.
- [func voiceChatService(GKVoiceChatService, didStopWithParticipantID: String, error: (any Error)?)](gkvoicechatclient/voicechatservice(_:didstopwithparticipantid:error:).md)
  Received by the client when a previously established voice chat has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/voicechatservice(_:didstartwithparticipantid:))*