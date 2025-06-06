# inputIsAvailable

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether a hardware audio input path is available.

**Availability**:
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var inputIsAvailable: Bool { get }
```

## See Also

- [var currentHardwareInputNumberOfChannels: Int](avaudiosession/currenthardwareinputnumberofchannels.md)
  The number of audio hardware input channels.
- [var currentHardwareOutputNumberOfChannels: Int](avaudiosession/currenthardwareoutputnumberofchannels.md)
  The number of audio hardware output channels.
- [var currentHardwareSampleRate: Double](avaudiosession/currenthardwaresamplerate.md)
  The audio hardware sample rate, in hertz.
- [var preferredHardwareSampleRate: Double](avaudiosession/preferredhardwaresamplerate.md)
  The preferred hardware sample rate, in hertz.
- [func setPreferredHardwareSampleRate(Double) throws](avaudiosession/setpreferredhardwaresamplerate(_:).md)
  Sets the preferred hardware sample rate for input and output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/inputisavailable)*