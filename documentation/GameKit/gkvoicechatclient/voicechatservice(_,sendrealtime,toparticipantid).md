# voiceChatService(_:sendRealTime:toParticipantID:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Asks the client to send data to a participant that must get there quickly.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

## Declaration

```swift
optional func voiceChatService(_ voiceChatService: GKVoiceChatService, sendRealTime data: Data, toParticipantID participantID: String)
```

```objc
- (void) voiceChatService:(GKVoiceChatService *) voiceChatService sendRealTimeData:(NSData *) data toParticipantID:(NSString *) participantID;
```

## Discussion

An implementation of this method maps the `participantID` string to a known participant and transmits the data to them. Data transmitted by this method can be sent unreliably. When the client on the other end receives this data, it should forward it to the voice chat service by calling the service’s [`receivedRealTime(_:fromParticipantID:)`](../gkvoicechatservice/receivedrealtime%28_,fromparticipantid%29.md) method.

## Parameters

- `voiceChatService`: The service that requested the transmission.
- `data`: The data to send.
- `participantID`: A string that uniquely identifies the participant to send the data to.

## See Also

### Sending data to other participants
- [func voiceChatService(GKVoiceChatService, send: Data, toParticipantID: String)](./voicechatservice%28_,send,toparticipantid%29.md)
  A request for the client to send data to a participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/voicechatservice(_:sendrealtime:toparticipantid:))*