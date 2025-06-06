# channelManager(_:failedToBeginTransmittingInChannel:error:)

**Framework**: Push to Talk  
**Kind**: method

Tells the observer that transmission failed to begin.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
optional func channelManager(_ channelManager: PTChannelManager, failedToBeginTransmittingInChannel channelUUID: UUID, error: any Error)
```

## Mentions

- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)

## Parameters

- `channelManager`: The channel manager.
- `channelUUID`: The channel identifier.
- `error`: The error that indicates the failure reason.

## See Also

- [func channelManager(PTChannelManager, channelUUID: UUID, didBeginTransmittingFrom: PTChannelTransmitRequestSource)](ptchannelmanagerdelegate/channelmanager(_:channeluuid:didbegintransmittingfrom:).md)
  Tells the observer that transmission began.
- [func channelManager(PTChannelManager, channelUUID: UUID, didEndTransmittingFrom: PTChannelTransmitRequestSource)](ptchannelmanagerdelegate/channelmanager(_:channeluuid:didendtransmittingfrom:).md)
  Tells the observer that transmission ended.
- [func channelManager(PTChannelManager, failedToStopTransmittingInChannel: UUID, error: any Error)](ptchannelmanagerdelegate/channelmanager(_:failedtostoptransmittinginchannel:error:).md)
  Tells the observer that transmission failed to stop.
- [func incomingServiceUpdatePush(channelManager: PTChannelManager, channelUUID: UUID, pushPayload: [String : Any], isHighPriority: Bool, remainingHighPriorityBudget: Int, completion: () -> Void)](ptchannelmanagerdelegate/incomingserviceupdatepush(channelmanager:channeluuid:pushpayload:ishighpriority:remaininghighprioritybudget:completion:).md)
  Extracts the service update data from the notification’s payload to perform the relevant task for that data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate/channelmanager(_:failedtobegintransmittinginchannel:error:))*