# PHASEMixerDefinition

**Framework**: PHASE  
**Kind**: class

An object to initialize a mixer with a given configuration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEMixerDefinition
```

#### Overview

A mixer combines multiple layers of audio to a single signal for transmission to the output device. The framework creates a mixer when you provide a mixer definition. Instead of creating an instance of this class, instantiate one of the mixer definition subclasses instead:

##### Play a Sound Using a Mixer

To play a sound using a mixer, create a mixer definition and pass it to a sound event. The following code creates a [`PHASEChannelMixerDefinition`](phasechannelmixerdefinition.md) and passes it into a node definition the app can invoke to play the channel-based audio file `drumloopSoundAsset`:

```swift
// Create a channel mixer definition.
let stereoMixer = PHASEChannelMixerDefinition(channelLayout:stereoLayout!)

// Pass the mixer to a sound event node definition that plays an audio file.
let drumloopSamplerNode = PHASESamplerNodeDefinition(soundAssetIdentifier:drumloopSoundAsset.identifier, mixerDefinition:stereoMixer, identifier:"drumloopNode")
```

## Topics

### Controlling Volume
- [var gain: Double](phasemixerdefinition/gain.md)
  The mixer’s volume.
- [var gainMetaParameterDefinition: PHASENumberMetaParameterDefinition?](phasemixerdefinition/gainmetaparameterdefinition.md)
  A template for a parameter that changes the mixer’s volume gradually over a period of time.

## Relationships

### Inherits From
- [PHASEDefinition](phasedefinition.md)
### Inherited By
- [PHASEAmbientMixerDefinition](phaseambientmixerdefinition.md)
- [PHASEChannelMixerDefinition](phasechannelmixerdefinition.md)
- [PHASESpatialMixerDefinition](phasespatialmixerdefinition.md)
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
- [class PHASEMixer](phasemixer.md)
  An object that combines multiple audio signals into a single signal.
- [class PHASEDefinition](phasedefinition.md)
  A base class that adds a name to framework definitions.
- [Spatial Mixing](spatial-mixing.md)
  Define environmental characteristics that determine how sound plays in your app’s 3D soundscape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemixerdefinition)*