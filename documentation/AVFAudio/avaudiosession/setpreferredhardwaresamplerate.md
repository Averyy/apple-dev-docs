# setPreferredHardwareSampleRate(_:)

**Framework**: AVFAudio  
**Kind**: method

Sets the preferred hardware sample rate for input and output.

**Availability**:
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func setPreferredHardwareSampleRate(_ sampleRate: Double) throws
```

## Parameters

- `sampleRate`: The hardware sample rate you want to use. The available range for hardware sample rate is device dependent.

## See Also

- [var currentHardwareInputNumberOfChannels: Int](avaudiosession/currenthardwareinputnumberofchannels.md)
  The number of audio hardware input channels.
- [var currentHardwareOutputNumberOfChannels: Int](avaudiosession/currenthardwareoutputnumberofchannels.md)
  The number of audio hardware output channels.
- [var currentHardwareSampleRate: Double](avaudiosession/currenthardwaresamplerate.md)
  The audio hardware sample rate, in hertz.
- [var inputIsAvailable: Bool](avaudiosession/inputisavailable.md)
  A Boolean value that indicates whether a hardware audio input path is available.
- [var preferredHardwareSampleRate: Double](avaudiosession/preferredhardwaresamplerate.md)
  The preferred hardware sample rate, in hertz.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setpreferredhardwaresamplerate(_:))*