# PHASEChannelMixerDefinition

**Framework**: PHASE  
**Kind**: class

An audio-layering object that routes sound directly to the device’s output.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEChannelMixerDefinition
```

#### Overview

Use this class to play one-time sounds such as menu clicks.

> **Note**:  If your audio playback requires 3D orienting or positioning, use [`PHASEAmbientMixerDefinition`](phaseambientmixerdefinition.md) or [`PHASESpatialMixerDefinition`](phasespatialmixerdefinition.md), respectively. For more information, see [`Spatial Mixing`](spatial-mixing.md).

This class defines the , which is the strategy the framework uses to send source mono or multichannel assets to the output for playback. The asset’s audio channels route to the output for playback according to the channel layout and runtime output conditions the app designates on an instance of this class.

This class minimizes  and  — that is, source audio channel conversion to a higher or lower number of channels. For example, although a spatial mixer overrides the use of output channels by panning to convey listener position and orientation, the channel mixer maintains source audio channel layout to preserve the listening experience of the source audio.

## Topics

### Creating a Channel Mixer
- [init(channelLayout: AVAudioChannelLayout)](phasechannelmixerdefinition/init(channellayout:).md)
  Creates a channel mixer with the given channel layout.
- [convenience init(channelLayout: AVAudioChannelLayout, identifier: String)](phasechannelmixerdefinition/init(channellayout:identifier:).md)
  Creates a named channel mixer with the given channel layout.
### Inspecting Channel Layout
- [var inputChannelLayout: AVAudioChannelLayout](phasechannelmixerdefinition/inputchannellayout.md)
  The channel layout of the mixer’s input audio.

## Relationships

### Inherits From
- [PHASEMixerDefinition](phasemixerdefinition.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASEAmbientMixerDefinition](phaseambientmixerdefinition.md)
  An audio-layering object that outputs sound in a particular direction in 3D space.
- [class PHASEMixerDefinition](phasemixerdefinition.md)
  An object to initialize a mixer with a given configuration.
- [class PHASEMixer](phasemixer.md)
  An object that combines multiple audio signals into a single signal.
- [class PHASEDefinition](phasedefinition.md)
  A base class that adds a name to framework definitions.
- [Spatial Mixing](spatial-mixing.md)
  Define environmental characteristics that determine how sound plays in your app’s 3D soundscape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasechannelmixerdefinition)*