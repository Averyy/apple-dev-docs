# fireWire

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

An I/O connection to a FireWire device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static let fireWire: AVAudioSession.Port
```

```c
extern AVAudioSessionPort const AVAudioSessionPortFireWire;
```

## See Also

### Getting I/O ports
- [static let AVB: AVAudioSession.Port](./avb.md)
  An I/O connection to an Audio Video Bridging (AVB) device.
- [static let PCI: AVAudioSession.Port](./pci.md)
  An I/O connection to a Peripheral Component Interconnect (PCI) device.
- [static let bluetoothHFP: AVAudioSession.Port](./bluetoothhfp.md)
  An I/O connection to a Bluetooth Hands-Free Profile device.
- [static let carAudio: AVAudioSession.Port](./caraudio.md)
  An I/O connection through Car Audio.
- [static let displayPort: AVAudioSession.Port](./displayport.md)
  An I/O connection to a DisplayPort device.
- [static let mediaDeviceExtension: AVAudioSession.Port](./mediadeviceextension.md)
  Output to a media device vended through a system-wide extension that the user has installed
- [static let thunderbolt: AVAudioSession.Port](./thunderbolt.md)
  An I/O connection to a Thunderbolt device.
- [static let usbAudio: AVAudioSession.Port](./usbaudio.md)
  An I/O connection to a Universal Serial Bus (USB) device.
- [static let virtual: AVAudioSession.Port](./virtual.md)
  An I/O connection that doesn’t correspond to physical audio hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/port/firewire)*