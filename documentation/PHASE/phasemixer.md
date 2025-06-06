# PHASEMixer

**Framework**: PHASE  
**Kind**: class

An object that combines multiple audio signals into a single signal.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEMixer
```

#### Overview

Mixers provide a single point of control over the multiple audio signals they combine. To create a mixer, you provide the framework with a mixer definition; see [`PHASEMixerDefinition`](phasemixerdefinition.md).

Subclasses of this class define unique properties the app sets to control specific features. For example, the spatial mixer ([`PHASESpatialMixerDefinition`](phasespatialmixerdefinition.md)) adds environmental effects into the output audio signal.

## Topics

### Adjusting Volume
- [var gain: Double](phasemixer/gain.md)
  The mixer’s volume.
- [var gainMetaParameter: PHASEMetaParameter?](phasemixer/gainmetaparameter.md)
  A parameter that changes the mixer’s volume gradually over a period of time.
### Retrieving the Mixer Identifier
- [var identifier: String](phasemixer/identifier.md)
  A unique name for the mixer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASEChannelMixerDefinition](phasechannelmixerdefinition.md)
  An audio-layering object that routes sound directly to the device’s output.
- [class PHASEAmbientMixerDefinition](phaseambientmixerdefinition.md)
  An audio-layering object that outputs sound in a particular direction in 3D space.
- [class PHASEMixerDefinition](phasemixerdefinition.md)
  An object to initialize a mixer with a given configuration.
- [class PHASEDefinition](phasedefinition.md)
  A base class that adds a name to framework definitions.
- [Spatial Mixing](spatial-mixing.md)
  Define environmental characteristics that determine how sound plays in your app’s 3D soundscape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemixer)*