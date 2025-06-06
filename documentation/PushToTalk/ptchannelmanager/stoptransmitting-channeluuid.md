# stopTransmitting(channelUUID:)

**Framework**: Push to Talk  
**Kind**: method

Stops an audio transmission with the channel identifer you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func stopTransmitting(channelUUID: UUID)
```

## Mentions

- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)

#### Discussion

If successful, you receive a callback from [`channelManager(_:channelUUID:didEndTransmittingFrom:)`](ptchannelmanagerdelegate/channelmanager(_:channeluuid:didendtransmittingfrom:).md) with `PTChannelTransmitRequestSource.programmaticRequest`; otherwise, you receive a failure reason through [`channelManager(_:failedToStopTransmittingInChannel:error:)`](ptchannelmanagerdelegate/channelmanager(_:failedtostoptransmittinginchannel:error:).md).

## Parameters

- `channelUUID`: The channel identifier.

## See Also

- [func requestBeginTransmitting(channelUUID: UUID)](ptchannelmanager/requestbegintransmitting(channeluuid:).md)
  Begins an audio transmission with the channel identifer you specify.
- [func setAccessoryButtonEventsEnabled(Bool, channelUUID: UUID, completionHandler: (((any Error)?) -> Void)?)](ptchannelmanager/setaccessorybuttoneventsenabled(_:channeluuid:completionhandler:).md)
  Maps supported accessory button events to actions that begin and end transmission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanager/stoptransmitting(channeluuid:))*