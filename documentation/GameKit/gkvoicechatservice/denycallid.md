# denyCallID(_:)

**Framework**: GameKit  
**Kind**: method

Rejects a request to establish a voice chat.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func denyCallID(_ callID: Int)
```

#### Discussion

When a remote user requests a voice chat, the voice chat service calls the client’s [`voiceChatService(_:didReceiveInvitationFromParticipantID:callID:)`](gkvoicechatclient/voicechatservice(_:didreceiveinvitationfromparticipantid:callid:).md) method. The client calls this method to reject the request or [`acceptCallID(_:)`](gkvoicechatservice/acceptcallid(_:).md) to accept it.

## Parameters

- `callID`: An integer that identifies the connection request.

## See Also

- [func acceptCallID(Int) throws](gkvoicechatservice/acceptcallid(_:).md)
  Accepts a request from a remote user to establish a voice chat.
- [func receivedData(Data!, fromParticipantID: String!)](gkvoicechatservice/receiveddata(_:fromparticipantid:).md)
  Called by the client to deliver new data received from a remote participant.
- [func receivedRealTime(Data!, fromParticipantID: String!)](gkvoicechatservice/receivedrealtime(_:fromparticipantid:).md)
  Called by the client to deliver voice data received from a remote participant..


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/denycallid(_:))*