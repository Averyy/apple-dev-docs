# incomingPushResult(channelManager:channelUUID:pushPayload:)

**Framework**: Push to Talk  
**Kind**: method  
**Required**: Yes

Tells the observer that the app has a push available to handle.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func incomingPushResult(channelManager: PTChannelManager, channelUUID: UUID, pushPayload: [String : Any]) -> PTPushResult
```

## Mentions

- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)

#### Discussion

The system calls this method for each incoming push. Return a [`PTPushResult`](ptpushresult.md) as soon as possible and don’t block the thread. Perform network tasks — like downloading a speaker’s image or setting up a streaming network connection to a server — on a separate thread.

If the PTT channel transmission mode is [`PTTransmissionMode.halfDuplex`](pttransmissionmode/halfduplex.md), and the local participant is transmitting when the app receives a PTT notification, returning an active participant results in an error. End the local participant’s transmission by calling [`stopTransmitting(channelUUID:)`](ptchannelmanager/stoptransmitting(channeluuid:).md) before returning an active remote participant.

## Parameters

- `channelManager`: The channel manager.
- `channelUUID`: The channel identifier.
- `pushPayload`: The push payload metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate/incomingpushresult(channelmanager:channeluuid:pushpayload:))*