# PHASEEngine.UpdateMode

**Framework**: PHASE  
**Kind**: enum

Modes that determine when the framework consumes API calls and updates internal state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum UpdateMode
```

#### Overview

To define the manner in which PHASE processes commands and updates internal state, select an option from this enumeration and pass it to the `updateMode` parameter of the [`PHASEEngine`](phaseengine.md) initializer, [`init(updateMode:)`](phaseengine/init(updatemode:).md).

## Topics

### Modes
- [PHASEEngine.UpdateMode.automatic](phaseengine/updatemode/automatic.md)
  A mode that indicates PHASE sets the timing of state adjustments.
- [PHASEEngine.UpdateMode.manual](phaseengine/updatemode/manual.md)
  A mode that indicates the app controls when the framework adjusts state.
### Initializers
- [init?(rawValue: Int)](phaseengine/updatemode/init(rawvalue:).md)

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
- [class PHASEAssetRegistry](phaseassetregistry.md)
  A central repository of audio assets.
- [enum PHASENormalizationMode](phasenormalizationmode.md)
  Options that determine whether the framework adjusts a sound asset’s loudness for the user’s output device.
- [enum PHASESpatializationMode](phasespatializationmode.md)
  The manner in which PHASE outputs spatial audio.
- [enum PHASEReverbPreset](phasereverbpreset.md)
  The manner in which PHASE diffuses resonating sound.
- [class PHASEMedium](phasemedium.md)
  A property or quality of the environment that affects how sound travels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/updatemode)*