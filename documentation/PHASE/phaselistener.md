# PHASEListener

**Framework**: PHASE  
**Kind**: class

A central point of reference that defines the location within the scene that’s most audible to the user.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEListener
```

## Mentions

- [Playing sound from a location in a 3D scene](playing-sound-from-a-location-in-a-3d-scene.md)

#### Overview

PHASE requires an instance of this class to play ambient or spatial audio. To output sound through an ambient mixer or spatial mixer, the app adds an instance of this class to a sound event by using [`PHASEMixerParameters`](phasemixerparameters.md).

For an example that demonstrates listeners, see [`Playing sound from a location in a 3D scene`](playing-sound-from-a-location-in-a-3d-scene.md).

## Topics

### Creating a Listener
- [init(engine: PHASEEngine)](phaselistener/init(engine:).md)
  Creates a listener with the given engine.
### Adjusting Loudness
- [var gain: Double](phaselistener/gain.md)
  Modifies the volume of all audio playback for the listener’s mixers.
### Instance Properties
- [var automaticHeadTrackingFlags: PHASEAutomaticHeadTrackingFlags](phaselistener/automaticheadtrackingflags.md)

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

- [class PHASESource](phasesource.md)
  An object that plays audio from a 3D location and orientation in a scene.
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

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaselistener)*