# portType

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The type of the port.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var portType: AVAudioSession.Port { get }
```

```objc
@property (nonatomic, readonly) AVAudioSessionPort portType;
```

#### Discussion

The value of this property can be any of the constants declared in `Input Ports`, `Output Port Types`, or `I/O Port Types`.

## See Also

### Getting the port attributes
- [var portName: String](./portname.md)
  A descriptive name for the port.
- [AVAudioSession.Port](../avaudiosession/port.md)
  A structure that defines the available input and output port types.
- [var channels: [AVAudioSessionChannelDescription]?](./channels.md)
  An array of channel objects that describe the port’s input or output channels.
- [class AVAudioSessionChannelDescription](../avaudiosessionchanneldescription.md)
  A class that describes a hardware channel on the current device.
- [var uid: String](./uid.md)
  A system-assigned unique identifier (UID) for the port.
- [var hasHardwareVoiceCallProcessing: Bool](./hashardwarevoicecallprocessing.md)
  A Boolean value that indicates whether the associated hardware port has built-in processing for two-way voice communication.
- [var isSpatialAudioEnabled: Bool](./isspatialaudioenabled.md)
  A Boolean value that indicates whether the port supports spatial audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionportdescription/porttype)*