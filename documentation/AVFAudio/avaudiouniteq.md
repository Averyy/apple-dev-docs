# AVAudioUnitEQ

**Framework**: AVFAudio  
**Kind**: class

An object that implements a multiband equalizer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAudioUnitEQ
```

#### Overview

The [`AVAudioUnitEQFilterParameters`](avaudiouniteqfilterparameters.md) class encapsulates the filter parameters that the [`bands`](avaudiouniteq/bands.md) property array returns.

## Topics

### Creating an equalizer
- [init(numberOfBands: Int)](avaudiouniteq/init(numberofbands:).md)
  Creates an audio unit equalizer object with the specified number of bands.
### Getting and setting the equalizer values
- [class AVAudioUnitEQFilterParameters](avaudiouniteqfilterparameters.md)
  An object that encapsulates the parameters that the equalizer uses.
- [var bands: [AVAudioUnitEQFilterParameters]](avaudiouniteq/bands.md)
  An array of equalizer filter parameters.
- [var globalGain: Float](avaudiouniteq/globalgain.md)
  The overall gain adjustment that the audio unit applies to the signal, in decibels.

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
- [class AVAudioUnitDistortion](avaudiounitdistortion.md)
  An object that implements a multistage distortion effect.
- [class AVAudioUnitDelay](avaudiounitdelay.md)
  An object that implements a delay effect.
- [class AVAudioUnitReverb](avaudiounitreverb.md)
  An object that implements a reverb effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiouniteq)*