# PHASEMedium

**Framework**: PHASE  
**Kind**: class  
**Role**: Class

A property or quality of the environment that affects how sound travels.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEMedium
```

```objc
@interface PHASEMedium : NSObject
```

#### Overview

This class defines choices for the engine’s [`defaultMedium`](./phaseengine/defaultmedium.md). Currently, this property provides only sound traveling through air.

## Topics

### Creating a Medium
- [init(engine: PHASEEngine, preset: PHASEMedium.Preset)](./phasemedium/init%28engine,preset%29.md)
  Creates a medium.
- [PHASEMedium.Preset](./phasemedium/preset.md)
  Predetermined qualities of an environment that affect how sound transmits.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Setup
- [class PHASEEngine](./phaseengine.md)
  An object that manages audio assets, controls playback, and configures environmental effects.
- [PHASEEngine.UpdateMode](./phaseengine/updatemode.md)
  Modes that determine when the framework consumes API calls and updates internal state.
- [PHASEEngine.RenderingMode](./phaseengine/renderingmode.md)
  Modes that determine whether the system renders audio in process or out of process.
- [class PHASEAssetRegistry](./phaseassetregistry.md)
  A central repository of audio assets.
- [enum PHASENormalizationMode](./phasenormalizationmode.md)
  Options that determine whether the framework adjusts a sound asset’s loudness for the user’s output device.
- [enum PHASESpatializationMode](./phasespatializationmode.md)
  The manner in which PHASE outputs spatial audio.
- [enum PHASEReverbPreset](./phasereverbpreset.md)
  The manner in which PHASE diffuses resonating sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemedium)*