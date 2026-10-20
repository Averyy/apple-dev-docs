# stopTransmitting(channelUUID:)

**Framework**: Push to Talk  
**Kind**: method  
**Role**: Instance Method

Stops an audio transmission with the channel identifer you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func stopTransmitting(channelUUID: UUID)
```

```objc
- (void) stopTransmittingWithChannelUUID:(NSUUID *) channelUUID;
```

## Mentions

- [Creating a Push to Talk app](../creating-a-push-to-talk-app.md)

#### Discussion

If successful, you receive a callback from [`channelManager(_:channelUUID:didEndTransmittingFrom:)`](../ptchannelmanagerdelegate/channelmanager%28_,channeluuid,didendtransmittingfrom%29.md) with `PTChannelTransmitRequestSource.programmaticRequest`; otherwise, you receive a failure reason through [`channelManager(_:failedToStopTransmittingInChannel:error:)`](../ptchannelmanagerdelegate/channelmanager%28_,failedtostoptransmittinginchannel,error%29.md).

## Parameters

- `channelUUID`: The channel identifier.

## See Also

### Starting and stopping transmission
- [func requestBeginTransmitting(channelUUID: UUID)](./requestbegintransmitting%28channeluuid%29.md)
  Begins an audio transmission with the channel identifer you specify.
- [func setAccessoryButtonEventsEnabled(Bool, channelUUID: UUID, completionHandler: (((any Error)?) -> Void)?)](./setaccessorybuttoneventsenabled%28_,channeluuid,completionhandler%29.md)
  Maps supported accessory button events to actions that begin and end transmission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanager/stoptransmitting(channeluuid:))*