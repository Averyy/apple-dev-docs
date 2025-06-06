# PTChannelRestorationDelegate

**Framework**: Push to Talk  
**Kind**: protocol

A type that represents the channel restoration behavior.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
protocol PTChannelRestorationDelegate : NSObjectProtocol
```

## Mentions

- [Creating a Push to Talk app](creating-a-push-to-talk-app.md)

## Topics

### Getting the channel descriptor
- [func channelDescriptor(restoredChannelUUID: UUID) -> PTChannelDescriptor](ptchannelrestorationdelegate/channeldescriptor(restoredchanneluuid:).md)
  Tells your observer the system restored the channel.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PTChannelDescriptor](ptchanneldescriptor.md)
  An object that describes a channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pushtotalk/ptchannelrestorationdelegate)*