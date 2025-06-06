# loadFactoryPreset(_:)

**Framework**: AVFAudio  
**Kind**: method

Configures the audio unit as a reverb preset.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func loadFactoryPreset(_ preset: AVAudioUnitReverbPreset)
```

#### Discussion

For more information about possible values, see [`AVAudioUnitReverbPreset`](avaudiounitreverbpreset.md). The default value is [`AVAudioUnitReverbPreset.mediumHall`](avaudiounitreverbpreset/mediumhall.md).

## Parameters

- `preset`: The reverb preset.

## See Also

- [enum AVAudioUnitReverbPreset](avaudiounitreverbpreset.md)
  Constants that represent preset reverbs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitreverb/loadfactorypreset(_:))*