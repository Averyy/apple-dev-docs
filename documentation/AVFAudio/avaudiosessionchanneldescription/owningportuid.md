# owningPortUID

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSString * owningPortUID;
```

## Discussion

You can use the value of this property along with the value of the [`channelNumber`](./channelnumber.md) property to communicate with specific hardware channels.

## See Also

### Getting the channel information
- [var channelName: String](./channelname.md)
  The descriptive name for the channel.
- [var channelNumber: Int](./channelnumber.md)
  The index of this channel in its owning port’s array of channels.
- [var channelLabel: AudioChannelLabel](./channellabel.md)
  A description of the physical location of this channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionchanneldescription/owningportuid)*