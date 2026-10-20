# headphones

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

An output to wired headphones.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let headphones: AVAudioSession.Port
```

```c
extern AVAudioSessionPort const AVAudioSessionPortHeadphones;
```

## See Also

### Getting output ports
- [static let airPlay: AVAudioSession.Port](./airplay.md)
  An output to an AirPlay device.
- [static let bluetoothA2DP: AVAudioSession.Port](./bluetootha2dp.md)
  An output to a Bluetooth A2DP device.
- [static let bluetoothLE: AVAudioSession.Port](./bluetoothle.md)
  An output to a Bluetooth Low Energy (LE) device.
- [static let builtInReceiver: AVAudioSession.Port](./builtinreceiver.md)
  An output to the speaker you hold to your ear when you’re on a phone call.
- [static let builtInSpeaker: AVAudioSession.Port](./builtinspeaker.md)
  An output to the device’s built-in speaker.
- [static let HDMI: AVAudioSession.Port](./hdmi.md)
  An output to a High-Definition Multimedia Interface (HDMI) device.
- [static let lineOut: AVAudioSession.Port](./lineout.md)
  A line-level output to the dock connector.
- [static let mediaDeviceExtension: AVAudioSession.Port](./mediadeviceextension.md)
  Output to a media device vended through a system-wide extension that the user has installed


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/port/headphones)*