# continuityMicrophone

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

An input from a Continuity Microphone on Apple TV.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static let continuityMicrophone: AVAudioSession.Port
```

```c
extern AVAudioSessionPort const AVAudioSessionPortContinuityMicrophone;
```

## Discussion

A Continuity Microphone is an iOS device that a user trusts to use for audio input on Apple TV.

## See Also

### Getting input ports
- [static let builtInMic: AVAudioSession.Port](./builtinmic.md)
  An input from a device’s built-in microphone.
- [static let headsetMic: AVAudioSession.Port](./headsetmic.md)
  An input from a wired headset’s built-in microphone.
- [static let lineIn: AVAudioSession.Port](./linein.md)
  A line-level input from the dock connector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/port/continuitymicrophone)*