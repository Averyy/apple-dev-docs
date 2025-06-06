# leaveChannel(channelUUID:)

**Framework**: Push to Talk  
**Kind**: method

Leaves a channel with the identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func leaveChannel(channelUUID: UUID)
```

#### Discussion

If successful, you receive a callback from [`channelManager(_:didLeaveChannel:reason:)`](ptchannelmanagerdelegate/channelmanager(_:didleavechannel:reason:).md) with `PTChannelLeaveReason.programmaticRequest`; otherwise, you receive a failure reason through [`channelManager(_:failedToLeaveChannel:error:)`](ptchannelmanagerdelegate/channelmanager(_:failedtoleavechannel:error:).md).

## Parameters

- `channelUUID`: The channel identifier.

## See Also

- [func requestJoinChannel(channelUUID: UUID, descriptor: PTChannelDescriptor)](ptchannelmanager/requestjoinchannel(channeluuid:descriptor:).md)
  Joins a channel with the identifier and descriptor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanager/leavechannel(channeluuid:))*