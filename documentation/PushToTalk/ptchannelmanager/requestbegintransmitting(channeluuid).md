# requestBeginTransmitting(channelUUID:)

**Framework**: Push to Talk  
**Kind**: method  
**Role**: Instance Method

Begins an audio transmission with the channel identifer you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func requestBeginTransmitting(channelUUID: UUID)
```

```objc
- (void) requestBeginTransmittingWithChannelUUID:(NSUUID *) channelUUID;
```

## Mentions

- [Creating a Push to Talk app](../creating-a-push-to-talk-app.md)

## Discussion

Your app can only begin a transmission when in the foreground, or following a [Core Bluetooth](../../CoreBluetooth/CoreBluetooth.md) event, such as when a wireless accessory button triggers a [Core Bluetooth](../../CoreBluetooth/CoreBluetooth.md) characteristic change. The user may also begin a transmission by using the Push to Talk system user interface.

If successful, you receive a callback from [`channelManager(_:channelUUID:didBeginTransmittingFrom:)`](../ptchannelmanagerdelegate/channelmanager%28_,channeluuid,didbegintransmittingfrom%29.md) with `PTChannelTransmitRequestSource.programmaticRequest`; otherwise, you receive a failure reason through [`channelManager(_:failedToBeginTransmittingInChannel:error:)`](../ptchannelmanagerdelegate/channelmanager%28_,failedtobegintransmittinginchannel,error%29.md).

## Parameters

- `channelUUID`: The channel identifier.

## See Also

### Starting and stopping transmission
- [func stopTransmitting(channelUUID: UUID)](./stoptransmitting%28channeluuid%29.md)
  Stops an audio transmission with the channel identifer you specify.
- [func setAccessoryButtonEventsEnabled(Bool, channelUUID: UUID, completionHandler: (((any Error)?) -> Void)?)](./setaccessorybuttoneventsenabled%28_,channeluuid,completionhandler%29.md)
  Maps supported accessory button events to actions that begin and end transmission.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanager/requestbegintransmitting(channeluuid:))*