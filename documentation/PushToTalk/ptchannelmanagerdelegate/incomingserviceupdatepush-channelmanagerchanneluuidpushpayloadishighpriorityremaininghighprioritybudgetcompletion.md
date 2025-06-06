# incomingServiceUpdatePush(channelManager:channelUUID:pushPayload:isHighPriority:remainingHighPriorityBudget:completion:)

**Framework**: Push to Talk  
**Kind**: method

Extracts the service update data from the notification’s payload to perform the relevant task for that data.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+

## Declaration

```swift
optional func incomingServiceUpdatePush(channelManager: PTChannelManager, channelUUID: UUID, pushPayload: [String : Any], isHighPriority: Bool, remainingHighPriorityBudget: Int) async
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
optional func incomingServiceUpdatePush(channelManager: PTChannelManager, channelUUID: UUID, pushPayload: [String : Any], isHighPriority: Bool, remainingHighPriorityBudget: Int) async
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
optional func incomingServiceUpdatePush(channelManager: PTChannelManager, channelUUID: UUID, pushPayload: [String : Any], isHighPriority: Bool, remainingHighPriorityBudget: Int) async
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `channelManager`: The channel manager.
- `channelUUID`: The channel identifier.
- `pushPayload`: The push payload metadata.
- `isHighPriority`: A flag indicating if this notification is a high priority.
- `remainingHighPriorityBudget`: Monitors the number of remaining high-priority push notifications available to your app. Use low-priority push notifications (priority <= 5) whenever possible, as they aren’t subject to a budget limit.
- `completion`: Execute to inform the Push to Talk framework you’ve finished your task.

## See Also

- [func channelManager(PTChannelManager, channelUUID: UUID, didBeginTransmittingFrom: PTChannelTransmitRequestSource)](ptchannelmanagerdelegate/channelmanager(_:channeluuid:didbegintransmittingfrom:).md)
  Tells the observer that transmission began.
- [func channelManager(PTChannelManager, channelUUID: UUID, didEndTransmittingFrom: PTChannelTransmitRequestSource)](ptchannelmanagerdelegate/channelmanager(_:channeluuid:didendtransmittingfrom:).md)
  Tells the observer that transmission ended.
- [func channelManager(PTChannelManager, failedToBeginTransmittingInChannel: UUID, error: any Error)](ptchannelmanagerdelegate/channelmanager(_:failedtobegintransmittinginchannel:error:).md)
  Tells the observer that transmission failed to begin.
- [func channelManager(PTChannelManager, failedToStopTransmittingInChannel: UUID, error: any Error)](ptchannelmanagerdelegate/channelmanager(_:failedtostoptransmittinginchannel:error:).md)
  Tells the observer that transmission failed to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate/incomingserviceupdatepush(channelmanager:channeluuid:pushpayload:ishighpriority:remaininghighprioritybudget:completion:))*