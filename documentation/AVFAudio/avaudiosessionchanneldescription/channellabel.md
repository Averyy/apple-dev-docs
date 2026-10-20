# channelLabel

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

A description of the physical location of this channel.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var channelLabel: AudioChannelLabel { get }
```

```objc
@property (nonatomic, readonly) AudioChannelLabel channelLabel;
```

## See Also

### Getting the channel information
- [var channelName: String](./channelname.md)
  The descriptive name for the channel.
- [var channelNumber: Int](./channelnumber.md)
  The index of this channel in its owning port’s array of channels.
- [var owningPortUID: String](./owningportuid.md)
  The unique identifier (UID) for this channel’s owning port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionchanneldescription/channellabel)*