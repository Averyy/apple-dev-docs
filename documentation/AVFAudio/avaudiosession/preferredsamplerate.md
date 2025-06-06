# preferredSampleRate

**Framework**: AVFAudio  
**Kind**: property

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

#### Discussion

The value of this property indicates the preferred sample rate set using the [`setPreferredSampleRate(_:)`](avaudiosession/setpreferredsamplerate(_:).md) method.

To determine the actual sample rate, query the [`sampleRate`](avaudiosession/samplerate.md) property.

## See Also

- [var sampleRate: Double](avaudiosession/samplerate.md)
  The current audio sample rate, in hertz.
- [func setPreferredSampleRate(Double) throws](avaudiosession/setpreferredsamplerate(_:).md)
  Sets the preferred sample rate for audio input and output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/preferredsamplerate)*