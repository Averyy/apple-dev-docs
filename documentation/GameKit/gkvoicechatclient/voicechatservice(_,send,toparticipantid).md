# voiceChatService(_:send:toParticipantID:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

A request for the client to send data to a participant.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

## Declaration

```swift
func voiceChatService(_ voiceChatService: GKVoiceChatService, send data: Data, toParticipantID participantID: String)
```

```objc
- (void) voiceChatService:(GKVoiceChatService *) voiceChatService sendData:(NSData *) data toParticipantID:(NSString *) participantID;
```

#### Discussion

An implementation of this method must reliably transmit the data to the participant identified by `participantID`. When the client on the other end receives the data, it should forward it to the voice chat service by calling the service’s [`receivedData(_:fromParticipantID:)`](../gkvoicechatservice/receiveddata%28_,fromparticipantid%29.md) method.

## Parameters

- `voiceChatService`: The service that requested the transmission.
- `data`: The data to send.
- `participantID`: A string that uniquely identifies the participant to send the data to.

## See Also

### Sending data to other participants
- [func voiceChatService(GKVoiceChatService, sendRealTime: Data, toParticipantID: String)](./voicechatservice%28_,sendrealtime,toparticipantid%29.md)
  Asks the client to send data to a participant that must get there quickly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/voicechatservice(_:send:toparticipantid:))*