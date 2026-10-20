# receivedRealTime(_:fromParticipantID:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Called by the client to deliver voice data received from a remote participant..

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use SharePlay instead

## Declaration

```swift
func receivedRealTime(_ audio: Data!, fromParticipantID participantID: String!)
```

```objc
- (void) receivedRealTimeData:(NSData *) audio fromParticipantID:(NSString *) participantID;
```

#### Discussion

The voice chat service uses a network connection provided by the client to exchange information between the participants. When the client receives information intended for the voice chat service, it should call this method to transfer it.

## Parameters

- `audio`: The audio data that was received from the other participant.
- `participantID`: A string that uniquely identifies the speaking participant.

## See Also

### Related Documentation
- [func voiceChatService(GKVoiceChatService, sendRealTime: Data, toParticipantID: String)](../gkvoicechatclient/voicechatservice%28_,sendrealtime,toparticipantid%29.md)
  Asks the client to send data to a participant that must get there quickly.
### Methods Called by the Client
- [func acceptCallID(Int) throws](./acceptcallid%28_%29.md)
  Accepts a request from a remote user to establish a voice chat.
- [func denyCallID(Int)](./denycallid%28_%29.md)
  Rejects a request to establish a voice chat.
- [func receivedData(Data!, fromParticipantID: String!)](./receiveddata%28_,fromparticipantid%29.md)
  Called by the client to deliver new data received from a remote participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatservice/receivedrealtime(_:fromparticipantid:))*