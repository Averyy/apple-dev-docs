# PHASESource

**Framework**: PHASE  
**Kind**: class

An object that plays audio from a 3D location and orientation in a scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASESource
```

## Mentions

- [Playing sound from a location in a 3D scene](playing-sound-from-a-location-in-a-3d-scene.md)

#### Overview

This class represents a sound-emitting point or area in a virtual environment, positioned and oriented by a 3D [`transform`](phaseobject/transform.md).

A spatial mixer, [`PHASESpatialMixerDefinition`](phasespatialmixerdefinition.md), adds environmental effects to sound sources. To tie a mixer to a sound source, create a [`PHASEMixerParameters`](phasemixerparameters.md) object and pass it into the `mixerParameters` argument of a sound event’s [`init(engine:assetIdentifier:mixerParameters:)`](phasesoundevent/init(engine:assetidentifier:mixerparameters:).md) initializer.

For an example that demonstrates sound sources, see [`Playing sound from a location in a 3D scene`](playing-sound-from-a-location-in-a-3d-scene.md).

## Topics

### Creating a Source
- [init(engine: PHASEEngine)](phasesource/init(engine:).md)
  Creates a single point in the environment from which sound emanates.
- [init(engine: PHASEEngine, shapes: [PHASEShape])](phasesource/init(engine:shapes:).md)
  Creates a voluminous area in the environment from which sound emanates.
### Controlling Sound Volume
- [var gain: Double](phasesource/gain.md)
  The amount of sound the source emanates.
### Inspecting the Shape
- [var shapes: [PHASEShape]](phasesource/shapes.md)
  An array of shapes that collectively define the audio-emitting surface area of a volumetric source.

## Relationships

### Inherits From
- [PHASEObject](phaseobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASEListener](phaselistener.md)
  A central point of reference that defines the location within the scene that’s most audible to the user.
- [class PHASEOccluder](phaseoccluder.md)
  An object with a shape and position that blocks audio from reaching the listener.
- [class PHASEObject](phaseobject.md)
  An object in the scene.
- [class PHASEShape](phaseshape.md)
  A collection of points that connect to form a 3D volume.
- [PHASEShape.Element](phaseshape/element.md)
  An object that describes the characteristics of a physical surface.
- [class PHASEMaterial](phasematerial.md)
  Surface characteristics that determine the acoustic properties of an object.
- [enum PHASEMaterialPreset](phasematerialpreset.md)
  A collection of physical surfaces that each add a unique acoustic quality to your app’s audio.
- [class PHASEMixerParameters](phasemixerparameters.md)
  An object that specifies a mixer for sound events and orients them in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesource)*