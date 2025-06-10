# PHASESpatializationMode

**Framework**: PHASE  
**Kind**: enum

The manner in which PHASE outputs spatial audio.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum PHASESpatializationMode
```

#### Overview

When your app outputs audio through a spatial mixer, [`PHASESpatialMixerDefinition`](phasespatialmixerdefinition.md), the PHASE engine requires your app to choose an option of this enumeration and assign it to the [`outputSpatializationMode`](phaseengine/outputspatializationmode.md) property.

## Topics

### Modes
- [PHASESpatializationMode.automatic](phasespatializationmode/automatic.md)
  A mode that indicates that the framework chooses the spatialization mode.
- [PHASESpatializationMode.alwaysUseBinaural](phasespatializationmode/alwaysusebinaural.md)
  A mode that introduces special processing to replicate a realistic spatial listening experience.
- [PHASESpatializationMode.alwaysUseChannelBased](phasespatializationmode/alwaysusechannelbased.md)
  A mode that adds a 3D position and orientation to sound by panning across the available output channels.
### Initializers
- [init?(rawValue: Int)](phasespatializationmode/init(rawvalue:).md)

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
- [class PHASEAssetRegistry](phaseassetregistry.md)
  A central repository of audio assets.
- [enum PHASENormalizationMode](phasenormalizationmode.md)
  Options that determine whether the framework adjusts a sound asset’s loudness for the user’s output device.
- [enum PHASEReverbPreset](phasereverbpreset.md)
  The manner in which PHASE diffuses resonating sound.
- [class PHASEMedium](phasemedium.md)
  A property or quality of the environment that affects how sound travels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatializationmode)*