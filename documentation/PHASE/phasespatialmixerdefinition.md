# PHASESpatialMixerDefinition

**Framework**: PHASE  
**Kind**: class

An audio-layering object that produces environmental effects and plays sound with a 3D position and orientation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASESpatialMixerDefinition
```

## Mentions

- [Playing sound from a location in a 3D scene](playing-sound-from-a-location-in-a-3d-scene.md)

#### Overview

This class enables the app to define a relationship between a source and listener in six degrees of freedom: orientation (roll, pitch, yaw) and a 3D position (x, y, z).

The framework plays back an audio source with  (see [`distanceModelParameters`](phasespatialmixerdefinition/distancemodelparameters.md)), direct path transmission effects and any combination of environmental effects, such as reverb (see [`PHASESpatialPipeline`](phasespatialpipeline.md)), and directivity (see [`listenerDirectivityModelParameters`](phasespatialmixerdefinition/listenerdirectivitymodelparameters.md)). 

The result enables an app to implement directive point or omnidirectional sound sources — with or without direction, respectively — and volumetric sources with a defined shape.

For a walkthrough of spatial mixing, see [`Playing sound from a location in a 3D scene`](playing-sound-from-a-location-in-a-3d-scene.md).

## Topics

### Creating a Spatial Mixer
- [init(spatialPipeline: PHASESpatialPipeline)](phasespatialmixerdefinition/init(spatialpipeline:).md)
  Creates a mixer with the designated spatial pipeline.
- [convenience init(spatialPipeline: PHASESpatialPipeline, identifier: String)](phasespatialmixerdefinition/init(spatialpipeline:identifier:).md)
  Creates a named mixer with the designated spatial pipeline.
### Setting a Pipeline
- [var spatialPipeline: PHASESpatialPipeline](phasespatialmixerdefinition/spatialpipeline.md)
  An object that adds sound layers for environmental effects.
### Changing Sound Over Distance
- [var distanceModelParameters: PHASEDistanceModelParameters?](phasespatialmixerdefinition/distancemodelparameters.md)
  An effect that changes sound as it carries over a distance.
### Configuring Directivity
- [var listenerDirectivityModelParameters: PHASEDirectivityModelParameters?](phasespatialmixerdefinition/listenerdirectivitymodelparameters.md)
  A data set that determines how well the listener hears depending on its direction relative to a sound source.
- [var sourceDirectivityModelParameters: PHASEDirectivityModelParameters?](phasespatialmixerdefinition/sourcedirectivitymodelparameters.md)
  A data set that directs sound such that it’s louder when directed at the listener.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialmixerdefinition)*