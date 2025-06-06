# receivedRealTime(_:fromParticipantID:)

**Framework**: GameKit  
**Kind**: method

Called by the client to deliver voice data received from a remote participant..

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func receivedRealTime(_ audio: Data!, fromParticipantID participantID: String!)
```

#### Discussion

The voice chat service uses a network connection provided by the client to exchange information between the participants. When the client receives information intended for the voice chat service, it should call this method to transfer it.

## Parameters

- `audio`: The audio data that was received from the other participant.
- `participantID`: A string that uniquely identifies the speaking participant.

## See Also

- [func voiceChatService(GKVoiceChatService, sendRealTime: Data, toParticipantID: String)](gkvoicechatclient/voicechatservice(_:sendrealtime:toparticipantid:).md)
  Asks the client to send data to a participant that must get there quickly.
- [func acceptCallID(Int) throws](gkvoicechatservice/acceptcallid(_:).md)
  Accepts a request from a remote user to establish a voice chat.
- [func denyCallID(Int)](gkvoicechatservice/denycallid(_:).md)
  Rejects a request to establish a voice chat.
- [func receivedData(Data!, fromParticipantID: String!)](gkvoicechatservice/receiveddata(_:fromparticipantid:).md)
  Called by the client to deliver new data received from a remote participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/receivedrealtime(_:fromparticipantid:))*