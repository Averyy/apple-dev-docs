# AVAudioUnitDistortion

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that implements a multistage distortion effect.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAudioUnitDistortion
```

```objc
@interface AVAudioUnitDistortion : AVAudioUnitEffect
```

## Topics

### Configuring the distortion
- [func loadFactoryPreset(AVAudioUnitDistortionPreset)](./avaudiounitdistortion/loadfactorypreset%28_%29.md)
  Configures the audio distortion unit by loading a distortion preset.
- [enum AVAudioUnitDistortionPreset](./avaudiounitdistortionpreset.md)
  Constants that represent preset audio distortions.
### Adjusting gain and mix
- [var preGain: Float](./avaudiounitdistortion/pregain.md)
  The gain that the audio unit applies to the signal before distortion, in decibels.
- [var wetDryMix: Float](./avaudiounitdistortion/wetdrymix.md)
  The blend of the distorted and dry signals.

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
- [class AVAudioUnitDelay](./avaudiounitdelay.md)
  An object that implements a delay effect.
- [class AVAudioUnitReverb](./avaudiounitreverb.md)
  An object that implements a reverb effect.
- [class AVAudioUnitEffect](./avaudiouniteffect.md)
  An object that processes audio in real time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitdistortion)*