# rate

**Framework**: AVFAudio  
**Kind**: property

The audio playback rate.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var rate: Float { get set }
```

#### Discussion

The varispeed audio unit resamples the input signal, and as a result, changing the playback rate also changes the pitch. For example, changing the rate to `2.0` results in the output audio playing one octave higher. Similarly changing the rate to `0.5`, results in the output audio playing one octave lower.

The audio unit measures the pitch in , a logarithmic value you use for measuring musical intervals. One octave is equal to 1200 cents. One musical semitone is equal to 100 cents.

Using the `rate` value you calculate the pitch (in cents) using the formula `pitch = 1200.0 * log2(rate)`. Conversely, you calculate the appropriate `rate` for a desired pitch with the formula `rate = pow(2, cents/1200.0)`.

The default value is `1.0`. The range of values is `0.25` to `4.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitvarispeed/rate)*