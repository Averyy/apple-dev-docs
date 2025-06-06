# AVAudioUnitDelay

**Framework**: AVFAudio  
**Kind**: class

An object that implements a delay effect.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAudioUnitDelay
```

#### Overview

A delay unit delays the input signal by the specified time interval and then blends it with the input signal. You can also control the amount of high-frequency roll-off to simulate the effect of a tape delay.

## Topics

### Getting and setting the delay values
- [var delayTime: TimeInterval](avaudiounitdelay/delaytime.md)
  The time for the input signal to reach the output.
- [var feedback: Float](avaudiounitdelay/feedback.md)
  The amount of the output signal that feeds back into the delay line.
- [var lowPassCutoff: Float](avaudiounitdelay/lowpasscutoff.md)
  The cutoff frequency above which high frequency content rolls off, in hertz.
- [var wetDryMix: Float](avaudiounitdelay/wetdrymix.md)
  The blend of the wet and dry signals.

## Relationships

### Inherits From
- [AVAudioUnitEffect](avaudiouniteffect.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAudioUnitEffect](avaudiouniteffect.md)
  An object that processes audio in real time.
- [class AVAudioUnitEQ](avaudiouniteq.md)
  An object that implements a multiband equalizer.
- [class AVAudioUnitDistortion](avaudiounitdistortion.md)
  An object that implements a multistage distortion effect.
- [class AVAudioUnitReverb](avaudiounitreverb.md)
  An object that implements a reverb effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitdelay)*