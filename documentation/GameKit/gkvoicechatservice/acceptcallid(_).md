# acceptCallID(_:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Accepts a request from a remote user to establish a voice chat.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use SharePlay instead

## Declaration

```swift
func acceptCallID(_ callID: Int) throws
```

```objc
- (BOOL) acceptCallID:(NSInteger) callID error:(NSError **) error;
```

## Discussion

When a remote user requests a voice chat, the voice chat service calls the client’s [`voiceChatService(_:didReceiveInvitationFromParticipantID:callID:)`](../gkvoicechatclient/voicechatservice%28_,didreceiveinvitationfromparticipantid,callid%29.md) method. The client calls this method to accept the request or [`denyCallID(_:)`](./denycallid%28_%29.md) to reject it.

## Parameters

- `callID`: An integer that identifies the connection request.

## See Also

### Methods Called by the Client
- [func denyCallID(Int)](./denycallid%28_%29.md)
  Rejects a request to establish a voice chat.
- [func receivedData(Data!, fromParticipantID: String!)](./receiveddata%28_,fromparticipantid%29.md)
  Called by the client to deliver new data received from a remote participant.
- [func receivedRealTime(Data!, fromParticipantID: String!)](./receivedrealtime%28_,fromparticipantid%29.md)
  Called by the client to deliver voice data received from a remote participant..


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/acceptcallid(_:))*