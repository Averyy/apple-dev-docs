# channels

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

An array of channel objects that describe the port’s input or output channels.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var channels: [AVAudioSessionChannelDescription]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<AVAudioSessionChannelDescription *> * channels;
```

#### Discussion

The contents of this array may change if the audio session’s input or output channel count changes.

## See Also

### Getting the port attributes
- [var portName: String](./portname.md)
  A descriptive name for the port.
- [var portType: AVAudioSession.Port](./porttype.md)
  The type of the port.
- [AVAudioSession.Port](../avaudiosession/port.md)
  A structure that defines the available input and output port types.
- [class AVAudioSessionChannelDescription](../avaudiosessionchanneldescription.md)
  A class that describes a hardware channel on the current device.
- [var uid: String](./uid.md)
  A system-assigned unique identifier (UID) for the port.
- [var hasHardwareVoiceCallProcessing: Bool](./hashardwarevoicecallprocessing.md)
  A Boolean value that indicates whether the associated hardware port has built-in processing for two-way voice communication.
- [var isSpatialAudioEnabled: Bool](./isspatialaudioenabled.md)
  A Boolean value that indicates whether the port supports spatial audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionportdescription/channels)*