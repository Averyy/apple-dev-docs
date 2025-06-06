# receivedData(_:fromParticipantID:)

**Framework**: GameKit  
**Kind**: method

Called by the client to deliver new data received from a remote participant.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func receivedData(_ arbitraryData: Data!, fromParticipantID participantID: String!)
```

#### Discussion

The voice chat service uses a network connection provided by the client to exchange information between the participants. When the client receives information intended for the voice chat service, it should call this method to transfer it.

## Parameters

- `arbitraryData`: The data received from a participant.
- `participantID`: A string that uniquely identifies the participant who sent the data.

## See Also

- [func voiceChatService(GKVoiceChatService, send: Data, toParticipantID: String)](gkvoicechatclient/voicechatservice(_:send:toparticipantid:).md)
  A request for the client to send data to a participant.
- [func acceptCallID(Int) throws](gkvoicechatservice/acceptcallid(_:).md)
  Accepts a request from a remote user to establish a voice chat.
- [func denyCallID(Int)](gkvoicechatservice/denycallid(_:).md)
  Rejects a request to establish a voice chat.
- [func receivedRealTime(Data!, fromParticipantID: String!)](gkvoicechatservice/receivedrealtime(_:fromparticipantid:).md)
  Called by the client to deliver voice data received from a remote participant..


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/receiveddata(_:fromparticipantid:))*