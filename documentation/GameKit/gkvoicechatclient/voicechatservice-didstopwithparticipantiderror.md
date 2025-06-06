# voiceChatService(_:didStopWithParticipantID:error:)

**Framework**: GameKit  
**Kind**: method

Received by the client when a previously established voice chat has ended.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didStopWithParticipantID participantID: String, error: (any Error)?)
```

#### Discussion

Your application can implement this method to notify the user that an established voice connection has ended. This may occur when another participant ends the chat or if the network connection was lost.

## Parameters

- `voiceChatService`: The voice chat that maintained the connection.
- `participantID`: A string that uniquely identifies the user who disconnected.
- `error`: The error that caused the chat to end.

## See Also

- [func voiceChatService(GKVoiceChatService, didStartWithParticipantID: String)](gkvoicechatclient/voicechatservice(_:didstartwithparticipantid:).md)
  Received by the client when a voice chat with another participant is established.
- [func voiceChatService(GKVoiceChatService, didNotStartWithParticipantID: String, error: (any Error)?)](gkvoicechatclient/voicechatservice(_:didnotstartwithparticipantid:error:).md)
  Received by the client when an attempt to establish a voice chat with another participant failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/voicechatservice(_:didstopwithparticipantid:error:))*