# AVAudioSession.Port

**Framework**: AVFAudio  
**Kind**: struct  
**Role**: Structure

A structure that defines the available input and output port types.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct Port
```

```c
typedef NSString * AVAudioSessionPort;
```

## Topics

### Creating a port
- [init(rawValue: String)](./port/init%28rawvalue%29.md)
  Creates a new instance with the raw value you specify.
### Getting input ports
- [static let builtInMic: AVAudioSession.Port](./port/builtinmic.md)
  An input from a device’s built-in microphone.
- [static let continuityMicrophone: AVAudioSession.Port](./port/continuitymicrophone.md)
  An input from a Continuity Microphone on Apple TV.
- [static let headsetMic: AVAudioSession.Port](./port/headsetmic.md)
  An input from a wired headset’s built-in microphone.
- [static let lineIn: AVAudioSession.Port](./port/linein.md)
  A line-level input from the dock connector.
### Getting output ports
- [static let airPlay: AVAudioSession.Port](./port/airplay.md)
  An output to an AirPlay device.
- [static let bluetoothA2DP: AVAudioSession.Port](./port/bluetootha2dp.md)
  An output to a Bluetooth A2DP device.
- [static let bluetoothLE: AVAudioSession.Port](./port/bluetoothle.md)
  An output to a Bluetooth Low Energy (LE) device.
- [static let builtInReceiver: AVAudioSession.Port](./port/builtinreceiver.md)
  An output to the speaker you hold to your ear when you’re on a phone call.
- [static let builtInSpeaker: AVAudioSession.Port](./port/builtinspeaker.md)
  An output to the device’s built-in speaker.
- [static let HDMI: AVAudioSession.Port](./port/hdmi.md)
  An output to a High-Definition Multimedia Interface (HDMI) device.
- [static let headphones: AVAudioSession.Port](./port/headphones.md)
  An output to wired headphones.
- [static let lineOut: AVAudioSession.Port](./port/lineout.md)
  A line-level output to the dock connector.
- [static let mediaDeviceExtension: AVAudioSession.Port](./port/mediadeviceextension.md)
  Output to a media device vended through a system-wide extension that the user has installed
### Getting I/O ports
- [static let AVB: AVAudioSession.Port](./port/avb.md)
  An I/O connection to an Audio Video Bridging (AVB) device.
- [static let PCI: AVAudioSession.Port](./port/pci.md)
  An I/O connection to a Peripheral Component Interconnect (PCI) device.
- [static let bluetoothHFP: AVAudioSession.Port](./port/bluetoothhfp.md)
  An I/O connection to a Bluetooth Hands-Free Profile device.
- [static let carAudio: AVAudioSession.Port](./port/caraudio.md)
  An I/O connection through Car Audio.
- [static let displayPort: AVAudioSession.Port](./port/displayport.md)
  An I/O connection to a DisplayPort device.
- [static let fireWire: AVAudioSession.Port](./port/firewire.md)
  An I/O connection to a FireWire device.
- [static let mediaDeviceExtension: AVAudioSession.Port](./port/mediadeviceextension.md)
  Output to a media device vended through a system-wide extension that the user has installed
- [static let thunderbolt: AVAudioSession.Port](./port/thunderbolt.md)
  An I/O connection to a Thunderbolt device.
- [static let usbAudio: AVAudioSession.Port](./port/usbaudio.md)
  An I/O connection to a Universal Serial Bus (USB) device.
- [static let virtual: AVAudioSession.Port](./port/virtual.md)
  An I/O connection that doesn’t correspond to physical audio hardware.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the port attributes
- [var portName: String](../avaudiosessionportdescription/portname.md)
  A descriptive name for the port.
- [var portType: AVAudioSession.Port](../avaudiosessionportdescription/porttype.md)
  The type of the port.
- [var channels: [AVAudioSessionChannelDescription]?](../avaudiosessionportdescription/channels.md)
  An array of channel objects that describe the port’s input or output channels.
- [class AVAudioSessionChannelDescription](../avaudiosessionchanneldescription.md)
  A class that describes a hardware channel on the current device.
- [var uid: String](../avaudiosessionportdescription/uid.md)
  A system-assigned unique identifier (UID) for the port.
- [var hasHardwareVoiceCallProcessing: Bool](../avaudiosessionportdescription/hashardwarevoicecallprocessing.md)
  A Boolean value that indicates whether the associated hardware port has built-in processing for two-way voice communication.
- [var isSpatialAudioEnabled: Bool](../avaudiosessionportdescription/isspatialaudioenabled.md)
  A Boolean value that indicates whether the port supports spatial audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/port)*