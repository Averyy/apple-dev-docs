# wetDryMix

**Framework**: AVFAudio  
**Kind**: property

The blend of the wet and dry signals.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var wetDryMix: Float { get set }
```

#### Discussion

You specify the blend as a percentage. The default value is `100%`. The valid range of values is `0%` through `100%`, where `0%` represents all dry.

## See Also

- [var delayTime: TimeInterval](avaudiounitdelay/delaytime.md)
  The time for the input signal to reach the output.
- [var feedback: Float](avaudiounitdelay/feedback.md)
  The amount of the output signal that feeds back into the delay line.
- [var lowPassCutoff: Float](avaudiounitdelay/lowpasscutoff.md)
  The cutoff frequency above which high frequency content rolls off, in hertz.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitdelay/wetdrymix)*