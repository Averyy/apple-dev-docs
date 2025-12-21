# PHASENormalizationMode

**Framework**: PHASE  
**Kind**: enum

Options that determine whether the framework adjusts a sound asset’s loudness for the user’s output device.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum PHASENormalizationMode
```

#### Overview

Different output devices feature loudness characteristics that require the audio engine to adjust the volume of the input audio to achieve a consistent listening experience across devices.

PHASE callibrates sound asset and stream loudness automatically when the app chooses [`PHASENormalizationMode.dynamic`](phasenormalizationmode/dynamic.md). If an app chooses [`PHASENormalizationMode.none`](phasenormalizationmode/none.md), the app needs to implement custom loudness normalizaton manually, by adjusting sound asset and stream signal strength for the user’s output device.

## Topics

### Loudness Normalization Modes
- [PHASENormalizationMode.dynamic](phasenormalizationmode/dynamic.md)
  A mode that instructs the framework to adjust a sound’s volume according to the user’s output device.
- [PHASENormalizationMode.none](phasenormalizationmode/none.md)
  A mode that instructs the framework not to adjust a sound’s volume according to the user’s output device.
### Initializers
- [init?(rawValue: Int)](phasenormalizationmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class PHASEEngine](phaseengine.md)
  An object that manages audio assets, controls playback, and configures environmental effects.
- [PHASEEngine.UpdateMode](phaseengine/updatemode.md)
  Modes that determine when the framework consumes API calls and updates internal state.
- [PHASEEngine.RenderingMode](phaseengine/renderingmode.md)
  Modes that determine whether the system renders audio in process or out of process.
- [class PHASEAssetRegistry](phaseassetregistry.md)
  A central repository of audio assets.
- [enum PHASESpatializationMode](phasespatializationmode.md)
  The manner in which PHASE outputs spatial audio.
- [enum PHASEReverbPreset](phasereverbpreset.md)
  The manner in which PHASE diffuses resonating sound.
- [class PHASEMedium](phasemedium.md)
  A property or quality of the environment that affects how sound travels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasenormalizationmode)*