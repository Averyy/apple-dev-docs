# setPreferredSampleRate(_:)

**Framework**: AVFAudio  
**Kind**: method

Sets the preferred sample rate for audio input and output.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setPreferredSampleRate(_ sampleRate: Double) throws
```

#### Discussion

This method requests a change to the input and output audio sample rate. To see the effect of this change, use the [`sampleRate`](avaudiosession/samplerate.md) property.

You can set a preferred sample rate before or after activating the audio session.

## Parameters

- `sampleRate`: The hardware sample rate to use. The available range is device dependent and is typically from 8000 through 48000 hertz.

## See Also

- [var sampleRate: Double](avaudiosession/samplerate.md)
  The current audio sample rate, in hertz.
- [var preferredSampleRate: Double](avaudiosession/preferredsamplerate.md)
  The preferred sample rate, in hertz.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setpreferredsamplerate(_:))*