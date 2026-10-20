# sampleRate

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The current audio sample rate, in hertz.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var sampleRate: Double { get }
```

```objc
@property (readonly) double sampleRate;
```

## See Also

### Configuring sample rate
- [var preferredSampleRate: Double](./preferredsamplerate.md)
  The preferred sample rate, in hertz.
- [func setPreferredSampleRate(Double) throws](./setpreferredsamplerate%28_%29.md)
  Sets the preferred sample rate for audio input and output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/samplerate)*