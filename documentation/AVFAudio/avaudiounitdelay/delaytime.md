# delayTime

**Framework**: AVFAudio  
**Kind**: property

The time for the input signal to reach the output.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var delayTime: TimeInterval { get set }
```

#### Discussion

You specify the delay in seconds. The default value is `1`. The valid range of values is `0` to `2` seconds.

## See Also

- [var feedback: Float](avaudiounitdelay/feedback.md)
  The amount of the output signal that feeds back into the delay line.
- [var lowPassCutoff: Float](avaudiounitdelay/lowpasscutoff.md)
  The cutoff frequency above which high frequency content rolls off, in hertz.
- [var wetDryMix: Float](avaudiounitdelay/wetdrymix.md)
  The blend of the wet and dry signals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitdelay/delaytime)*