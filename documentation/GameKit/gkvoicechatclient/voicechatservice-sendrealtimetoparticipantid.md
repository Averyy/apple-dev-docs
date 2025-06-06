# voiceChatService(_:sendRealTime:toParticipantID:)

**Framework**: GameKit  
**Kind**: method

Asks the client to send data to a participant that must get there quickly.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func voiceChatService(_ voiceChatService: GKVoiceChatService, sendRealTime data: Data, toParticipantID participantID: String)
```

#### Discussion

An implementation of this method maps the `participantID` string to a known participant and transmits the data to them. Data transmitted by this method can be sent unreliably. When the client on the other end receives this data, it should forward it to the voice chat service by calling the service’s [`receivedRealTime(_:fromParticipantID:)`](gkvoicechatservice/receivedrealtime(_:fromparticipantid:).md) method.

## Parameters

- `voiceChatService`: The service that requested the transmission.
- `data`: The data to send.
- `participantID`: A string that uniquely identifies the participant to send the data to.

## See Also

- [func voiceChatService(GKVoiceChatService, send: Data, toParticipantID: String)](gkvoicechatclient/voicechatservice(_:send:toparticipantid:).md)
  A request for the client to send data to a participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/voicechatservice(_:sendrealtime:toparticipantid:))*