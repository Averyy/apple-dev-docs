# voiceChatService(_:send:toParticipantID:)

**Framework**: GameKit  
**Kind**: method  
**Required**: Yes

A request for the client to send data to a participant.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func voiceChatService(_ voiceChatService: GKVoiceChatService, send data: Data, toParticipantID participantID: String)
```

#### Discussion

An implementation of this method must reliably transmit the data to the participant identified by `participantID`. When the client on the other end receives the data, it should forward it to the voice chat service by calling the service’s [`receivedData(_:fromParticipantID:)`](gkvoicechatservice/receiveddata(_:fromparticipantid:).md) method.

## Parameters

- `voiceChatService`: The service that requested the transmission.
- `data`: The data to send.
- `participantID`: A string that uniquely identifies the participant to send the data to.

## See Also

- [func voiceChatService(GKVoiceChatService, sendRealTime: Data, toParticipantID: String)](gkvoicechatclient/voicechatservice(_:sendrealtime:toparticipantid:).md)
  Asks the client to send data to a participant that must get there quickly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/voicechatservice(_:send:toparticipantid:))*