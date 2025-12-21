# PHASEEngine.RenderingMode

**Framework**: PHASE  
**Kind**: enum

Modes that determine whether the system renders audio in process or out of process.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
enum RenderingMode
```

#### Overview

To define the manner in which PHASE renders audio content, select an option from this enumeration and pass it to the `renderingMode` parameter of the [`PHASEEngine`](phaseengine.md) initializer, [`init(updateMode:renderingMode:)`](phaseengine/init(updatemode:renderingmode:).md).

## Topics

### Modes
- [PHASEEngine.RenderingMode.local](phaseengine/renderingmode/local.md)
  A mode that indicates that the system renders audio in process.
- [PHASEEngine.RenderingMode.client](phaseengine/renderingmode/client.md)
  A mode that instructs the system to render audio in a secure process.
### Initializers
- [init?(rawValue: Int)](phaseengine/renderingmode/init(rawvalue:).md)

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
- [enum PHASESpatializationMode](phasespatializationmode.md)
  The manner in which PHASE outputs spatial audio.
- [enum PHASEReverbPreset](phasereverbpreset.md)
  The manner in which PHASE diffuses resonating sound.
- [class PHASEMedium](phasemedium.md)
  A property or quality of the environment that affects how sound travels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/renderingmode)*