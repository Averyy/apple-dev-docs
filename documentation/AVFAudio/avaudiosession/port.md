# AVAudioSession.Port

**Framework**: AVFAudio  
**Kind**: struct

A structure that defines the available input and output port types.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct Port
```

## Topics

### Getting Input Ports
- [static let builtInMic: AVAudioSession.Port](avaudiosession/port/builtinmic.md)
  An input from a device’s built-in microphone.
- [static let continuityMicrophone: AVAudioSession.Port](avaudiosession/port/continuitymicrophone.md)
  An input from a Continuity Microphone on Apple TV.
- [static let headsetMic: AVAudioSession.Port](avaudiosession/port/headsetmic.md)
  An input from a wired headset’s built-in microphone.
- [static let lineIn: AVAudioSession.Port](avaudiosession/port/linein.md)
  A line-level input from the dock connector.
### Getting Output Ports
- [static let airPlay: AVAudioSession.Port](avaudiosession/port/airplay.md)
  An output to an AirPlay device.
- [static let bluetoothA2DP: AVAudioSession.Port](avaudiosession/port/bluetootha2dp.md)
  An output to a Bluetooth A2DP device.
- [static let bluetoothLE: AVAudioSession.Port](avaudiosession/port/bluetoothle.md)
  An output to a Bluetooth Low Energy (LE) device.
- [static let builtInReceiver: AVAudioSession.Port](avaudiosession/port/builtinreceiver.md)
  An output to the speaker you hold to your ear when you’re on a phone call.
- [static let builtInSpeaker: AVAudioSession.Port](avaudiosession/port/builtinspeaker.md)
  An output to the device’s built-in speaker.
- [static let HDMI: AVAudioSession.Port](avaudiosession/port/hdmi.md)
  An output to a High-Definition Multimedia Interface (HDMI) device.
- [static let headphones: AVAudioSession.Port](avaudiosession/port/headphones.md)
  An output to wired headphones.
- [static let lineOut: AVAudioSession.Port](avaudiosession/port/lineout.md)
  A line-level output to the dock connector.
### Getting I/O Ports
- [static let AVB: AVAudioSession.Port](avaudiosession/port/avb.md)
  An I/O connection to an Audio Video Bridging (AVB) device.
- [static let PCI: AVAudioSession.Port](avaudiosession/port/pci.md)
  An I/O connection to a Peripheral Component Interconnect (PCI) device.
- [static let bluetoothHFP: AVAudioSession.Port](avaudiosession/port/bluetoothhfp.md)
  An I/O connection to a Bluetooth Hands-Free Profile device.
- [static let carAudio: AVAudioSession.Port](avaudiosession/port/caraudio.md)
  An I/O connection through Car Audio.
- [static let displayPort: AVAudioSession.Port](avaudiosession/port/displayport.md)
  An I/O connection to a DisplayPort device.
- [static let fireWire: AVAudioSession.Port](avaudiosession/port/firewire.md)
  An I/O connection to a FireWire device.
- [static let thunderbolt: AVAudioSession.Port](avaudiosession/port/thunderbolt.md)
  An I/O connection to a Thunderbolt device.
- [static let usbAudio: AVAudioSession.Port](avaudiosession/port/usbaudio.md)
  An I/O connection to a Universal Serial Bus (USB) device.
- [static let virtual: AVAudioSession.Port](avaudiosession/port/virtual.md)
  An I/O connection that doesn’t correspond to physical audio hardware.
### Initializers
- [init(rawValue: String)](avaudiosession/port/init(rawvalue:).md)
  Creates a new instance with the raw value you specify.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var portName: String](avaudiosessionportdescription/portname.md)
  A descriptive name for the port.
- [var portType: AVAudioSession.Port](avaudiosessionportdescription/porttype.md)
  The type of the port.
- [var channels: [AVAudioSessionChannelDescription]?](avaudiosessionportdescription/channels.md)
  An array of channel objects that describe the port’s input or output channels.
- [class AVAudioSessionChannelDescription](avaudiosessionchanneldescription.md)
  A class that describes a hardware channel on the current device.
- [var uid: String](avaudiosessionportdescription/uid.md)
  A system-assigned unique identifier (UID) for the port.
- [var hasHardwareVoiceCallProcessing: Bool](avaudiosessionportdescription/hashardwarevoicecallprocessing.md)
  A Boolean value that indicates whether the associated hardware port has built-in processing for two-way voice communication.
- [var isSpatialAudioEnabled: Bool](avaudiosessionportdescription/isspatialaudioenabled.md)
  A Boolean value that indicates whether the port supports spatial audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/port)*