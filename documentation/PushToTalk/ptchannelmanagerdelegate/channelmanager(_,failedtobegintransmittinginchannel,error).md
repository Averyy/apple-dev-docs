# channelManager(_:failedToBeginTransmittingInChannel:error:)

**Framework**: Push to Talk  
**Kind**: method  
**Role**: Instance Method

Tells the observer that transmission failed to begin.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
optional func channelManager(_ channelManager: PTChannelManager, failedToBeginTransmittingInChannel channelUUID: UUID, error: any Error)
```

```objc
- (void) channelManager:(PTChannelManager *) channelManager failedToBeginTransmittingInChannelWithUUID:(NSUUID *) channelUUID error:(NSError *) error;
```

## Mentions

- [Creating a Push to Talk app](../creating-a-push-to-talk-app.md)

## Parameters

- `channelManager`: The channel manager.
- `channelUUID`: The channel identifier.
- `error`: The error that indicates the failure reason.

## See Also

### Beginning or ending transmission
- [func channelManager(PTChannelManager, channelUUID: UUID, didBeginTransmittingFrom: PTChannelTransmitRequestSource)](./channelmanager%28_,channeluuid,didbegintransmittingfrom%29.md)
  Tells the observer that transmission began.
- [func channelManager(PTChannelManager, channelUUID: UUID, didEndTransmittingFrom: PTChannelTransmitRequestSource)](./channelmanager%28_,channeluuid,didendtransmittingfrom%29.md)
  Tells the observer that transmission ended.
- [func channelManager(PTChannelManager, failedToStopTransmittingInChannel: UUID, error: any Error)](./channelmanager%28_,failedtostoptransmittinginchannel,error%29.md)
  Tells the observer that transmission failed to stop.
- [func incomingServiceUpdatePush(channelManager: PTChannelManager, channelUUID: UUID, pushPayload: [String : Any], isHighPriority: Bool, remainingHighPriorityBudget: Int, completion: () -> Void)](./incomingserviceupdatepush%28channelmanager,channeluuid,pushpayload,ishighpriority,remaininghighprioritybudget,completion%29.md)
  Extracts the service update data from the notification’s payload to perform the relevant task for that data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate/channelmanager(_:failedtobegintransmittinginchannel:error:))*