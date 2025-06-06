# requestJoinChannel(channelUUID:descriptor:)

**Framework**: Push to Talk  
**Kind**: method

Joins a channel with the identifier and descriptor you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func requestJoinChannel(channelUUID: UUID, descriptor: PTChannelDescriptor)
```

## Mentions

- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)

#### Discussion

If successful, you receive a callback from [`channelManager(_:didJoinChannel:reason:)`](ptchannelmanagerdelegate/channelmanager(_:didjoinchannel:reason:).md) with `PTChannelJoinReasonProgrammaticRequest`; otherwise, you receive a failure reason through [`channelManager(_:failedToJoinChannel:error:)`](ptchannelmanagerdelegate/channelmanager(_:failedtojoinchannel:error:).md).

> **Note**:  You can only join a channel in the foreground.

 You can only join a channel in the foreground.

The framework uses shared system resources, so only one PTT channel can be active on the system at a time.

```swift
// Create a descriptor an app uses to join a channel.    
let channelImage = UIImage(named: "ChannelImage")    
channelDescriptor = PTChannelDescriptor(name: "The channel name",                                                                             
                                        image: channelImage)

// Join a channel with a unique identifier and descriptor.
channelManager.requestJoinChannel(channelUUID: channelUUID,
                                  descriptor: channelDescriptor)
```

The system uses the same unique identifier when interacting with the manager throughout the life of the channel, so when joining a channel, store the descriptor and UUID for later use.

## Parameters

- `channelUUID`: The channel identifier.
- `descriptor`: The channel description.

## See Also

- [func leaveChannel(channelUUID: UUID)](ptchannelmanager/leavechannel(channeluuid:).md)
  Leaves a channel with the identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelmanager/requestjoinchannel(channeluuid:descriptor:))*