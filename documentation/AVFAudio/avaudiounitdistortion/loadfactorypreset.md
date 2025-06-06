# loadFactoryPreset(_:)

**Framework**: AVFAudio  
**Kind**: method

Configures the audio distortion unit by loading a distortion preset.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func loadFactoryPreset(_ preset: AVAudioUnitDistortionPreset)
```

#### Discussion

For more information about possible values for `preset`, see [`AVAudioUnitDistortionPreset`](avaudiounitdistortionpreset.md). The default value is [`AVAudioUnitDistortionPreset.drumsBitBrush`](avaudiounitdistortionpreset/drumsbitbrush.md).

## Parameters

- `preset`: The distortion preset.

## See Also

- [enum AVAudioUnitDistortionPreset](avaudiounitdistortionpreset.md)
  Constants that represent preset audio distortions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitdistortion/loadfactorypreset(_:))*