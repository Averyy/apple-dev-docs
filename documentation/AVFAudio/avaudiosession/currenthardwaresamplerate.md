# currentHardwareSampleRate

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The audio hardware sample rate, in hertz.

**Availability**:
- Mac Catalyst 14.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`sampleRate`](./samplerate.md) instead

## Declaration

```swift
var currentHardwareSampleRate: Double { get }
```

```objc
@property (readonly) double currentHardwareSampleRate;
```

## Discussion

Obtain the value of this property after activating your audio session. After successful activation, the value of this property doesn’t change while your session remains active.

## See Also

### Inspecting audio hardware
- [var currentHardwareInputNumberOfChannels: Int](./currenthardwareinputnumberofchannels.md)
  The number of audio hardware input channels.
- [var currentHardwareOutputNumberOfChannels: Int](./currenthardwareoutputnumberofchannels.md)
  The number of audio hardware output channels.
- [var inputIsAvailable: Bool](./inputisavailable.md)
  A Boolean value that indicates whether a hardware audio input path is available.
- [var preferredHardwareSampleRate: Double](./preferredhardwaresamplerate.md)
  The preferred hardware sample rate, in hertz.
- [func setPreferredHardwareSampleRate(Double) throws](./setpreferredhardwaresamplerate%28_%29.md)
  Sets the preferred hardware sample rate for input and output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/currenthardwaresamplerate)*