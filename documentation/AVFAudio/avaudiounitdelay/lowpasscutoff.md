# lowPassCutoff

**Framework**: AVFAudio  
**Kind**: property

The cutoff frequency above which high frequency content rolls off, in hertz.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var lowPassCutoff: Float { get set }
```

#### Discussion

The default value is `15000 Hz`. The valid range of values is `10 Hz` through `(sampleRate/2)`.

## See Also

- [var delayTime: TimeInterval](avaudiounitdelay/delaytime.md)
  The time for the input signal to reach the output.
- [var feedback: Float](avaudiounitdelay/feedback.md)
  The amount of the output signal that feeds back into the delay line.
- [var wetDryMix: Float](avaudiounitdelay/wetdrymix.md)
  The blend of the wet and dry signals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitdelay/lowpasscutoff)*