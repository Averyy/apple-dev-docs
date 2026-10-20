# leaveChannel(channelUUID:)

**Framework**: Push to Talk  
**Kind**: method  
**Role**: Instance Method

Leaves a channel with the identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func leaveChannel(channelUUID: UUID)
```

```objc
- (void) leaveChannelWithUUID:(NSUUID *) channelUUID;
```

#### Discussion

If successful, you receive a callback from [`channelManager(_:didLeaveChannel:reason:)`](../ptchannelmanagerdelegate/channelmanager%28_,didleavechannel,reason%29.md) with `PTChannelLeaveReason.programmaticRequest`; otherwise, you receive a failure reason through [`channelManager(_:failedToLeaveChannel:error:)`](../ptchannelmanagerdelegate/channelmanager%28_,failedtoleavechannel,error%29.md).

## Parameters

- `channelUUID`: The channel identifier.

## See Also

### Joining and leaving a channel
- [func requestJoinChannel(channelUUID: UUID, descriptor: PTChannelDescriptor)](./requestjoinchannel%28channeluuid,descriptor%29.md)
  Joins a channel with the identifier and descriptor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanager/leavechannel(channeluuid:))*