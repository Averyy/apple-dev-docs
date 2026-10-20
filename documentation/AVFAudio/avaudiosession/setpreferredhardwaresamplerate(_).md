# setPreferredHardwareSampleRate(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Sets the preferred hardware sample rate for input and output.

**Availability**:
- Mac Catalyst 14.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`setPreferredSampleRate(_:)`](./setpreferredsamplerate%28_%29.md) instead.

## Declaration

```swift
func setPreferredHardwareSampleRate(_ sampleRate: Double) throws
```

```objc
- (BOOL) setPreferredHardwareSampleRate:(double) sampleRate error:(NSError **) outError;
```

## Parameters

- `sampleRate`: The hardware sample rate you want to use. The available range for hardware sample rate is device dependent.

## See Also

### Inspecting audio hardware
- [var currentHardwareInputNumberOfChannels: Int](./currenthardwareinputnumberofchannels.md)
  The number of audio hardware input channels.
- [var currentHardwareOutputNumberOfChannels: Int](./currenthardwareoutputnumberofchannels.md)
  The number of audio hardware output channels.
- [var currentHardwareSampleRate: Double](./currenthardwaresamplerate.md)
  The audio hardware sample rate, in hertz.
- [var inputIsAvailable: Bool](./inputisavailable.md)
  A Boolean value that indicates whether a hardware audio input path is available.
- [var preferredHardwareSampleRate: Double](./preferredhardwaresamplerate.md)
  The preferred hardware sample rate, in hertz.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setpreferredhardwaresamplerate(_:))*