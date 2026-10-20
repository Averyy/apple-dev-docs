# PHASEEngine.UpdateMode

**Framework**: PHASE  
**Kind**: enum  
**Role**: Enumeration

Modes that determine when the framework consumes API calls and updates internal state.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum UpdateMode
```

```c
enum PHASEUpdateMode : NSInteger;
```

#### Overview

To define the manner in which PHASE processes commands and updates internal state, select an option from this enumeration and pass it to the `updateMode` parameter of the [`PHASEEngine`](../phaseengine.md) initializer, [`init(updateMode:)`](./init%28updatemode%29.md).

## Topics

### Modes
- [PHASEEngine.UpdateMode.automatic](./updatemode/automatic.md)
  A mode that indicates PHASE sets the timing of state adjustments.
- [PHASEEngine.UpdateMode.manual](./updatemode/manual.md)
  A mode that indicates the app controls when the framework adjusts state.
### Initializers
- [init?(rawValue: Int)](./updatemode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Setup
- [class PHASEEngine](../phaseengine.md)
  An object that manages audio assets, controls playback, and configures environmental effects.
- [PHASEEngine.RenderingMode](./renderingmode.md)
  Modes that determine whether the system renders audio in process or out of process.
- [class PHASEAssetRegistry](../phaseassetregistry.md)
  A central repository of audio assets.
- [enum PHASENormalizationMode](../phasenormalizationmode.md)
  Options that determine whether the framework adjusts a sound asset’s loudness for the user’s output device.
- [enum PHASESpatializationMode](../phasespatializationmode.md)
  The manner in which PHASE outputs spatial audio.
- [enum PHASEReverbPreset](../phasereverbpreset.md)
  The manner in which PHASE diffuses resonating sound.
- [class PHASEMedium](../phasemedium.md)
  A property or quality of the environment that affects how sound travels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/updatemode)*