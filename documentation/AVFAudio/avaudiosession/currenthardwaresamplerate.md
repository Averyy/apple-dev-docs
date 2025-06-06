# currentHardwareSampleRate

**Framework**: AVFAudio  
**Kind**: property

The audio hardware sample rate, in hertz.

**Availability**:
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var currentHardwareSampleRate: Double { get }
```

#### Discussion

Obtain the value of this property after activating your audio session. After successful activation, the value of this property doesn’t change while your session remains active.

## See Also

- [var currentHardwareInputNumberOfChannels: Int](avaudiosession/currenthardwareinputnumberofchannels.md)
  The number of audio hardware input channels.
- [var currentHardwareOutputNumberOfChannels: Int](avaudiosession/currenthardwareoutputnumberofchannels.md)
  The number of audio hardware output channels.
- [var inputIsAvailable: Bool](avaudiosession/inputisavailable.md)
  A Boolean value that indicates whether a hardware audio input path is available.
- [var preferredHardwareSampleRate: Double](avaudiosession/preferredhardwaresamplerate.md)
  The preferred hardware sample rate, in hertz.
- [func setPreferredHardwareSampleRate(Double) throws](avaudiosession/setpreferredhardwaresamplerate(_:).md)
  Sets the preferred hardware sample rate for input and output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/currenthardwaresamplerate)*