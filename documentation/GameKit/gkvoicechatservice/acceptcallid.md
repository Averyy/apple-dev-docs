# acceptCallID(_:)

**Framework**: GameKit  
**Kind**: method

Accepts a request from a remote user to establish a voice chat.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func acceptCallID(_ callID: Int) throws
```

#### Discussion

When a remote user requests a voice chat, the voice chat service calls the client’s [`voiceChatService(_:didReceiveInvitationFromParticipantID:callID:)`](gkvoicechatclient/voicechatservice(_:didreceiveinvitationfromparticipantid:callid:).md) method. The client calls this method to accept the request or [`denyCallID(_:)`](gkvoicechatservice/denycallid(_:).md) to reject it.

## Parameters

- `callID`: An integer that identifies the connection request.

## See Also

- [func denyCallID(Int)](gkvoicechatservice/denycallid(_:).md)
  Rejects a request to establish a voice chat.
- [func receivedData(Data!, fromParticipantID: String!)](gkvoicechatservice/receiveddata(_:fromparticipantid:).md)
  Called by the client to deliver new data received from a remote participant.
- [func receivedRealTime(Data!, fromParticipantID: String!)](gkvoicechatservice/receivedrealtime(_:fromparticipantid:).md)
  Called by the client to deliver voice data received from a remote participant..


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/acceptcallid(_:))*