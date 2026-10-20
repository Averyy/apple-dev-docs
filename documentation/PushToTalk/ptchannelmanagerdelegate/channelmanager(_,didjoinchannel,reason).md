# channelManager(_:didJoinChannel:reason:)

**Framework**: Push to Talk  
**Kind**: method  
**Required**: Yes

Tells the observer that the app successfully joined a Push to Talk channel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func channelManager(_ channelManager: PTChannelManager, didJoinChannel channelUUID: UUID, reason: PTChannelJoinReason)
```

## Parameters

- `channelManager`: The channel manager.
- `channelUUID`: The channel identifier.
- `reason`: The join reason.

## See Also

- [func channelManager(PTChannelManager, didLeaveChannel: UUID, reason: PTChannelLeaveReason)](ptchannelmanagerdelegate/channelmanager(_:didleavechannel:reason:).md)
  Tells the observer that the app left a Push to Talk channel.
- [func channelManager(PTChannelManager, failedToJoinChannel: UUID, error: any Error)](ptchannelmanagerdelegate/channelmanager(_:failedtojoinchannel:error:).md)
  Tells the observer that the app failed to join a Push to Talk channel.
- [func channelManager(PTChannelManager, failedToLeaveChannel: UUID, error: any Error)](ptchannelmanagerdelegate/channelmanager(_:failedtoleavechannel:error:).md)
  Tells the observer that the app failed to leave a Push to Talk channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanagerdelegate/channelmanager(_:didjoinchannel:reason:))*