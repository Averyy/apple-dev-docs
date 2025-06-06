# channelDescriptor(restoredChannelUUID:)

**Framework**: Push to Talk  
**Kind**: method  
**Required**: Yes

Tells your observer the system restored the channel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func channelDescriptor(restoredChannelUUID channelUUID: UUID) -> PTChannelDescriptor
```

## Mentions

- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)

#### Return Value

An object that describes a channel you associate with the unique identifier.

#### Discussion

If the system tracks a channel, but there’s no pending push, the system calls this method when it’s unable to use cached data. If your app launches because of user interaction with the system user interface, the system calls this method as long as there’s no pending push.

## Parameters

- `channelUUID`: The channel identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelrestorationdelegate/channeldescriptor(restoredchanneluuid:))*