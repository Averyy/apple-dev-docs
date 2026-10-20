# channelManager(_:didLeaveChannel:reason:)

**Framework**: Push to Talk  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the observer that the app left a Push to Talk channel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func channelManager(_ channelManager: PTChannelManager, didLeaveChannel channelUUID: UUID, reason: PTChannelLeaveReason)
```

```objc
- (void) channelManager:(PTChannelManager *) channelManager didLeaveChannelWithUUID:(NSUUID *) channelUUID reason:(PTChannelLeaveReason) reason;
```

## Parameters

- `channelManager`: The channel manager.
- `channelUUID`: The channel identifier.
- `reason`: The leave reason.

## See Also

### Joining and leaving a channel
- [func channelManager(PTChannelManager, didJoinChannel: UUID, reason: PTChannelJoinReason)](./channelmanager%28_,didjoinchannel,reason%29.md)
  Tells the observer that the app successfully joined a Push to Talk channel.
- [func channelManager(PTChannelManager, failedToJoinChannel: UUID, error: any Error)](./channelmanager%28_,failedtojoinchannel,error%29.md)
  Tells the observer that the app failed to join a Push to Talk channel.
- [func channelManager(PTChannelManager, failedToLeaveChannel: UUID, error: any Error)](./channelmanager%28_,failedtoleavechannel,error%29.md)
  Tells the observer that the app failed to leave a Push to Talk channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate/channelmanager(_:didleavechannel:reason:))*