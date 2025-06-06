# PHASEOccluder

**Framework**: PHASE  
**Kind**: class

An object with a shape and position that blocks audio from reaching the listener.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEOccluder
```

## Mentions

- [Playing sound from a location in a 3D scene](playing-sound-from-a-location-in-a-3d-scene.md)

#### Overview

The framework lowers the volume of an audio signal when an instance of this class positions somewhere along the path between the sound source and the listener.

For an example that demonstrates sound occlusion, see [`Playing sound from a location in a 3D scene`](playing-sound-from-a-location-in-a-3d-scene.md).

## Topics

### Creating an Occluder
- [init(engine: PHASEEngine, shapes: [PHASEShape])](phaseoccluder/init(engine:shapes:).md)
  Creates an occluder with the given engine and shapes.
### Inspecting the Shape
- [var shapes: [PHASEShape]](phaseoccluder/shapes.md)
  An array of shapes that collectively define the occluder’s audio-deflecting surface and texture.

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
- [class PHASEListener](phaselistener.md)
  A central point of reference that defines the location within the scene that’s most audible to the user.
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

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseoccluder)*