# channelManager(_:failedToLeaveChannel:error:)

**Framework**: Push to Talk  
**Kind**: method  
**Role**: Instance Method

Tells the observer that the app failed to leave a Push to Talk channel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
optional func channelManager(_ channelManager: PTChannelManager, failedToLeaveChannel channelUUID: UUID, error: any Error)
```

```objc
- (void) channelManager:(PTChannelManager *) channelManager failedToLeaveChannelWithUUID:(NSUUID *) channelUUID error:(NSError *) error;
```

## Parameters

- `channelManager`: The channel manager.
- `channelUUID`: The channel identifier.
- `error`: The error that indicates the failure reason.

## See Also

### Joining and leaving a channel
- [func channelManager(PTChannelManager, didJoinChannel: UUID, reason: PTChannelJoinReason)](./channelmanager%28_,didjoinchannel,reason%29.md)
  Tells the observer that the app successfully joined a Push to Talk channel.
- [func channelManager(PTChannelManager, didLeaveChannel: UUID, reason: PTChannelLeaveReason)](./channelmanager%28_,didleavechannel,reason%29.md)
  Tells the observer that the app left a Push to Talk channel.
- [func channelManager(PTChannelManager, failedToJoinChannel: UUID, error: any Error)](./channelmanager%28_,failedtojoinchannel,error%29.md)
  Tells the observer that the app failed to join a Push to Talk channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate/channelmanager(_:failedtoleavechannel:error:))*