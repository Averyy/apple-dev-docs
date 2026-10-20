# denyCallID(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Rejects a request to establish a voice chat.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use SharePlay instead

## Declaration

```swift
func denyCallID(_ callID: Int)
```

```objc
- (void) denyCallID:(NSInteger) callID;
```

#### Discussion

When a remote user requests a voice chat, the voice chat service calls the client’s [`voiceChatService(_:didReceiveInvitationFromParticipantID:callID:)`](../gkvoicechatclient/voicechatservice%28_,didreceiveinvitationfromparticipantid,callid%29.md) method. The client calls this method to reject the request or [`acceptCallID(_:)`](./acceptcallid%28_%29.md) to accept it.

## Parameters

- `callID`: An integer that identifies the connection request.

## See Also

### Methods Called by the Client
- [func acceptCallID(Int) throws](./acceptcallid%28_%29.md)
  Accepts a request from a remote user to establish a voice chat.
- [func receivedData(Data!, fromParticipantID: String!)](./receiveddata%28_,fromparticipantid%29.md)
  Called by the client to deliver new data received from a remote participant.
- [func receivedRealTime(Data!, fromParticipantID: String!)](./receivedrealtime%28_,fromparticipantid%29.md)
  Called by the client to deliver voice data received from a remote participant..


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/denycallid(_:))*