# owningPortUID

**Framework**: AVFAudio  
**Kind**: property

The unique identifier (UID) for this channel’s owning port.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var owningPortUID: String { get }
```

#### Discussion

You can use the value of this property along with the value of the [`channelNumber`](avaudiosessionchanneldescription/channelnumber.md) property to communicate with specific hardware channels.

## See Also

- [var channelName: String](avaudiosessionchanneldescription/channelname.md)
  The descriptive name for the channel.
- [var channelNumber: Int](avaudiosessionchanneldescription/channelnumber.md)
  The index of this channel in its owning port’s array of channels.
- [var channelLabel: AudioChannelLabel](avaudiosessionchanneldescription/channellabel.md)
  A description of the physical location of this channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionchanneldescription/owningportuid)*