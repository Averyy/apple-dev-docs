# AVAudioUnitReverb

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAudioUnitReverb : AVAudioUnitEffect
```

## Overview

A reverb simulates the acoustic characteristics of a particular environment. Use the different presets to simulate a particular space and blend it in with the original signal using the [`wetDryMix`](./avaudiounitreverb/wetdrymix.md) property.

## Topics

### Loading a reverb preset
- [func loadFactoryPreset(AVAudioUnitReverbPreset)](./avaudiounitreverb/loadfactorypreset%28_%29.md)
  Configures the audio unit as a reverb preset.
- [enum AVAudioUnitReverbPreset](./avaudiounitreverbpreset.md)
  Constants that represent preset reverbs.
### Adjusting the wet-dry mix
- [var wetDryMix: Float](./avaudiounitreverb/wetdrymix.md)
  The blend of the wet and dry signals.

## Relationships

### Inherits From
- [AVAudioUnitEffect](./avaudiouniteffect.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Audio effects
- [class AVAudioUnitEQ](./avaudiouniteq.md)
  An object that implements a multiband equalizer.
- [class AVAudioUnitDistortion](./avaudiounitdistortion.md)
  An object that implements a multistage distortion effect.
- [class AVAudioUnitDelay](./avaudiounitdelay.md)
  An object that implements a delay effect.
- [class AVAudioUnitEffect](./avaudiouniteffect.md)
  An object that processes audio in real time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitreverb)*