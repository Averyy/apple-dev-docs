# currentHardwareInputNumberOfChannels

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The number of audio hardware input channels.

**Availability**:
- Mac Catalyst 14.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`inputNumberOfChannels`](./inputnumberofchannels.md) instead.

## Declaration

```swift
var currentHardwareInputNumberOfChannels: Int { get }
```

```objc
@property (readonly) NSInteger currentHardwareInputNumberOfChannels;
```

## See Also

### Inspecting audio hardware
- [var currentHardwareOutputNumberOfChannels: Int](./currenthardwareoutputnumberofchannels.md)
  The number of audio hardware output channels.
- [var currentHardwareSampleRate: Double](./currenthardwaresamplerate.md)
  The audio hardware sample rate, in hertz.
- [var inputIsAvailable: Bool](./inputisavailable.md)
  A Boolean value that indicates whether a hardware audio input path is available.
- [var preferredHardwareSampleRate: Double](./preferredhardwaresamplerate.md)
  The preferred hardware sample rate, in hertz.
- [func setPreferredHardwareSampleRate(Double) throws](./setpreferredhardwaresamplerate%28_%29.md)
  Sets the preferred hardware sample rate for input and output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/currenthardwareinputnumberofchannels)*