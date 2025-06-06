# channelManager(_:failedToLeaveChannel:error:)

**Framework**: Push to Talk  
**Kind**: method

Tells the observer that the app failed to leave a Push to Talk channel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
optional func channelManager(_ channelManager: PTChannelManager, failedToLeaveChannel channelUUID: UUID, error: any Error)
```

## Parameters

- `channelManager`: The channel manager.
- `channelUUID`: The channel identifier.
- `error`: The error that indicates the failure reason.

## See Also

- [func channelManager(PTChannelManager, didJoinChannel: UUID, reason: PTChannelJoinReason)](ptchannelmanagerdelegate/channelmanager(_:didjoinchannel:reason:).md)
  Tells the observer that the app successfully joined a Push to Talk channel.
- [func channelManager(PTChannelManager, didLeaveChannel: UUID, reason: PTChannelLeaveReason)](ptchannelmanagerdelegate/channelmanager(_:didleavechannel:reason:).md)
  Tells the observer that the app left a Push to Talk channel.
- [func channelManager(PTChannelManager, failedToJoinChannel: UUID, error: any Error)](ptchannelmanagerdelegate/channelmanager(_:failedtojoinchannel:error:).md)
  Tells the observer that the app failed to join a Push to Talk channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate/channelmanager(_:failedtoleavechannel:error:))*