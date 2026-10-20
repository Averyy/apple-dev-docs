# preferredSampleRate

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The preferred sample rate, in hertz.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var preferredSampleRate: Double { get }
```

```objc
@property (readonly) double preferredSampleRate;
```

#### Discussion

The value of this property indicates the preferred sample rate set using the [`setPreferredSampleRate(_:)`](./setpreferredsamplerate%28_%29.md) method.

To determine the actual sample rate, query the [`sampleRate`](./samplerate.md) property.

## See Also

### Configuring sample rate
- [var sampleRate: Double](./samplerate.md)
  The current audio sample rate, in hertz.
- [func setPreferredSampleRate(Double) throws](./setpreferredsamplerate%28_%29.md)
  Sets the preferred sample rate for audio input and output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/preferredsamplerate)*