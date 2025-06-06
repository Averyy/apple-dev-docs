# feedback

**Framework**: AVFAudio  
**Kind**: property

The amount of the output signal that feeds back into the delay line.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var feedback: Float { get set }
```

#### Discussion

You specify the feedback as a percentage. The default value is `50%`. The valid range of values is `-100%` to `100%`.

## See Also

- [var delayTime: TimeInterval](avaudiounitdelay/delaytime.md)
  The time for the input signal to reach the output.
- [var lowPassCutoff: Float](avaudiounitdelay/lowpasscutoff.md)
  The cutoff frequency above which high frequency content rolls off, in hertz.
- [var wetDryMix: Float](avaudiounitdelay/wetdrymix.md)
  The blend of the wet and dry signals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitdelay/feedback)*