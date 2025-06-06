# AVAudioUnitReverb

**Framework**: AVFAudio  
**Kind**: class

An object that implements a reverb effect.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAudioUnitReverb
```

#### Overview

A reverb simulates the acoustic characteristics of a particular environment. Use the different presets to simulate a particular space and blend it in with the original signal using the [`wetDryMix`](avaudiounitreverb/wetdrymix.md) property.

## Topics

### Configure the reverb
- [func loadFactoryPreset(AVAudioUnitReverbPreset)](avaudiounitreverb/loadfactorypreset(_:).md)
  Configures the audio unit as a reverb preset.
- [enum AVAudioUnitReverbPreset](avaudiounitreverbpreset.md)
  Constants that represent preset reverbs.
### Getting and setting the reverb values
- [var wetDryMix: Float](avaudiounitreverb/wetdrymix.md)
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
- [class AVAudioUnitDelay](avaudiounitdelay.md)
  An object that implements a delay effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitreverb)*