# channelNumber

**Framework**: AVFAudio  
**Kind**: property

The index of this channel in its owning port’s array of channels.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var channelNumber: Int { get }
```

#### Discussion

You can use the value in this property to identify the channel during audio routing. However, the value of this property isn’t guaranteed to persist across route changes.

## See Also

- [var channelName: String](avaudiosessionchanneldescription/channelname.md)
  The descriptive name for the channel.
- [var owningPortUID: String](avaudiosessionchanneldescription/owningportuid.md)
  The unique identifier (UID) for this channel’s owning port.
- [var channelLabel: AudioChannelLabel](avaudiosessionchanneldescription/channellabel.md)
  A description of the physical location of this channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionchanneldescription/channelnumber)*