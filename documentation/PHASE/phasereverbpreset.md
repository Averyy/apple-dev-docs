# PHASEReverbPreset

**Framework**: PHASE  
**Kind**: enum

The manner in which PHASE diffuses resonating sound.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum PHASEReverbPreset
```

#### Overview

The PHASE engine requires your app to choose an option of this enumeration and assign it to the [`defaultReverbPreset`](phaseengine/defaultreverbpreset.md) property.

The value you choose adds resonation to sound that simulates the experience of hearing it in a particular environment. For example, a small room, [`PHASEReverbPreset.smallRoom`](phasereverbpreset/smallroom.md), adds very little reverberation compared to a large chamber, [`PHASEReverbPreset.largeChamber`](phasereverbpreset/largechamber.md).

## Topics

### Presets
- [PHASEReverbPreset.cathedral](phasereverbpreset/cathedral.md)
  A resonation that simulates the experience of hearing a sound in a cathedral.
- [PHASEReverbPreset.largeChamber](phasereverbpreset/largechamber.md)
  A resonation that simulates the experience of hearing a sound in a large chamber with specific dimensions.
- [PHASEReverbPreset.largeHall](phasereverbpreset/largehall.md)
  A resonation that simulates the experience of hearing a sound in a large hall with specific dimensions.
- [PHASEReverbPreset.largeHall2](phasereverbpreset/largehall2.md)
  A resonation that simulates the experience of hearing a sound in one kind of large hall with specific dimensions.
- [PHASEReverbPreset.largeRoom](phasereverbpreset/largeroom.md)
  A resonation that simulates the experience of hearing a sound in a large room with specific dimensions.
- [PHASEReverbPreset.largeRoom2](phasereverbpreset/largeroom2.md)
  A resonation that simulates the experience of hearing a sound in one kind of large room with specific dimensions.
- [PHASEReverbPreset.mediumChamber](phasereverbpreset/mediumchamber.md)
  A resonation that simulates the experience of hearing a sound in a medium-size chamber with specific dimensions.
- [PHASEReverbPreset.mediumHall](phasereverbpreset/mediumhall.md)
  A resonation that simulates the experience of hearing a sound in a medium-size hall with specific dimensions.
- [PHASEReverbPreset.mediumHall2](phasereverbpreset/mediumhall2.md)
  A resonation that simulates the experience of hearing a sound in one kind of medium-size hall with specific dimensions.
- [PHASEReverbPreset.mediumHall3](phasereverbpreset/mediumhall3.md)
  A resonation that simulates the experience of hearing a sound in another kind of medium-size hall with specific dimensions.
- [PHASEReverbPreset.mediumRoom](phasereverbpreset/mediumroom.md)
  A resonation that simulates the experience of hearing a sound in a medium-size room with specific dimensions.
- [PHASEReverbPreset.none](phasereverbpreset/none.md)
  An option that adds no reverberation to a sound.
- [PHASEReverbPreset.smallRoom](phasereverbpreset/smallroom.md)
  A resonation that simulates the experience of hearing a sound in a small room with specific dimensions.
### Initializers
- [init?(rawValue: Int)](phasereverbpreset/init(rawvalue:).md)

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
- [enum PHASENormalizationMode](phasenormalizationmode.md)
  Options that determine whether the framework adjusts a sound asset’s loudness for the user’s output device.
- [enum PHASESpatializationMode](phasespatializationmode.md)
  The manner in which PHASE outputs spatial audio.
- [class PHASEMedium](phasemedium.md)
  A property or quality of the environment that affects how sound travels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasereverbpreset)*