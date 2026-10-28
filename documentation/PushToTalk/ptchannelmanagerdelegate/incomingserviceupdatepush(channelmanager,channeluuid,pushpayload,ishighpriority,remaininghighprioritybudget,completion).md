# incomingServiceUpdatePush(channelManager:channelUUID:pushPayload:isHighPriority:remainingHighPriorityBudget:completion:)

**Framework**: Push to Talk  
**Kind**: method  
**Role**: Instance Method

Extracts the service update data from the notification’s payload to perform the relevant task for that data.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+

## Declaration

```swift
optional func incomingServiceUpdatePush(channelManager: PTChannelManager, channelUUID: UUID, pushPayload: [String : Any], isHighPriority: Bool, remainingHighPriorityBudget: Int, completion: @escaping @Sendable () -> Void)
```

```swift
optional func incomingServiceUpdatePush(channelManager: PTChannelManager, channelUUID: UUID, pushPayload: [String : Any], isHighPriority: Bool, remainingHighPriorityBudget: Int) async
```

```objc
- (void) incomingServiceUpdatePushForChannelManager:(PTChannelManager *) channelManager channelUUID:(NSUUID *) channelUUID pushPayload:(NSDictionary<NSString *,id> *) pushPayload isHighPriority:(BOOL) isHighPriority remainingHighPriorityBudget:(NSInteger) remainingHighPriorityBudget withCompletionHandler:(void (^)()) completion;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> optional func incomingServiceUpdatePush(channelManager: PTChannelManager, channelUUID: UUID, pushPayload: [String : Any], isHighPriority: Bool, remainingHighPriorityBudget: Int) async
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `channelManager`: The channel manager.
- `channelUUID`: The channel identifier.
- `pushPayload`: The push payload metadata.
- `isHighPriority`: A flag indicating if this notification is a high priority.
- `remainingHighPriorityBudget`: Monitors the number of remaining high-priority push notifications available to your app. Use low-priority push notifications (priority <= 5) whenever possible, as they aren’t subject to a budget limit.
- `completion`: Execute to inform the Push to Talk framework you’ve finished your task.

## See Also

### Beginning or ending transmission
- [func channelManager(PTChannelManager, channelUUID: UUID, didBeginTransmittingFrom: PTChannelTransmitRequestSource)](./channelmanager%28_,channeluuid,didbegintransmittingfrom%29.md)
  Tells the observer that transmission began.
- [func channelManager(PTChannelManager, channelUUID: UUID, didEndTransmittingFrom: PTChannelTransmitRequestSource)](./channelmanager%28_,channeluuid,didendtransmittingfrom%29.md)
  Tells the observer that transmission ended.
- [func channelManager(PTChannelManager, failedToBeginTransmittingInChannel: UUID, error: any Error)](./channelmanager%28_,failedtobegintransmittinginchannel,error%29.md)
  Tells the observer that transmission failed to begin.
- [func channelManager(PTChannelManager, failedToStopTransmittingInChannel: UUID, error: any Error)](./channelmanager%28_,failedtostoptransmittinginchannel,error%29.md)
  Tells the observer that transmission failed to stop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate/incomingserviceupdatepush(channelmanager:channeluuid:pushpayload:ishighpriority:remaininghighprioritybudget:completion:))*