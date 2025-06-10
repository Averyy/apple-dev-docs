# AVAudioSessionChannelDescription

**Framework**: AVFAudio  
**Kind**: class

A class that describes a hardware channel on the current device.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioSessionChannelDescription
```

## Topics

### Getting the Channel Information
- [var channelName: String](avaudiosessionchanneldescription/channelname.md)
  The descriptive name for the channel.
- [var channelNumber: Int](avaudiosessionchanneldescription/channelnumber.md)
  The index of this channel in its owning port’s array of channels.
- [var owningPortUID: String](avaudiosessionchanneldescription/owningportuid.md)
  The unique identifier (UID) for this channel’s owning port.
- [var channelLabel: AudioChannelLabel](avaudiosessionchanneldescription/channellabel.md)
  A description of the physical location of this channel.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var portName: String](avaudiosessionportdescription/portname.md)
  A descriptive name for the port.
- [var portType: AVAudioSession.Port](avaudiosessionportdescription/porttype.md)
  The type of the port.
- [AVAudioSession.Port](avaudiosession/port.md)
  A structure that defines the available input and output port types.
- [var channels: [AVAudioSessionChannelDescription]?](avaudiosessionportdescription/channels.md)
  An array of channel objects that describe the port’s input or output channels.
- [var uid: String](avaudiosessionportdescription/uid.md)
  A system-assigned unique identifier (UID) for the port.
- [var hasHardwareVoiceCallProcessing: Bool](avaudiosessionportdescription/hashardwarevoicecallprocessing.md)
  A Boolean value that indicates whether the associated hardware port has built-in processing for two-way voice communication.
- [var isSpatialAudioEnabled: Bool](avaudiosessionportdescription/isspatialaudioenabled.md)
  A Boolean value that indicates whether the port supports spatial audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionchanneldescription)*