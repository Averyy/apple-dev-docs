# PTChannelManagerDelegate

**Framework**: Push to Talk  
**Kind**: protocol

A type that represents your life cycle of a channel manager.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
protocol PTChannelManagerDelegate : NSObjectProtocol
```

## Topics

### Beginning or ending transmission
- [func channelManager(PTChannelManager, channelUUID: UUID, didBeginTransmittingFrom: PTChannelTransmitRequestSource)](ptchannelmanagerdelegate/channelmanager(_:channeluuid:didbegintransmittingfrom:).md)
  Tells the observer that transmission began.
- [func channelManager(PTChannelManager, channelUUID: UUID, didEndTransmittingFrom: PTChannelTransmitRequestSource)](ptchannelmanagerdelegate/channelmanager(_:channeluuid:didendtransmittingfrom:).md)
  Tells the observer that transmission ended.
- [func channelManager(PTChannelManager, failedToBeginTransmittingInChannel: UUID, error: any Error)](ptchannelmanagerdelegate/channelmanager(_:failedtobegintransmittinginchannel:error:).md)
  Tells the observer that transmission failed to begin.
- [func channelManager(PTChannelManager, failedToStopTransmittingInChannel: UUID, error: any Error)](ptchannelmanagerdelegate/channelmanager(_:failedtostoptransmittinginchannel:error:).md)
  Tells the observer that transmission failed to stop.
- [func incomingServiceUpdatePush(channelManager: PTChannelManager, channelUUID: UUID, pushPayload: [String : Any], isHighPriority: Bool, remainingHighPriorityBudget: Int, completion: () -> Void)](ptchannelmanagerdelegate/incomingserviceupdatepush(channelmanager:channeluuid:pushpayload:ishighpriority:remaininghighprioritybudget:completion:).md)
  Extracts the service update data from the notification’s payload to perform the relevant task for that data.
### Activating and deactivating the audio session
- [func channelManager(PTChannelManager, didActivate: AVAudioSession)](ptchannelmanagerdelegate/channelmanager(_:didactivate:).md)
  Tells the observer the audio session activated.
- [func channelManager(PTChannelManager, didDeactivate: AVAudioSession)](ptchannelmanagerdelegate/channelmanager(_:diddeactivate:).md)
  Tells the observer the audio session deactivated.
### Joining and leaving a channel
- [func channelManager(PTChannelManager, didJoinChannel: UUID, reason: PTChannelJoinReason)](ptchannelmanagerdelegate/channelmanager(_:didjoinchannel:reason:).md)
  Tells the observer that the app successfully joined a Push to Talk channel.
- [func channelManager(PTChannelManager, didLeaveChannel: UUID, reason: PTChannelLeaveReason)](ptchannelmanagerdelegate/channelmanager(_:didleavechannel:reason:).md)
  Tells the observer that the app left a Push to Talk channel.
- [func channelManager(PTChannelManager, failedToJoinChannel: UUID, error: any Error)](ptchannelmanagerdelegate/channelmanager(_:failedtojoinchannel:error:).md)
  Tells the observer that the app failed to join a Push to Talk channel.
- [func channelManager(PTChannelManager, failedToLeaveChannel: UUID, error: any Error)](ptchannelmanagerdelegate/channelmanager(_:failedtoleavechannel:error:).md)
  Tells the observer that the app failed to leave a Push to Talk channel.
### Getting a push token
- [func channelManager(PTChannelManager, receivedEphemeralPushToken: Data)](ptchannelmanagerdelegate/channelmanager(_:receivedephemeralpushtoken:).md)
  Tells the observer that the app received a push token after you create a channel manager.
### Handling the push result
- [func incomingPushResult(channelManager: PTChannelManager, channelUUID: UUID, pushPayload: [String : Any]) -> PTPushResult](ptchannelmanagerdelegate/incomingpushresult(channelmanager:channeluuid:pushpayload:).md)
  Tells the observer that the app has a push available to handle.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [enum PTTransmissionMode](pttransmissionmode.md)
  Identifies the type of audio transmission modes.
- [enum PTServiceStatus](ptservicestatus.md)
  Identifies the type that indicates the status of the service.
- [enum PTChannelJoinReason](ptchanneljoinreason.md)
  Identifies the type that indicates the join reason.
- [enum PTChannelLeaveReason](ptchannelleavereason.md)
  Identifies the type that indicates the leave reason.
- [enum PTChannelTransmitRequestSource](ptchanneltransmitrequestsource.md)
  Identifies the type that indicates the transmission request source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate)*