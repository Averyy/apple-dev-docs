# hasHardwareVoiceCallProcessing

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether the associated hardware port has built-in processing for two-way voice communication.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var hasHardwareVoiceCallProcessing: Bool { get }
```

#### Discussion

Applications that use their own proprietary voice-processing algorithms should use this property to decide when to disable processing. If your app uses Apple’s Voice Processing I/O unit (subtype `kAudioUnitSubType_VoiceProcessingIO`), the system automatically manages this for you.

## See Also

- [var portName: String](avaudiosessionportdescription/portname.md)
  A descriptive name for the port.
- [var portType: AVAudioSession.Port](avaudiosessionportdescription/porttype.md)
  The type of the port.
- [AVAudioSession.Port](avaudiosession/port.md)
  A structure that defines the available input and output port types.
- [var channels: [AVAudioSessionChannelDescription]?](avaudiosessionportdescription/channels.md)
  An array of channel objects that describe the port’s input or output channels.
- [class AVAudioSessionChannelDescription](avaudiosessionchanneldescription.md)
  A class that describes a hardware channel on the current device.
- [var uid: String](avaudiosessionportdescription/uid.md)
  A system-assigned unique identifier (UID) for the port.
- [var isSpatialAudioEnabled: Bool](avaudiosessionportdescription/isspatialaudioenabled.md)
  A Boolean value that indicates whether the port supports spatial audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionportdescription/hashardwarevoicecallprocessing)*