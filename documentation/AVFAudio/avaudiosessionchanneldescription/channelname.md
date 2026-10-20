# channelName

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The descriptive name for the channel.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var channelName: String { get }
```

```objc
@property (nonatomic, readonly) NSString * channelName;
```

## See Also

### Getting the channel information
- [var channelNumber: Int](./channelnumber.md)
  The index of this channel in its owning port’s array of channels.
- [var owningPortUID: String](./owningportuid.md)
  The unique identifier (UID) for this channel’s owning port.
- [var channelLabel: AudioChannelLabel](./channellabel.md)
  A description of the physical location of this channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionchanneldescription/channelname)*