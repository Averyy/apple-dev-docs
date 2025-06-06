# loadFactoryReverbPreset(_:)

**Framework**: AVFAudio  
**Kind**: method

Loads one of the reverbs factory presets.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func loadFactoryReverbPreset(_ preset: AVAudioUnitReverbPreset)
```

#### Discussion

Loading a factory reverb preset changes the sound of the reverb. This is independent of the filter which follows the reverb in the signal chain.

## Parameters

- `preset`: A reverb preset to load.

## See Also

- [var enable: Bool](avaudioenvironmentreverbparameters/enable.md)
  A Boolean value that indicates whether reverberation is in an enabled state.
- [var level: Float](avaudioenvironmentreverbparameters/level.md)
  Controls the amount of reverb, in decibels.
- [var filterParameters: AVAudioUnitEQFilterParameters](avaudioenvironmentreverbparameters/filterparameters.md)
  A filter that the system applies to the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenvironmentreverbparameters/loadfactoryreverbpreset(_:))*