# channelManager(_:channelUUID:didEndTransmittingFrom:)

**Framework**: Push to Talk  
**Kind**: method  
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

## Mentions

- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)

#### Discussion

The system calls this method when the user stops pressing the talk button in the user interface, a programmatic transmit ends, or transmission ends from a hands-free accessory button release.

## Parameters

- `channelManager`: The channel manager.
- `channelUUID`: The channel identifier.
- `source`: The transmission request source.

## See Also

- [func channelManager(PTChannelManager, channelUUID: UUID, didBeginTransmittingFrom: PTChannelTransmitRequestSource)](ptchannelmanagerdelegate/channelmanager(_:channeluuid:didbegintransmittingfrom:).md)
  Tells the observer that transmission began.
- [func channelManager(PTChannelManager, failedToBeginTransmittingInChannel: UUID, error: any Error)](ptchannelmanagerdelegate/channelmanager(_:failedtobegintransmittinginchannel:error:).md)
  Tells the observer that transmission failed to begin.
- [func channelManager(PTChannelManager, failedToStopTransmittingInChannel: UUID, error: any Error)](ptchannelmanagerdelegate/channelmanager(_:failedtostoptransmittinginchannel:error:).md)
  Tells the observer that transmission failed to stop.
- [func incomingServiceUpdatePush(channelManager: PTChannelManager, channelUUID: UUID, pushPayload: [String : Any], isHighPriority: Bool, remainingHighPriorityBudget: Int, completion: () -> Void)](ptchannelmanagerdelegate/incomingserviceupdatepush(channelmanager:channeluuid:pushpayload:ishighpriority:remaininghighprioritybudget:completion:).md)
  Extracts the service update data from the notification’s payload to perform the relevant task for that data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate/channelmanager(_:channeluuid:didendtransmittingfrom:))*