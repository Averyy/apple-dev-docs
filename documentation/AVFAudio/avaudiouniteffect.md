# AVAudioUnitEffect

**Framework**: AVFAudio  
**Kind**: class

An object that processes audio in real time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAudioUnitEffect
```

#### Overview

This processing uses [`AudioUnit`](https://developer.apple.com/documentation/AudioToolbox/AudioUnit) of type effect, music effect, panner, remote effect, or remote music effect. These effects run in real time and process some number of audio input samples to produce several audio output samples. A delay unit is an example of an effect unit.

## Topics

### Creating an audio effect
- [init(audioComponentDescription: AudioComponentDescription)](avaudiouniteffect/init(audiocomponentdescription:).md)
  Creates an audio unit effect object with the specified description.
### Getting the bypass state
- [var bypass: Bool](avaudiouniteffect/bypass.md)
  The bypass state of the audio unit.

## Relationships

### Inherits From
- [AVAudioUnit](avaudiounit.md)
### Inherited By
- [AVAudioUnitDelay](avaudiounitdelay.md)
- [AVAudioUnitDistortion](avaudiounitdistortion.md)
- [AVAudioUnitEQ](avaudiouniteq.md)
- [AVAudioUnitReverb](avaudiounitreverb.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAudioUnitEQ](avaudiouniteq.md)
  An object that implements a multiband equalizer.
- [class AVAudioUnitDistortion](avaudiounitdistortion.md)
  An object that implements a multistage distortion effect.
- [class AVAudioUnitDelay](avaudiounitdelay.md)
  An object that implements a delay effect.
- [class AVAudioUnitReverb](avaudiounitreverb.md)
  An object that implements a reverb effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiouniteffect)*