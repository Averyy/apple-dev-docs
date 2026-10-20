# channelManager(_:channelUUID:didEndTransmittingFrom:)

**Framework**: Push to Talk  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the observer that transmission ended.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func channelManager(_ channelManager: PTChannelManager, channelUUID: UUID, didEndTransmittingFrom source: PTChannelTransmitRequestSource)
```

```objc
- (void) channelManager:(PTChannelManager *) channelManager channelUUID:(NSUUID *) channelUUID didEndTransmittingFromSource:(PTChannelTransmitRequestSource) source;
```

## Mentions

- [Creating a Push to Talk app](../creating-a-push-to-talk-app.md)

#### Discussion

The system calls this method when the user stops pressing the talk button in the user interface, a programmatic transmit ends, or transmission ends from a hands-free accessory button release.

## Parameters

- `channelManager`: The channel manager.
- `channelUUID`: The channel identifier.
- `source`: The transmission request source.

## See Also

### Beginning or ending transmission
- [func channelManager(PTChannelManager, channelUUID: UUID, didBeginTransmittingFrom: PTChannelTransmitRequestSource)](./channelmanager%28_,channeluuid,didbegintransmittingfrom%29.md)
  Tells the observer that transmission began.
- [func channelManager(PTChannelManager, failedToBeginTransmittingInChannel: UUID, error: any Error)](./channelmanager%28_,failedtobegintransmittinginchannel,error%29.md)
  Tells the observer that transmission failed to begin.
- [func channelManager(PTChannelManager, failedToStopTransmittingInChannel: UUID, error: any Error)](./channelmanager%28_,failedtostoptransmittinginchannel,error%29.md)
  Tells the observer that transmission failed to stop.
- [func incomingServiceUpdatePush(channelManager: PTChannelManager, channelUUID: UUID, pushPayload: [String : Any], isHighPriority: Bool, remainingHighPriorityBudget: Int, completion: () -> Void)](./incomingserviceupdatepush%28channelmanager,channeluuid,pushpayload,ishighpriority,remaininghighprioritybudget,completion%29.md)
  Extracts the service update data from the notification’s payload to perform the relevant task for that data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate/channelmanager(_:channeluuid:didendtransmittingfrom:))*